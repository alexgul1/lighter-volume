import asyncio
import random
import time
from typing import Set, Dict, Optional, Tuple
import lighter

from src.config import Config
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger, Stats

logger = setup_logger(__name__, Config.LOG_LEVEL)


class TradingEngine:
    """
    Futures trading engine for Lighter Protocol.
    Opens and closes long/short positions with proper timing.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.client: Optional[lighter.SignerClient] = None
        self.api_client = None
        self.transaction_api = None

        # Trading state
        self.active_positions: Dict[str, dict] = {}  # token -> position info
        self.running = False
        self.stats = Stats()

        # Track order indices
        self.next_order_index = 1000
        self._order_index_lock = asyncio.Lock()

        # Track nonces
        self.current_nonce = 0
        self._nonce_lock = asyncio.Lock()

    async def initialize(self):
        """Initialize Lighter client"""
        try:
            # Initialize API client
            configuration = lighter.Configuration(Config.BASE_URL)
            self.api_client = lighter.ApiClient(configuration)
            self.transaction_api = lighter.TransactionApi(self.api_client)

            # Initialize signer client
            self.client = lighter.SignerClient(
                url=Config.BASE_URL,
                private_key=Config.API_KEY_PRIVATE_KEY,
                account_index=Config.ACCOUNT_INDEX,
                api_key_index=Config.API_KEY_INDEX
            )

            # Check client
            err = self.client.check_client()
            if err is not None:
                raise Exception(f"Client check failed: {err}")

            # Get initial nonce
            next_nonce = await self.transaction_api.next_nonce(
                account_index=Config.ACCOUNT_INDEX,
                api_key_index=Config.API_KEY_INDEX
            )
            self.current_nonce = next_nonce.nonce

            # Set leverage for all markets
            await self._set_leverage_for_markets()

            logger.info(f"Trading engine initialized (Account type: {Config.ACCOUNT_TYPE})")
            logger.info(f"Default leverage: {Config.DEFAULT_LEVERAGE}x")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def _set_leverage_for_markets(self):
        """Set leverage for all trading markets"""
        for token in Config.TRADING_TOKENS:
            market_index = Config.MARKET_INDICES.get(token)
            if market_index is None:
                continue

            try:
                # Calculate Initial Margin Fraction (IMF) from leverage
                # IMF = 10000 / leverage (as per signer_client.py)
                imf = int(10000 / Config.DEFAULT_LEVERAGE)

                # Sign leverage update
                tx_info, error = self.client.sign_update_leverage(
                    market_index=market_index,
                    fraction=imf,
                    margin_mode=self.client.CROSS_MARGIN_MODE,  # Use cross margin
                    nonce=await self.get_next_nonce()
                )

                if error:
                    logger.error(f"Failed to sign leverage update for {token}: {error}")
                    continue

                # Send transaction
                result = await self.transaction_api.send_tx(
                    tx_type=self.client.TX_TYPE_UPDATE_LEVERAGE,
                    tx_info=tx_info
                )

                logger.info(f"Set leverage {Config.DEFAULT_LEVERAGE}x for {token}")
                await asyncio.sleep(1)  # Small delay between leverage updates

            except Exception as e:
                logger.error(f"Failed to set leverage for {token}: {e}")

    async def cleanup(self):
        """Cleanup resources"""
        if self.client:
            await self.client.close()
        if self.api_client:
            await self.api_client.close()

    async def get_next_order_index(self) -> int:
        """Get unique order index"""
        async with self._order_index_lock:
            index = self.next_order_index
            self.next_order_index += 1
            return index

    async def get_next_nonce(self) -> int:
        """Get next nonce"""
        async with self._nonce_lock:
            nonce = self.current_nonce
            self.current_nonce += 1
            return nonce

    async def start(self):
        """Start trading bot"""
        self.running = True
        logger.info("🚀 Futures trading bot started")
        logger.info(f"Tokens: {Config.TRADING_TOKENS}")
        logger.info(f"Position size: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}")
        logger.info(f"Hold time: {Config.POSITION_HOLD_TIME_MIN}-{Config.POSITION_HOLD_TIME_MAX}s")

        await self._trading_loop()

    async def stop(self):
        """Stop trading bot"""
        self.running = False

        # Close any open positions
        for token, position in self.active_positions.items():
            logger.info(f"Closing open position for {token}")
            await self._close_position(token, position)

        logger.info("Trading bot stopped")
        logger.info(self.stats.get_stats_string())

    async def _trading_loop(self):
        """Main trading loop"""
        while self.running:
            try:
                # Select random token
                available_tokens = [
                    token for token in Config.TRADING_TOKENS
                    if token not in self.active_positions
                ]

                if not available_tokens:
                    await asyncio.sleep(2)
                    continue

                token = random.choice(available_tokens)

                # Open a position
                await self._open_position(token)

                # Wait before next trade
                await asyncio.sleep(Config.DELAY_BETWEEN_TRADES)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(5)

    async def _open_position(self, token: str):
        """Open a long or short position"""

        # Get market index
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            logger.error(f"Unknown market for token {token}")
            return

        # Random position type
        is_long = random.choice([True, False])
        position_type = "long" if is_long else "short"

        # Random amount in USDC
        amount_usdc = round(random.uniform(
            Config.MIN_TRADE_AMOUNT,
            Config.MAX_TRADE_AMOUNT
        ), 2)

        # Calculate base amount (seems to be integer in examples)
        # From examples: BaseAmount of 11 for ~$10-12 position
        # This suggests BaseAmount might be position size in dollars or a scaled value
        base_amount = int(amount_usdc)

        # Calculate price with max slippage
        # From examples: prices are like 1112032, which is $11,120.32
        # So price is in cents (multiply by 100)
        if is_long:
            # For long: buy at any price (high limit)
            price = 999999999
            is_ask = False  # Buy to open long
        else:
            # For short: sell at any price (low limit)
            price = 1
            is_ask = True  # Sell to open short

        try:
            logger.info(f"📈 Opening {position_type.upper()} {token}: ${amount_usdc}")

            # Get order index and nonce
            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            # Sign order
            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=base_amount,
                price=price,
                is_ask=is_ask,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=False,  # False for opening position
                trigger_price=0,
                order_expiry=0,  # 0 for IOC
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign open order: {error}")
                return

            # Send transaction
            result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            # Log transaction
            tx = Transaction(
                tx_type="open",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=price,
                is_success=True,
                order_id=str(order_index),
                tx_hash=str(result) if result else None
            )
            open_tx_id = await self.db.log_transaction(tx)

            # Store position info
            self.active_positions[token] = {
                "position_type": position_type,
                "is_long": is_long,
                "base_amount": base_amount,
                "amount_usdc": amount_usdc,
                "open_tx_id": open_tx_id,
                "open_time": time.time()
            }

            logger.info(f"✅ Opened {position_type} position for {token}")
            self.stats.add_position(True, amount_usdc, is_long)

            # Schedule position close
            hold_time = random.uniform(
                Config.POSITION_HOLD_TIME_MIN,
                Config.POSITION_HOLD_TIME_MAX
            )
            asyncio.create_task(self._schedule_close_position(token, hold_time))

        except Exception as e:
            logger.error(f"Failed to open position for {token}: {e}")

            # Log failed transaction
            tx = Transaction(
                tx_type="open",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=price,
                is_success=False,
                error=str(e)
            )
            await self.db.log_transaction(tx)

    async def _schedule_close_position(self, token: str, hold_time: float):
        """Schedule closing a position after hold time"""
        await asyncio.sleep(hold_time)

        position = self.active_positions.get(token)
        if position:
            await self._close_position(token, position)

    async def _close_position(self, token: str, position: dict):
        """Close an open position"""

        # Get market index
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            return

        is_long = position["is_long"]
        position_type = position["position_type"]
        base_amount = position["base_amount"]
        amount_usdc = position["amount_usdc"]
        open_tx_id = position["open_tx_id"]

        # For closing: reverse the side
        if is_long:
            # Close long: sell
            price = 1  # Sell at any price
            is_ask = True
        else:
            # Close short: buy
            price = 999999999  # Buy at any price
            is_ask = False

        try:
            logger.info(f"📉 Closing {position_type.upper()} {token}")

            # Get order index and nonce
            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            # Sign order
            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=base_amount,
                price=price,
                is_ask=is_ask,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=True,  # True for closing position
                trigger_price=0,
                order_expiry=0,  # 0 for IOC
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign close order: {error}")
                return

            # Send transaction
            result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            # Log transaction
            tx = Transaction(
                tx_type="close",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=price,
                is_success=True,
                dependency=open_tx_id,
                order_id=str(order_index),
                tx_hash=str(result) if result else None
            )
            await self.db.log_transaction(tx)

            # Remove from active positions
            del self.active_positions[token]

            logger.info(f"✅ Closed {position_type} position for {token}")
            logger.info(self.stats.get_stats_string())

        except Exception as e:
            logger.error(f"Failed to close position for {token}: {e}")

            # Log failed transaction
            tx = Transaction(
                tx_type="close",
                position_type=position_type,
                token=token,
                amount_usdc=amount_usdc,
                base_amount=base_amount,
                price=price,
                is_success=False,
                dependency=open_tx_id,
                error=str(e)
            )
            await self.db.log_transaction(tx)