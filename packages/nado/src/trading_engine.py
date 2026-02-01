"""
Nado.xyz Fast Token Rotation Trading Engine

Uses official nado-protocol SDK for trading operations.
"""
import asyncio
import random
import time
import logging
from typing import Optional, Dict
from dataclasses import dataclass, field

from nado_protocol.client import create_nado_client, NadoClient, NadoClientMode
from nado_protocol.engine_client.types.execute import PlaceMarketOrderParams
from nado_protocol.utils.execute import MarketOrderParams
from nado_protocol.utils.subaccount import SubaccountParams
from nado_protocol.utils.math import to_x18, from_x18

from src.config import Config

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
    Fast token rotation engine for Nado using official SDK.

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

        # Subaccount sender hex
        self._sender_hex: Optional[str] = None

    def _get_client_mode(self) -> NadoClientMode:
        """Map config network to SDK mode"""
        if Config.NETWORK == "mainnet":
            return NadoClientMode.MAINNET
        elif Config.NETWORK == "testnet":
            return NadoClientMode.TESTNET
        else:
            return NadoClientMode.DEVNET

    async def initialize(self):
        """Initialize the trading engine"""
        logger.info("Initializing Nado Trading Engine with official SDK...")

        # Validate config
        Config.validate()

        # Create client using official SDK
        mode = self._get_client_mode()
        private_key = Config.PRIVATE_KEY

        logger.info(f"Creating Nado client (mode={mode})...")
        self.client = create_nado_client(mode, private_key)

        # Get signer address and build sender hex
        signer_address = self.client.context.engine_client.signer.address
        self._sender_hex = self._build_sender_hex(signer_address, Config.SUBACCOUNT_NAME)

        logger.info(f"Client initialized:")
        logger.info(f"  Network: {Config.NETWORK}")
        logger.info(f"  Address: {signer_address}")
        logger.info(f"  Subaccount: {Config.SUBACCOUNT_NAME}")
        logger.info(f"  Sender: {self._sender_hex}")

        # Check subaccount exists
        info = self.client.subaccount.get_engine_subaccount_summary(self._sender_hex)
        if not info.exists:
            raise Exception(
                f"Subaccount does not exist. Please deposit at least $5 USDT0 first. "
                f"Sender: {self._sender_hex}"
            )

        # Log initial balance
        usdt_balance = self._get_usdt_balance(info)
        health = self._get_health(info)
        logger.info(f"Subaccount USDT0 balance: ${usdt_balance:,.2f}")
        logger.info(f"Health (initial): {health:.4f}")

        # Notify telegram
        if self.telegram:
            await self.telegram.send_message(
                f"*Nado Bot Started*\n\n"
                f"Network: `{Config.NETWORK}`\n"
                f"Address: `{signer_address[:10]}...`\n"
                f"Balance: ${usdt_balance:,.2f}\n"
                f"Products: {[Config.get_product_symbol(p) for p in Config.TRADING_PRODUCTS]}"
            )

        logger.info("Trading engine initialized successfully")

    def _build_sender_hex(self, address: str, subaccount_name: str) -> str:
        """Build sender bytes32 hex: address (20 bytes) + subaccount name (12 bytes)"""
        addr_hex = address.lower().replace("0x", "")
        name_bytes = subaccount_name.encode('utf-8')
        name_hex = name_bytes.hex().ljust(24, '0')  # 12 bytes = 24 hex chars
        return "0x" + addr_hex + name_hex

    def _get_usdt_balance(self, info) -> float:
        """Extract USDT balance from subaccount info"""
        for balance in info.spot_balances:
            if balance.product_id == 0:  # USDT0 is product 0
                # SpotProductBalance.balance is SpotBalance, SpotBalance.amount is str
                return from_x18(int(balance.balance.amount))
        return 0.0

    def _get_health(self, info) -> float:
        """Extract initial health from subaccount info"""
        if info.healths and len(info.healths) > 0:
            # SubaccountHealth.health is str
            return from_x18(int(info.healths[0].health))
        return 0.0

    async def cleanup(self):
        """Cleanup resources"""
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
                f"*Nado Bot Stopped*\n\n"
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
        """Execute a single rotation cycle: open -> wait -> close"""
        symbol = Config.get_product_symbol(product_id)
        logger.info(f"Starting rotation on {symbol}")

        # Random trade parameters
        trade_amount = random.uniform(Config.MIN_TRADE_AMOUNT, Config.MAX_TRADE_AMOUNT)
        is_long = random.choice([True, False])
        hold_time = random.uniform(Config.POSITION_HOLD_TIME_MIN, Config.POSITION_HOLD_TIME_MAX)

        # Get current price
        try:
            market = self.client.market.get_latest_market_price(product_id)
            # MarketPriceData has bid_x18 and ask_x18 as strings
            bid = from_x18(int(market.bid_x18))
            ask = from_x18(int(market.ask_x18))
            if bid == 0 or ask == 0:
                logger.warning(f"No market for {symbol}, skipping")
                return
        except Exception as e:
            logger.error(f"Failed to get market price for {symbol}: {e}")
            return

        current_price = (bid + ask) / 2
        trade_size = trade_amount / current_price  # Base asset size

        direction = "LONG" if is_long else "SHORT"
        logger.info(
            f"Opening {direction} {symbol}: ${trade_amount:.2f} "
            f"({trade_size:.6f} @ ${current_price:.2f})"
        )

        # Open position using SDK
        try:
            # Amount is positive for long, negative for short
            amount_x18 = to_x18(trade_size if is_long else -trade_size)

            # Build subaccount params
            subaccount = SubaccountParams(
                subaccount_owner=self.client.context.engine_client.signer.address,
                subaccount_name=Config.SUBACCOUNT_NAME
            )

            # Build market order params
            market_order = MarketOrderParams(
                sender=subaccount,
                amount=amount_x18,
                nonce=None  # SDK will generate
            )

            params = PlaceMarketOrderParams(
                product_id=product_id,
                market_order=market_order,
                slippage=0.01,  # 1% slippage
                spot_leverage=Config.USE_SPOT_LEVERAGE
            )

            result = self.client.market.place_market_order(params)

            self.stats.total_trades += 1
            self.stats.successful_trades += 1
            self.stats.total_volume_usd += trade_amount

            # Track position
            digest = result.data.digest if result.data else None
            self.positions[product_id] = ActivePosition(
                product_id=product_id,
                is_long=is_long,
                amount=trade_size,
                entry_price=current_price,
                open_time=time.time(),
                order_digest=digest
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
            market = self.client.market.get_latest_market_price(product_id)
            exit_price = (from_x18(int(market.bid_x18)) + from_x18(int(market.ask_x18))) / 2
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

        # Close using SDK's close_position method
        try:
            subaccount = SubaccountParams(
                subaccount_owner=self.client.context.engine_client.signer.address,
                subaccount_name=Config.SUBACCOUNT_NAME
            )

            result = self.client.market.close_position(subaccount, product_id)

            self.stats.total_trades += 1
            self.stats.successful_trades += 1
            self.stats.total_volume_usd += position.amount * exit_price

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
        info = self.client.subaccount.get_engine_subaccount_summary(self._sender_hex)
        usdt_balance = self._get_usdt_balance(info)

        return {
            "running": self.running,
            "address": self.client.context.engine_client.signer.address,
            "balance_usd": usdt_balance,
            "health": self._get_health(info),
            "open_positions": len(self.positions),
            "stats": {
                "total_trades": self.stats.total_trades,
                "successful_trades": self.stats.successful_trades,
                "success_rate": self.stats.success_rate,
                "total_volume": self.stats.total_volume_usd,
                "uptime_hours": self.stats.uptime_hours
            }
        }
