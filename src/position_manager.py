import asyncio
import random
import time
import uuid
from typing import Dict, List, Optional
import lighter

from src.config import Config
from src.position import Position
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger

logger = setup_logger(__name__, Config.LOG_LEVEL)


class PositionManager:
    """Manages position lifecycle: open, TP/SL, close"""

    TX_TYPE_CREATE_ORDER = 14
    TX_TYPE_BATCH_CREATE = 28

    def __init__(self, client: lighter.SignerClient, transaction_api, db: DatabaseManager):
        self.client = client
        self.transaction_api = transaction_api
        self.db = db

        # Position tracking
        self.active_positions: Dict[str, Position] = {}
        self.positions_by_token: Dict[str, List[str]] = {}
        self.token_last_close_time: Dict[str, float] = {}

        # Order tracking
        self.next_order_index = 1000
        self._order_index_lock = asyncio.Lock()
        self.current_nonce = 0
        self._nonce_lock = asyncio.Lock()

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

    def set_initial_nonce(self, nonce: int):
        """Set initial nonce from API"""
        self.current_nonce = nonce

    def can_trade_token(self, token: str) -> bool:
        """Check if token is available for trading based on cooldown"""
        last_close = self.token_last_close_time.get(token, 0)
        time_since_close = time.time() - last_close
        return time_since_close >= Config.DELAY_BETWEEN_TRADES_PER_TOKEN

    def get_available_tokens(self) -> List[str]:
        """Get list of tokens available for trading"""
        return [token for token in Config.TRADING_TOKENS if self.can_trade_token(token)]

    async def open_position(self, token: str) -> Optional[Position]:
        """Open a new position for given token"""
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            logger.error(f"Unknown market for token {token}")
            return None

        position_id = str(uuid.uuid4())[:8]
        is_long = random.choice([True, False])
        position_type = "long" if is_long else "short"

        # Calculate amount based on token

        amount_usdc = round(random.uniform(
            Config.MIN_TRADE_AMOUNT,
            Config.MAX_TRADE_AMOUNT
        ), 2)

        base_amount = int(amount_usdc)

        # Price settings for market order
        if is_long:
            price = 999999999  # Max price for buy
            is_ask = False
        else:
            price = 1  # Min price for sell
            is_ask = True

        try:
            token_positions = self.positions_by_token.get(token, [])
            logger.info(f"📈 Opening {position_type.upper()} {token}: ${amount_usdc} "
                        f"(ID: {position_id}, Active: {len(token_positions)})")

            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=base_amount,
                price=price,
                is_ask=is_ask,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=False,
                trigger_price=0,
                order_expiry=0,
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign open order: {error}")
                return None

            result = await self.transaction_api.send_tx(
                tx_type=self.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            # Log to database
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

            # Create position object
            position = Position(
                position_id=position_id,
                token=token,
                market_index=market_index,
                position_type=position_type,
                is_long=is_long,
                base_amount=base_amount,
                amount_usdc=amount_usdc,
                open_order_index=order_index,
                open_tx_id=open_tx_id
            )

            # Track position
            self.active_positions[position_id] = position
            if token not in self.positions_by_token:
                self.positions_by_token[token] = []
            self.positions_by_token[token].append(position_id)

            logger.info(f"✅ Opened {position_type} {token} (ID: {position_id})")
            return position

        except Exception as e:
            logger.error(f"Failed to open position for {token}: {e}")
            return None

    async def close_position(self, position_id: str) -> bool:
        """Force close a position"""
        position = self.active_positions.get(position_id)
        if not position or position.is_closing:
            return False

        position.is_closing = True

        if position.is_long:
            price = 1  # Sell at any price
            is_ask = True
        else:
            price = 999999999  # Buy at any price
            is_ask = False

        try:
            logger.info(f"📉 Closing {position.position_type} {position.token} (ID: {position_id})")

            order_index = await self.get_next_order_index()
            nonce = await self.get_next_nonce()

            tx_info, error = self.client.sign_create_order(
                market_index=position.market_index,
                client_order_index=order_index,
                base_amount=position.base_amount,
                price=price,
                is_ask=is_ask,
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=True,
                trigger_price=0,
                order_expiry=0,
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign close order: {error}")
                position.is_closing = False
                return False

            await self.transaction_api.send_tx(
                tx_type=self.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            self.handle_position_closed(position_id, "Manual close")
            return True

        except Exception as e:
            logger.error(f"Failed to close position {position_id}: {e}")
            position.is_closing = False
            return False

    def handle_position_closed(self, position_id: str, reason: str):
        """Handle position closure and update tracking"""
        position = self.active_positions.get(position_id)
        if not position:
            return

        # Update last close time for token
        self.token_last_close_time[position.token] = time.time()

        # Remove from active positions
        del self.active_positions[position_id]

        # Remove from token tracking
        if position.token in self.positions_by_token:
            self.positions_by_token[position.token].remove(position_id)
            if not self.positions_by_token[position.token]:
                del self.positions_by_token[position.token]

        remaining = len(self.positions_by_token.get(position.token, []))
        logger.info(f"✅ Closed {position.position_type} {position.token} "
                    f"(ID: {position_id}, Reason: {reason}, Remaining: {remaining})")