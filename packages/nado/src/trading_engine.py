"""
Nado.xyz Fast Token Rotation Trading Engine

Implements fast buy/sell cycles on Nado DEX for volume generation.
"""
import asyncio
import random
import time
import logging
from typing import Optional, Dict, List
from dataclasses import dataclass, field

from src.config import Config
from src.client import NadoClient, OrderAppendix, from_x18

logger = logging.getLogger(__name__)


@dataclass
class TradeStats:
    """Trading statistics"""
    total_trades: int = 0
    successful_trades: int = 0
    failed_trades: int = 0
    total_volume_usd: float = 0.0
    start_time: float = field(default_factory=time.time)

    @property
    def success_rate(self) -> float:
        if self.total_trades == 0:
            return 0.0
        return self.successful_trades / self.total_trades * 100

    @property
    def uptime_hours(self) -> float:
        return (time.time() - self.start_time) / 3600

    def log_stats(self):
        logger.info(
            f"Stats: {self.successful_trades}/{self.total_trades} trades "
            f"({self.success_rate:.1f}% success), "
            f"${self.total_volume_usd:,.2f} volume, "
            f"{self.uptime_hours:.2f}h uptime"
        )


@dataclass
class ActivePosition:
    """Tracks an open position for closing"""
    product_id: int
    is_long: bool
    amount: float  # base asset amount
    entry_price: float
    open_time: float
    order_digest: Optional[str] = None


