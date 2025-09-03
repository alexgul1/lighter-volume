# src/trading_engine.py
import asyncio
import json
import time
import random
from typing import Dict, List, Optional
import lighter

from src.config import Config
from src.position import Position
from src.position_manager import PositionManager
from src.database import DatabaseManager, Transaction
from src.websocket_manager import WebSocketManager
from src.utils import setup_logger, Stats

logger = setup_logger(__name__, Config.LOG_LEVEL)


class TradingEngine:
    """Main trading engine orchestrator"""

    TX_TYPE_CREATE_ORDER = 14
    TX_TYPE_BATCH_CREATE = 28

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.client: Optional[lighter.SignerClient] = None
        self.api_client = None
        self.transaction_api = None
        self.ws_manager: Optional[WebSocketManager] = None
        self.position_manager: Optional[PositionManager] = None
        self.running = False
        self.stats = Stats()

    async def initialize(self):
        """Initialize all components"""
        try:
            configuration = lighter.Configuration(Config.BASE_URL)
            self.api_client = lighter.ApiClient(configuration)
            self.transaction_api = lighter.TransactionApi(self.api_client)

            self.client = lighter.SignerClient(
                url=Config.BASE_URL,
                private_key=Config.API_KEY_PRIVATE_KEY,
                account_index=Config.ACCOUNT_INDEX,
                api_key_index=Config.API_KEY_INDEX
            )

            err = self.client.check_client()
            if err:
                raise Exception(f"Client check failed: {err}")

            next_nonce = await self.transaction_api.next_nonce(
                account_index=Config.ACCOUNT_INDEX,
                api_key_index=Config.API_KEY_INDEX
            )

            self.position_manager = PositionManager(self.client, self.transaction_api, self.db)
            self.position_manager.set_initial_nonce(next_nonce.nonce)

            auth_token, err = self.client.create_auth_token_with_expiry()
            if err:
                raise Exception(f"Failed to create auth token: {err}")

            self.ws_manager = WebSocketManager(Config.ACCOUNT_INDEX, auth_token)
            self.ws_manager.register_callback("on_position_update", self._on_position_update)
            self.ws_manager.register_callback("on_order_update", self._on_order_update)

            await self.ws_manager.connect()
            await self._set_leverage_for_markets()

            logger.info("Trading engine initialized")
            logger.info(f"TP: {Config.TAKE_PROFIT_PERCENT}%, SL: {Config.STOP_LOSS_PERCENT}%")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def _set_leverage_for_markets(self):
        """Set leverage for all markets"""
        for token in Config.TRADING_TOKENS:
            market_index = Config.MARKET_INDICES.get(token)
            if market_index is None:
                continue

            try:
                imf = int(10000 / Config.DEFAULT_LEVERAGE)
                tx_info, error = self.client.sign_update_leverage(
                    market_index=market_index,
                    fraction=imf,
                    margin_mode=self.client.CROSS_MARGIN_MODE,
                    nonce=await self.position_manager.get_next_nonce()
                )

                if not error:
                    await self.transaction_api.send_tx(
                        tx_type=self.client.TX_TYPE_UPDATE_LEVERAGE,
                        tx_info=tx_info
                    )
                    logger.info(f"Set leverage {Config.DEFAULT_LEVERAGE}x for {token}")
                    await asyncio.sleep(1)

            except Exception as e:
                logger.error(f"Failed to set leverage for {token}: {e}")

    async def start(self):
        """Start trading"""
        self.running = True
        logger.info("🚀 Trading started")
        await self._trading_loop()

    async def stop(self):
        """Stop trading"""
        self.running = False

        for position_id in list(self.position_manager.active_positions.keys()):
            await self.position_manager.close_position(position_id)

        logger.info(self.stats.get_stats_string())

    async def cleanup(self):
        """Cleanup resources"""
        if self.ws_manager:
            await self.ws_manager.disconnect()
        if self.client:
            await self.client.close()
        if self.api_client:
            await self.api_client.close()

    async def _trading_loop(self):
        """Main trading loop"""
        while self.running:
            try:
                available_tokens = self.position_manager.get_available_tokens()

                if available_tokens:
                    token = random.choice(available_tokens)
                    position = await self.position_manager.open_position(token)

                    if position:
                        self.stats.add_position(True, position.amount_usdc, position.is_long)

                        hold_time = random.uniform(
                            Config.POSITION_HOLD_TIME_MIN,
                            Config.POSITION_HOLD_TIME_MAX
                        )
                        asyncio.create_task(self._schedule_fallback_close(position.position_id, hold_time))

                await asyncio.sleep(0.5)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(5)

    async def _schedule_fallback_close(self, position_id: str, hold_time: float):
        """Schedule fallback close if TP/SL don't trigger"""
        await asyncio.sleep(hold_time)

        position = self.position_manager.active_positions.get(position_id)
        if position and not position.is_closing:
            logger.info(f"⏰ Fallback close for {position_id}")
            await self.position_manager.close_position(position_id)
            # self.stats.record_close("Manual")

    async def _on_position_update(self, market_id: str, position_data: Dict):
        """Handle position update from WebSocket - detect opened position and place TP/SL"""
        try:
            market_index = int(market_id)
            avg_entry_price = float(position_data.get("avg_entry_price", "0"))

            if avg_entry_price <= 0:
                return

            for position_id, position in self.position_manager.active_positions.items():
                if position.market_index == market_index and not position.tp_sl_placed:
                    position.calculate_tp_sl(
                        avg_entry_price,
                        Config.TAKE_PROFIT_PERCENT,
                        Config.STOP_LOSS_PERCENT
                    )

                    logger.info(f"📊 Position {position_id} entry: ${avg_entry_price:.2f}")
                    logger.info(f"   TP: ${position.tp_price:.2f}, SL: ${position.sl_price:.2f}")

                    await self._place_tp_sl_batch(position)
                    break

        except Exception as e:
            logger.error(f"Error handling position update: {e}")

    async def _place_tp_sl_batch(self, position: Position):
        """Place TP and SL orders using TX_TYPE 28 batch transaction"""
        try:
            sl_trigger = position.get_sl_trigger_price()
            tp_trigger = position.get_tp_trigger_price()

            nonce = await self.position_manager.get_next_nonce()
            current_time_ms = int(time.time() * 1000)
            order_expiry = current_time_ms + (28 * 24 * 60 * 60 * 1000)

            # Prepare batch order structure (TX_TYPE 28)
            batch_orders = {
                "AccountIndex": Config.ACCOUNT_INDEX,
                "ApiKeyIndex": Config.API_KEY_INDEX,
                "GroupingType": 2,
                "Orders": [
                    {
                        "MarketIndex": position.market_index,
                        "ClientOrderIndex": 0,
                        "BaseAmount": 0,
                        "Price": 1,
                        "IsAsk": 1 if position.is_long else 0,
                        "Type": 2,  # Stop Loss
                        "TimeInForce": 0,
                        "ReduceOnly": 1,
                        "TriggerPrice": sl_trigger,
                        "OrderExpiry": order_expiry
                    },
                    {
                        "MarketIndex": position.market_index,
                        "ClientOrderIndex": 0,
                        "BaseAmount": 0,
                        "Price": 1,
                        "IsAsk": 1 if position.is_long else 0,
                        "Type": 4,  # Take Profit
                        "TimeInForce": 0,
                        "ReduceOnly": 1,
                        "TriggerPrice": tp_trigger,
                        "OrderExpiry": order_expiry
                    }
                ],
                "ExpiredAt": current_time_ms + 60000,
                "Nonce": nonce
            }

            # Sign batch (this needs custom implementation for TX_TYPE 28)
            # For now, we'll send through WebSocket
            tx_info = json.dumps(batch_orders)
            await self.ws_manager.send_transaction(self.TX_TYPE_BATCH_CREATE, tx_info)

            position.tp_sl_placed = True

            # Log TP/SL orders to database
            await self.db.log_transaction(Transaction(
                tx_type="tp_sl_batch",
                position_type=position.position_type,
                token=position.token,
                amount_usdc=position.amount_usdc,
                base_amount=position.base_amount,
                avg_entry_price=position.avg_entry_price,
                tp_price=position.tp_price,
                sl_price=position.sl_price,
                is_success=True,
                dependency=position.open_tx_id
            ))

            logger.info(f"✅ Placed TP/SL batch for {position.token}")

        except Exception as e:
            logger.error(f"Failed to place TP/SL batch: {e}")

    async def _on_order_update(self, market_id: str, orders: List[Dict]):
        """Handle order updates - detect filled TP/SL"""
        try:
            for order in orders:
                if order.get("status") == "filled" and order.get("reduce_only"):
                    # Find position with this market
                    for position_id, position in list(self.position_manager.active_positions.items()):
                        if position.market_index == int(market_id):
                            # Determine if it was TP or SL based on trigger price
                            order_price = float(order.get("trigger_price", "0"))
                            close_reason = "Unknown"

                            if position.tp_price and abs(order_price - position.tp_price * 100) < 10:
                                close_reason = "TP"
                            elif position.sl_price and abs(order_price - position.sl_price * 100) < 10:
                                close_reason = "SL"

                            self.position_manager.handle_position_closed(position_id, f"{close_reason} triggered")
                            # self.stats.record_close(close_reason)

                            # Log close to database
                            await self.db.log_transaction(Transaction(
                                tx_type="close",
                                position_type=position.position_type,
                                token=position.token,
                                amount_usdc=position.amount_usdc,
                                base_amount=position.base_amount,
                                avg_entry_price=position.avg_entry_price,
                                is_success=True,
                                dependency=position.open_tx_id
                            ))
                            break

        except Exception as e:
            logger.error(f"Error handling order update: {e}")
