import asyncio
import time
from typing import Dict, Optional, List
from dataclasses import dataclass
import lighter

from src.config import Config
from src.utils import setup_logger

logger = setup_logger(__name__, Config.LOG_LEVEL)


@dataclass
class PositionSnapshot:
    """Snapshot of position state at a point in time"""
    timestamp: float
    symbol: str
    market_id: int
    position_size: float
    avg_entry_price: float
    current_price: float
    unrealized_pnl: float
    realized_pnl: float
    liquidation_price: float
    margin_mode: str
    allocated_margin: float


class PositionMonitor:
    """
    Monitors open positions in real-time via REST API polling.
    Tracks PnL, liquidation risks, and position changes.

    Since Lighter has no WebSocket support, this uses aggressive REST polling
    to achieve near-real-time monitoring (1-2 second intervals).
    """

    def __init__(
        self,
        account_api: lighter.AccountApi,
        order_api: lighter.OrderApi,
        account_1_index: int,
        account_2_index: int
    ):
        self.account_api = account_api
        self.order_api = order_api
        self.account_1_index = account_1_index
        self.account_2_index = account_2_index

        # Position snapshots: {f"acc{num}_market{id}": PositionSnapshot}
        self.current_positions: Dict[str, PositionSnapshot] = {}

        # Price cache: {market_id: (price, timestamp)}
        self.price_cache: Dict[int, tuple[float, float]] = {}
        self.price_cache_ttl = Config.PRICE_CACHE_TTL  # Adaptive TTL based on account type

        # Monitoring state
        self.running = False
        self.monitor_interval = Config.POSITION_MONITOR_INTERVAL

    async def start(self):
        """Start position monitoring loop"""
        self.running = True
        logger.info(f"Position monitor started (interval: {self.monitor_interval}s)")
        asyncio.create_task(self._monitor_loop())

    async def stop(self):
        """Stop position monitoring"""
        self.running = False
        logger.info("Position monitor stopped")

    async def _monitor_loop(self):
        """Main monitoring loop"""
        while self.running:
            try:
                await self._update_positions()
                await asyncio.sleep(self.monitor_interval)
            except Exception as e:
                logger.error(f"Position monitor error: {e}")
                await asyncio.sleep(self.monitor_interval * 2)  # Back off on error

    async def _update_positions(self):
        """Update all positions for both accounts"""
        try:
            # Fetch positions for both accounts concurrently
            account_1_task = self._fetch_account_positions(self.account_1_index, 1)
            account_2_task = self._fetch_account_positions(self.account_2_index, 2)

            await asyncio.gather(account_1_task, account_2_task, return_exceptions=True)

        except Exception as e:
            logger.error(f"Failed to update positions: {e}")

    async def _fetch_account_positions(self, account_index: int, account_num: int):
        """Fetch positions for a single account"""
        try:
            # Get account data
            response = await self.account_api.account(by="index", value=str(account_index))

            if not response.data:
                return

            account_data = response.data[0]

            # Process each position
            for position in account_data.positions:
                if float(position.position) == 0:
                    continue  # Skip closed positions

                # Get current price
                current_price = await self._get_current_price(position.market_id)

                # Create position snapshot
                key = f"acc{account_num}_market{position.market_id}"
                snapshot = PositionSnapshot(
                    timestamp=time.time(),
                    symbol=position.symbol,
                    market_id=position.market_id,
                    position_size=float(position.position),
                    avg_entry_price=float(position.avg_entry_price),
                    current_price=current_price,
                    unrealized_pnl=float(position.unrealized_pnl),
                    realized_pnl=float(position.realized_pnl),
                    liquidation_price=float(position.liquidation_price) if position.liquidation_price else 0.0,
                    margin_mode=position.margin_mode,
                    allocated_margin=float(position.allocated_margin)
                )

                # Check for significant changes
                old_snapshot = self.current_positions.get(key)
                if old_snapshot:
                    self._check_position_changes(old_snapshot, snapshot, account_num)

                # Update cache
                self.current_positions[key] = snapshot

        except Exception as e:
            logger.error(f"Failed to fetch positions for account {account_num}: {e}")

    async def _get_current_price(self, market_id: int) -> float:
        """
        Get current market price with caching.
        Uses recent trades endpoint for most accurate price.
        """
        current_time = time.time()

        # Check cache
        if market_id in self.price_cache:
            cached_price, cached_time = self.price_cache[market_id]
            if current_time - cached_time < self.price_cache_ttl:
                return cached_price

        try:
            # Fetch recent trade
            trades = await self.order_api.recent_trades(market_id=market_id, limit=1)

            if trades.data and len(trades.data) > 0:
                price = float(trades.data[0].price)
                self.price_cache[market_id] = (price, current_time)
                return price

        except Exception as e:
            logger.error(f"Failed to get price for market {market_id}: {e}")

        # Fallback to cached price or 0
        if market_id in self.price_cache:
            return self.price_cache[market_id][0]

        return 0.0

    def _check_position_changes(
        self,
        old: PositionSnapshot,
        new: PositionSnapshot,
        account_num: int
    ):
        """Check for significant position changes and log them"""

        # Check for size changes
        if abs(new.position_size - old.position_size) > 0.01:
            logger.info(
                f"Position size changed for {new.symbol} on Account {account_num}: "
                f"{old.position_size:.4f} → {new.position_size:.4f}"
            )

        # Check for significant PnL changes (>$1)
        pnl_change = abs(new.unrealized_pnl - old.unrealized_pnl)
        if pnl_change > 1.0:
            logger.debug(
                f"PnL update for {new.symbol} on Account {account_num}: "
                f"${new.unrealized_pnl:+.2f} (change: ${new.unrealized_pnl - old.unrealized_pnl:+.2f})"
            )

        # Check liquidation proximity (within 10%)
        if new.liquidation_price > 0:
            price_to_liq = abs(new.current_price - new.liquidation_price) / new.current_price
            if price_to_liq < 0.10:  # Within 10%
                logger.warning(
                    f"⚠️ Position {new.symbol} on Account {account_num} near liquidation! "
                    f"Current: ${new.current_price:.4f}, Liquidation: ${new.liquidation_price:.4f} "
                    f"({price_to_liq*100:.1f}% away)"
                )

    def get_position_snapshot(self, account_num: int, market_id: int) -> Optional[PositionSnapshot]:
        """Get current position snapshot for specific account and market"""
        key = f"acc{account_num}_market{market_id}"
        return self.current_positions.get(key)

    def get_all_positions(self) -> Dict[str, PositionSnapshot]:
        """Get all current position snapshots"""
        return self.current_positions.copy()

    def get_total_unrealized_pnl(self) -> float:
        """Calculate total unrealized PnL across all positions"""
        return sum(pos.unrealized_pnl for pos in self.current_positions.values())

    def get_account_pnl(self, account_num: int) -> float:
        """Get total PnL for specific account"""
        return sum(
            pos.unrealized_pnl + pos.realized_pnl
            for key, pos in self.current_positions.items()
            if key.startswith(f"acc{account_num}_")
        )

    def get_hedged_pair_pnl(self, market_id: int) -> Optional[tuple[float, float, float]]:
        """
        Calculate combined PnL for a hedged pair.

        Returns:
            (account_1_pnl, account_2_pnl, total_pnl) or None if pair not found
        """
        pos1 = self.get_position_snapshot(1, market_id)
        pos2 = self.get_position_snapshot(2, market_id)

        if not pos1 and not pos2:
            return None

        pnl1 = pos1.unrealized_pnl if pos1 else 0.0
        pnl2 = pos2.unrealized_pnl if pos2 else 0.0

        return (pnl1, pnl2, pnl1 + pnl2)
