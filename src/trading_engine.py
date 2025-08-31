import asyncio
import random
import json
from typing import Set, Dict, Optional, List, Tuple
from datetime import datetime
import lighter

from src.config import Config
from src.database import DatabaseManager, Transaction
from src.utils import setup_logger, Stats

logger = setup_logger(__name__, Config.LOG_LEVEL)


class TradingEngine:
    """
    Optimized trading engine for maximum efficiency on standard accounts.
    Uses batch transactions to execute buy+sell in a single API call.
    """

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager
        self.client: Optional[lighter.SignerClient] = None
        self.api_client = None
        self.transaction_api = None

        # Trading state
        self.active_tokens: Set[str] = set()
        self.running = False
        self.stats = Stats()

        # Track order indices
        self.next_order_index = 10000
        self._order_index_lock = asyncio.Lock()

        # Track nonces
        self.current_nonce = 0
        self._nonce_lock = asyncio.Lock()

    async def initialize(self):
        """Initialize Lighter client - minimal API usage"""
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

            # Check client (one-time check)
            err = self.client.check_client()
            if err is not None:
                raise Exception(f"Client check failed: {err}")

            # Get initial nonce (only API call during init)
            next_nonce = await self.transaction_api.next_nonce(
                account_index=Config.ACCOUNT_INDEX,
                api_key_index=Config.API_KEY_INDEX
            )
            self.current_nonce = next_nonce.nonce

            logger.info(f"Trading engine initialized (Account type: {Config.ACCOUNT_TYPE})")
            logger.info(f"Max trades/minute: {Config.MAX_REQUESTS_PER_MINUTE}")

        except Exception as e:
            logger.error(f"Failed to initialize: {e}")
            raise

    async def cleanup(self):
        """Cleanup resources"""
        if self.client:
            await self.client.close()
        if self.api_client:
            await self.api_client.close()

    async def get_next_order_indices(self, count: int = 2) -> List[int]:
        """Get unique order indices for batch orders"""
        async with self._order_index_lock:
            indices = []
            for _ in range(count):
                indices.append(self.next_order_index)
                self.next_order_index += 1
            return indices

    async def get_next_nonces(self, count: int = 2) -> List[int]:
        """Get nonces for batch orders"""
        async with self._nonce_lock:
            nonces = []
            for _ in range(count):
                nonces.append(self.current_nonce)
                self.current_nonce += 1
            return nonces

    async def start(self):
        """Start trading bot"""
        self.running = True
        logger.info("🚀 Trading bot started - Maximum efficiency mode")
        logger.info(f"Tokens: {Config.TRADING_TOKENS}")
        logger.info(f"Amount range: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}")

        # Single trading loop for maximum efficiency
        await self._trading_loop()

    async def stop(self):
        """Stop trading bot"""
        self.running = False
        logger.info("Trading bot stopped")
        logger.info(self.stats.get_stats_string())

    async def _trading_loop(self):
        """
        Main trading loop - optimized for maximum swaps.
        Uses batch transactions to send buy+sell together.
        """
        consecutive_errors = 0

        while self.running:
            try:
                # Execute batch trade (buy + sell in one transaction)
                success = await self._execute_batch_trade()

                if success:
                    consecutive_errors = 0
                    logger.info(self.stats.get_stats_string())
                else:
                    consecutive_errors += 1
                    if consecutive_errors > 5:
                        logger.warning(f"Multiple consecutive errors ({consecutive_errors}), backing off...")
                        await asyncio.sleep(30)
                        consecutive_errors = 0

                # Fixed delay based on account type
                await asyncio.sleep(Config.SAFE_DELAY_BETWEEN_BATCHES)

            except Exception as e:
                logger.error(f"Trading loop error: {e}")
                await asyncio.sleep(10)

    async def _execute_batch_trade(self) -> bool:
        """
        Execute a batch transaction with buy + sell.
        This sends both orders in a single API call for maximum efficiency.
        """
        # Select random token
        token = random.choice(Config.TRADING_TOKENS)

        # Random amount
        amount_usdc = round(random.uniform(
            Config.MIN_TRADE_AMOUNT,
            Config.MAX_TRADE_AMOUNT
        ), 2)

        # Get market index
        market_index = Config.MARKET_INDICES.get(token)
        if market_index is None:
            logger.error(f"Unknown market for token {token}")
            return False

        try:
            # Convert USDC to base amount (6 decimals)
            base_amount = int(amount_usdc * 1_000_000)

            # Get order indices and nonces for batch
            order_indices = await self.get_next_order_indices(2)
            nonces = await self.get_next_nonces(2)

            logger.info(f"📊 Batch trade {token}: ${amount_usdc} USDC")

            # Calculate order expiry (10 minutes from now in milliseconds)
            import time
            order_expiry = int((time.time() + 600) * 1000)  # Convert to milliseconds

            # Sign buy order (market order with max slippage)
            buy_tx_info, buy_err = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_indices[0],
                base_amount=base_amount,
                price=Config.MAX_BUY_PRICE,  # Max price for market buy
                is_ask=False,  # Buy
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=False,
                trigger_price=0,
                order_expiry=order_expiry,  # Order expiry in milliseconds
                nonce=nonces[0]
            )

            if buy_err is not None:
                logger.error(f"Failed to sign buy order: {buy_err}")
                return False

            # Sign sell order (market order with min price)
            sell_tx_info, sell_err = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_indices[1],
                base_amount=base_amount,
                price=Config.MIN_SELL_PRICE,  # Min price for market sell
                is_ask=True,  # Sell
                order_type=self.client.ORDER_TYPE_MARKET,
                time_in_force=self.client.ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL,
                reduce_only=False,
                trigger_price=0,
                order_expiry=order_expiry,  # Order expiry in milliseconds
                nonce=nonces[1]
            )

            if sell_err is not None:
                logger.error(f"Failed to sign sell order: {sell_err}")
                return False

            # Prepare batch transaction
            tx_types = json.dumps([
                self.client.TX_TYPE_CREATE_ORDER,
                self.client.TX_TYPE_CREATE_ORDER
            ])
            tx_infos = json.dumps([buy_tx_info, sell_tx_info])

            # Send batch transaction (single API call for both orders)
            try:
                tx_hashes = await self.transaction_api.send_tx_batch(
                    tx_types=tx_types,
                    tx_infos=tx_infos
                )

                # Log transactions
                buy_tx = Transaction("buy", token, amount_usdc, True,
                                     order_id=str(order_indices[0]),
                                     tx_hash=str(tx_hashes) if tx_hashes else None)
                sell_tx = Transaction("sell", token, amount_usdc, True,
                                      order_id=str(order_indices[1]),
                                      tx_hash=str(tx_hashes) if tx_hashes else None)

                tx_ids = await self.db.log_batch_transactions([buy_tx, sell_tx])
                sell_tx.dependency = tx_ids[0]  # Link sell to buy

                self.stats.add_trade(True, amount_usdc * 2)  # Count both buy and sell

                logger.info(f"✅ Batch executed: {token} buy/sell for ${amount_usdc}")
                return True

            except Exception as e:
                logger.error(f"Batch transaction failed: {e}")

                # Log failed transactions
                buy_tx = Transaction("buy", token, amount_usdc, False,
                                     error=str(e))
                sell_tx = Transaction("sell", token, amount_usdc, False,
                                      error=str(e))
                await self.db.log_batch_transactions([buy_tx, sell_tx])

                self.stats.add_trade(False, 0)
                return False

        except Exception as e:
            logger.error(f"Batch trade error: {e}")
            return False