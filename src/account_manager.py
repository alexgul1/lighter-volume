"""
Account Manager - Coordinates isolated worker processes for each account

This module manages separate processes for each account to avoid
global singleton conflicts in lighter-sdk 0.1.4+
"""

import asyncio
import logging
import queue
from typing import Dict, Any, Optional
from multiprocessing import Process, Queue
from src.account_worker import worker_main
from src.config import Config

logger = logging.getLogger(__name__)


class AccountManager:
    """Manages isolated worker processes for dual accounts"""

    def __init__(self):
        self.config = self._prepare_config()
        self.workers = {}  # account_num -> Process

    def _prepare_config(self) -> Dict[str, Any]:
        """Prepare config dict for worker processes"""
        return {
            'BASE_URL': Config.BASE_URL,
            'ACCOUNT_1_PRIVATE_KEY': Config.ACCOUNT_1_PRIVATE_KEY,
            'ACCOUNT_1_INDEX': Config.ACCOUNT_1_INDEX,
            'ACCOUNT_1_API_KEY_INDEX': Config.ACCOUNT_1_API_KEY_INDEX,
            'ACCOUNT_2_PRIVATE_KEY': Config.ACCOUNT_2_PRIVATE_KEY,
            'ACCOUNT_2_INDEX': Config.ACCOUNT_2_INDEX,
            'ACCOUNT_2_API_KEY_INDEX': Config.ACCOUNT_2_API_KEY_INDEX,
        }

    async def execute_command(self, account_num: int, command: str, params: Dict[str, Any]) -> Any:
        """
        Execute a command in isolated worker process

        Args:
            account_num: Account number (1 or 2)
            command: Command to execute ('set_leverage', 'open_position', 'close_position')
            params: Command parameters

        Returns:
            Command result
        """
        # Create result queue for IPC
        result_queue = Queue()

        # Create and start worker process
        worker_process = Process(
            target=worker_main,
            args=(account_num, self.config, command, params, result_queue)
        )

        try:
            logger.info(f"🚀 Starting worker process for Account {account_num}, command: {command}")
            worker_process.start()

            # Wait for result with longer timeout (especially for close operations during shutdown)
            # Run in executor to avoid blocking async event loop
            loop = asyncio.get_event_loop()
            timeout = 60 if command == 'close_position' else 30
            result = await loop.run_in_executor(
                None,
                lambda: result_queue.get(timeout=timeout)
            )

            # Wait for process to finish naturally
            worker_process.join(timeout=10)

            if worker_process.is_alive():
                logger.warning(f"⚠️ Worker process for Account {account_num} still alive after {timeout}s, terminating")
                worker_process.terminate()
                worker_process.join(timeout=5)

            logger.info(f"✅ Worker process for Account {account_num} completed: {result}")
            return result

        except queue.Empty:
            logger.error(f"❌ Worker process for Account {account_num} timed out after {timeout}s")
            if worker_process.is_alive():
                logger.warning(f"⚠️ Terminating stuck worker process")
                worker_process.terminate()
                worker_process.join(timeout=5)
            return {'error': f'Worker timeout after {timeout}s'}
        except Exception as e:
            logger.error(f"❌ Worker process error for Account {account_num}: {e}")
            if worker_process.is_alive():
                worker_process.terminate()
                worker_process.join(timeout=5)
            return {'error': str(e)}

    async def set_leverage(self, account_num: int, token: str, market_index: int, leverage: int) -> bool:
        """Set leverage for account"""
        result = await self.execute_command(
            account_num,
            'set_leverage',
            {
                'token': token,
                'market_index': market_index,
                'leverage': leverage
            }
        )

        if 'error' in result:
            logger.error(f"Failed to set leverage on Account {account_num}: {result['error']}")
            return False

        return result.get('success', False)

    async def open_position(self, account_num: int, token: str, market_index: int,
                           base_amount: int, is_long: bool, price: int,
                           order_index: int) -> Optional[Dict[str, Any]]:
        """Open position on account"""
        result = await self.execute_command(
            account_num,
            'open_position',
            {
                'token': token,
                'market_index': market_index,
                'base_amount': base_amount,
                'is_long': is_long,
                'price': price,
                'order_index': order_index
            }
        )

        if 'error' in result:
            logger.error(f"Failed to open position on Account {account_num}: {result['error']}")
            return None

        return result

    async def close_position(self, account_num: int, token: str, market_index: int,
                            base_amount: int, is_long: bool, price: int,
                            order_index: int) -> bool:
        """Close position on account"""
        result = await self.execute_command(
            account_num,
            'close_position',
            {
                'token': token,
                'market_index': market_index,
                'base_amount': base_amount,
                'is_long': is_long,
                'price': price,
                'order_index': order_index
            }
        )

        if 'error' in result:
            logger.error(f"Failed to close position on Account {account_num}: {result['error']}")
            return False

        return result.get('success', False)
