import time
from typing import Optional


class Position:
    """Represents a single futures position with TP/SL tracking"""

    def __init__(self, position_id: str, token: str, market_index: int,
                 position_type: str, is_long: bool, base_amount: int,
                 amount_usdc: float, open_order_index: int, open_tx_id: int):
        self.position_id = position_id
        self.token = token
        self.market_index = market_index
        self.position_type = position_type  # "long" or "short"
        self.is_long = is_long
        self.base_amount = base_amount
        self.amount_usdc = amount_usdc
        self.open_order_index = open_order_index
        self.open_tx_id = open_tx_id
        self.open_time = time.time()

        # Will be set from WebSocket position update
        self.avg_entry_price: Optional[float] = None
        self.tp_price: Optional[float] = None
        self.sl_price: Optional[float] = None
        self.tp_sl_placed = False
        self.is_closing = False

    def calculate_tp_sl(self, avg_entry_price: float, tp_percent: float, sl_percent: float):
        """Calculate TP and SL prices based on entry price"""
        self.avg_entry_price = avg_entry_price

        if self.is_long:
            # Long position: TP above entry, SL below
            self.tp_price = avg_entry_price * (1 + tp_percent / 100)
            self.sl_price = avg_entry_price * (1 - sl_percent / 100)
        else:
            # Short position: TP below entry, SL above
            self.tp_price = avg_entry_price * (1 - tp_percent / 100)
            self.sl_price = avg_entry_price * (1 + sl_percent / 100)

    def get_sl_trigger_price(self) -> int:
        """Get stop loss trigger price in cents"""
        return int(self.sl_price * 100) if self.sl_price else 0

    def get_tp_trigger_price(self) -> int:
        """Get take profit trigger price in cents"""
        return int(self.tp_price * 100) if self.tp_price else 0