class TradingEngine:
    """
    Fast token rotation engine for Nado.

    Strategy:
    1. Open position (buy or sell)
    2. Wait brief period (5-30 seconds)
    3. Close position (opposite trade)
    4. Repeat on different products
    """

    def __init__(self, telegram_notifier=None):
        self.client: Optional[NadoClient] = None
        self.telegram = telegram_notifier
        self.running = False
        self.stats = TradeStats()

        # Active positions (product_id -> position)
        self.positions: Dict[int, ActivePosition] = {}

        # Product info cache
        self.products: Dict[int, Dict] = {}

    async def initialize(self):
        """Initialize the trading engine"""
        logger.info("Initializing Nado Trading Engine...")

        # Validate config
        Config.validate()

        # Create client
        self.client = NadoClient()

        # Fetch and cache products
        await self._load_products()

        # Check subaccount exists
        info = await self.client.get_subaccount_info()
        if not info.exists:
            raise Exception(
                f"Subaccount does not exist. Please deposit at least $5 USDT0 first. "
                f"Sender: {self.client.sender}"
            )

        # Log initial balance
        usdt_balance = from_x18(info.spot_balances.get(0, 0))
        logger.info(f"Subaccount USDT0 balance: ${usdt_balance:,.2f}")
        logger.info(f"Health (initial): {from_x18(info.health_initial):.4f}")

        # Notify telegram
        if self.telegram:
            await self.telegram.send_message(
                f"🚀 *Nado Bot Started*\n\n"
                f"Network: `{Config.NETWORK}`\n"
                f"Address: `{self.client.address[:10]}...`\n"
                f"Balance: ${usdt_balance:,.2f}\n"
                f"Products: {[Config.get_product_symbol(p) for p in Config.TRADING_PRODUCTS]}"
            )

        logger.info("Trading engine initialized successfully")

    async def _load_products(self):
        """Load product info from API"""
        products = await self.client.get_all_products()
        for product in products:
            pid = product.get("product_id")
            if pid is not None:
                self.products[pid] = product
        logger.info(f"Loaded {len(self.products)} products")

    async def cleanup(self):
        """Cleanup resources"""
        if self.client:
            await self.client.close()
        logger.info("Trading engine cleanup complete")

    async def start(self):
        """Start the trading loop"""
        self.running = True
        self.stats = TradeStats()

        logger.info("=" * 50)
        logger.info("Starting fast token rotation trading")
        logger.info(f"Products: {[Config.get_product_symbol(p) for p in Config.TRADING_PRODUCTS]}")
        logger.info(f"Trade size: ${Config.MIN_TRADE_AMOUNT} - ${Config.MAX_TRADE_AMOUNT}")
        logger.info(f"Hold time: {Config.POSITION_HOLD_TIME_MIN}s - {Config.POSITION_HOLD_TIME_MAX}s")
        logger.info(f"Rate limit delay: {Config.get_rate_limit_delay()}s")
        logger.info("=" * 50)

        try:
            await self._trading_loop()
        except Exception as e:
            logger.error(f"Trading loop error: {e}", exc_info=True)
            raise
        finally:
            self.stats.log_stats()

    async def stop(self):
        """Stop the trading loop"""
        logger.info("Stopping trading engine...")
        self.running = False

        # Close any open positions
        if self.positions:
            logger.info(f"Closing {len(self.positions)} open positions...")
            for product_id in list(self.positions.keys()):
                try:
                    await self._close_position(product_id)
                except Exception as e:
                    logger.error(f"Failed to close position {product_id}: {e}")

        self.stats.log_stats()

        if self.telegram:
            await self.telegram.send_message(
                f"🛑 *Nado Bot Stopped*\n\n"
                f"Total trades: {self.stats.total_trades}\n"
                f"Success rate: {self.stats.success_rate:.1f}%\n"
                f"Volume: ${self.stats.total_volume_usd:,.2f}\n"
                f"Uptime: {self.stats.uptime_hours:.2f}h"
            )

    async def _trading_loop(self):
        """Main trading loop"""
        while self.running:
            try:
                # Select random product
                product_id = random.choice(Config.TRADING_PRODUCTS)

                # Skip if we already have a position on this product
                if product_id in self.positions:
                    await asyncio.sleep(1)
                    continue

                # Execute rotation cycle
                await self._execute_rotation(product_id)

                # Delay between trades
                await asyncio.sleep(Config.DELAY_BETWEEN_TRADES)

            except Exception as e:
                logger.error(f"Trading loop iteration error: {e}")
                await asyncio.sleep(5)  # Wait before retry

    async def _execute_rotation(self, product_id: int):
        """
        Execute a single rotation cycle: open -> wait -> close
        """
        symbol = Config.get_product_symbol(product_id)
        logger.info(f"Starting rotation on {symbol}")

        # Random trade parameters
        trade_amount = random.uniform(Config.MIN_TRADE_AMOUNT, Config.MAX_TRADE_AMOUNT)
        is_long = random.choice([True, False])
        hold_time = random.uniform(Config.POSITION_HOLD_TIME_MIN, Config.POSITION_HOLD_TIME_MAX)

        # Get current price
        try:
            market = await self.client.get_market_price(product_id)
            if market.bid == 0 or market.ask == 0:
                logger.warning(f"No market for {symbol}, skipping")
                return
        except Exception as e:
            logger.error(f"Failed to get market price for {symbol}: {e}")
            return

        current_price = market.mid_price
        trade_size = trade_amount / current_price  # Base asset size

        direction = "LONG" if is_long else "SHORT"
        logger.info(
            f"Opening {direction} {symbol}: ${trade_amount:.2f} "
            f"({trade_size:.6f} @ ${current_price:.2f})"
        )

        # Open position
        try:
            result = await self.client.place_market_order(
                product_id=product_id,
                amount_usd=trade_amount,
                is_buy=is_long
            )

            self.stats.total_trades += 1
            self.stats.successful_trades += 1
            self.stats.total_volume_usd += trade_amount

            # Track position
            self.positions[product_id] = ActivePosition(
                product_id=product_id,
                is_long=is_long,
                amount=trade_size,
                entry_price=current_price,
                open_time=time.time(),
                order_digest=result.get("data", {}).get("digest")
            )

            logger.info(f"Opened {direction} {symbol} successfully")

        except Exception as e:
            logger.error(f"Failed to open {direction} {symbol}: {e}")
            self.stats.total_trades += 1
            self.stats.failed_trades += 1
            return

        # Wait hold time
        logger.info(f"Holding {symbol} for {hold_time:.1f}s...")
        await asyncio.sleep(hold_time)

        # Close position
        await self._close_position(product_id)

        # Rate limit delay
        await asyncio.sleep(Config.get_rate_limit_delay())

    async def _close_position(self, product_id: int):
        """Close an open position"""
        position = self.positions.get(product_id)
        if not position:
            return

        symbol = Config.get_product_symbol(product_id)
        direction = "LONG" if position.is_long else "SHORT"

        # Get current price for PnL calculation
        try:
            market = await self.client.get_market_price(product_id)
            exit_price = market.mid_price
        except:
            exit_price = position.entry_price

        # Calculate approximate PnL
        if position.is_long:
            pnl = (exit_price - position.entry_price) * position.amount
        else:
            pnl = (position.entry_price - exit_price) * position.amount

        logger.info(
            f"Closing {direction} {symbol}: "
            f"entry=${position.entry_price:.2f}, exit=${exit_price:.2f}, "
            f"PnL=${pnl:+.4f}"
        )

        # Close by placing opposite order
        try:
            close_amount_usd = position.amount * exit_price

            result = await self.client.place_market_order(
                product_id=product_id,
                amount_usd=close_amount_usd,
                is_buy=not position.is_long,  # Opposite direction
                reduce_only=True
            )

            self.stats.total_trades += 1
            self.stats.successful_trades += 1
            self.stats.total_volume_usd += close_amount_usd

            del self.positions[product_id]
            logger.info(f"Closed {direction} {symbol}, PnL: ${pnl:+.4f}")

        except Exception as e:
            logger.error(f"Failed to close {direction} {symbol}: {e}")
            self.stats.total_trades += 1
            self.stats.failed_trades += 1

            # Remove from tracking anyway to avoid stuck positions
            del self.positions[product_id]

    async def get_status(self) -> Dict:
        """Get current bot status"""
        info = await self.client.get_subaccount_info()
        usdt_balance = from_x18(info.spot_balances.get(0, 0))

        return {
            "running": self.running,
            "address": self.client.address,
            "balance_usd": usdt_balance,
            "health": from_x18(info.health_initial),
            "open_positions": len(self.positions),
            "stats": {
                "total_trades": self.stats.total_trades,
                "successful_trades": self.stats.successful_trades,
                "success_rate": self.stats.success_rate,
                "total_volume": self.stats.total_volume_usd,
                "uptime_hours": self.stats.uptime_hours
            }
        }
