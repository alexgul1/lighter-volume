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
        self.total_positions = 0
        self.successful_positions = 0
        self.failed_positions = 0
        self.total_volume = 0.0
        self.long_positions = 0
        self.short_positions = 0

    def add_position(self, success: bool, volume: float, is_long: bool):
        """Add position to statistics"""
        self.total_positions += 1
        self.total_volume += volume
        if is_long:
            self.long_positions += 1
        else:
            self.short_positions += 1
        if success:
            self.successful_positions += 1
        else:
            self.failed_positions += 1

    def get_stats_string(self) -> str:
        """Get formatted statistics string"""
        runtime = datetime.now() - self.start_time
        hours = runtime.total_seconds() / 3600
        positions_per_hour = self.total_positions / hours if hours > 0 else 0

        return (
            f"📊 Stats: {self.total_positions} positions "
            f"(L:{self.long_positions} S:{self.short_positions}) | "
            f"Success: {self.successful_positions} | "
            f"Volume: ${self.total_volume:.2f} | "
            f"Rate: {positions_per_hour:.1f}/hour"
        )