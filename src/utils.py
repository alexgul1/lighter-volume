import logging
import colorlog
from datetime import datetime


def setup_logger(name: str, level: str = "INFO") -> logging.Logger:
    """Setup colored logger"""
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(getattr(logging, level.upper()))

    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red,bg_white',
            }
        )
    )

    logger.addHandler(handler)
    return logger


class Stats:
    """Trading statistics tracker"""

    def __init__(self):
        self.start_time = datetime.now()
        self.total_trades = 0
        self.successful_trades = 0
        self.failed_trades = 0
        self.total_volume = 0.0

    def add_trade(self, success: bool, volume: float):
        """Add trade to statistics"""
        self.total_trades += 1
        self.total_volume += volume
        if success:
            self.successful_trades += 1
        else:
            self.failed_trades += 1

    def get_stats_string(self) -> str:
        """Get formatted statistics string"""
        runtime = datetime.now() - self.start_time
        hours = runtime.total_seconds() / 3600
        trades_per_hour = self.total_trades / hours if hours > 0 else 0

        return (
            f"Stats: {self.total_trades} trades "
            f"({self.successful_trades} success, {self.failed_trades} failed) | "
            f"Volume: ${self.total_volume:.2f} | "
            f"Rate: {trades_per_hour:.1f} trades/hour"
        )