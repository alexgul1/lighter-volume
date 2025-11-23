"""
Account Worker - Isolated process for each SignerClient

This module provides isolated workers for each account to avoid
global singleton conflicts in lighter-sdk 0.1.4+
"""

import asyncio
import logging
from typing import Dict, Any, Optional
import lighter
from src.config import Config

logger = logging.getLogger(__name__)


class AccountWorker:
    """Worker that runs in isolated process for single account"""

    def __init__(self, account_num: int, config: Dict[str, Any]):
        self.account_num = account_num
        self.config = config
        self.client = None
        self.transaction_api = None

    async def initialize(self):
        """Initialize SignerClient in this isolated process"""
        try:
            # Get account-specific config
            if self.account_num == 1:
                private_key = self.config['ACCOUNT_1_PRIVATE_KEY']
                account_index = self.config['ACCOUNT_1_INDEX']
                api_key_index = self.config['ACCOUNT_1_API_KEY_INDEX']
            else:
                private_key = self.config['ACCOUNT_2_PRIVATE_KEY']
                account_index = self.config['ACCOUNT_2_INDEX']
                api_key_index = self.config['ACCOUNT_2_API_KEY_INDEX']

            logger.info(f"🔧 Initializing Account {self.account_num} worker (index={account_index}, api_key={api_key_index})")

            # Create isolated SignerClient
            self.client = lighter.SignerClient(
                url=self.config['BASE_URL'],
                private_key=private_key,
                account_index=account_index,
                api_key_index=api_key_index
            )

            # Create transaction API
            configuration = lighter.Configuration(self.config['BASE_URL'])
            api_client = lighter.ApiClient(configuration)
            self.transaction_api = lighter.TransactionApi(api_client)

            logger.info(f"✅ Account {self.account_num} worker initialized")
            return True

        except Exception as e:
            logger.error(f"❌ Failed to initialize Account {self.account_num} worker: {e}")
            return False

    async def get_nonce(self) -> int:
        """Get fresh nonce from API"""
        try:
            if self.account_num == 1:
                account_index = self.config['ACCOUNT_1_INDEX']
                api_key_index = self.config['ACCOUNT_1_API_KEY_INDEX']
            else:
                account_index = self.config['ACCOUNT_2_INDEX']
                api_key_index = self.config['ACCOUNT_2_API_KEY_INDEX']

            next_nonce = await self.transaction_api.next_nonce(
                account_index=account_index,
                api_key_index=api_key_index
            )
            return next_nonce.nonce
        except Exception as e:
            logger.error(f"Failed to get nonce for Account {self.account_num}: {e}")
            raise

    async def set_leverage(self, token: str, market_index: int, leverage: int) -> bool:
        """Set leverage for market"""
        try:
            imf = int(10000 / leverage)
            nonce = await self.get_nonce()

            logger.info(f"📝 Setting leverage {leverage}x for {token} on Account {self.account_num} with nonce={nonce}")

            tx_info, error = self.client.sign_update_leverage(
                market_index=market_index,
                fraction=imf,
                margin_mode=self.client.CROSS_MARGIN_MODE,
                nonce=nonce
            )

            if error:
                logger.error(f"Failed to sign leverage update: {error}")
                return False

            await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_UPDATE_LEVERAGE,
                tx_info=tx_info
            )

            logger.info(f"✅ Set leverage {leverage}x for {token} on Account {self.account_num}")
            return True

        except Exception as e:
            logger.error(f"Failed to set leverage on Account {self.account_num}: {e}")
            return False

    async def open_position(self, token: str, market_index: int, base_amount: int,
                           is_long: bool, price: int, order_index: int) -> Optional[Dict[str, Any]]:
        """Open position"""
        try:
            nonce = await self.get_nonce()
            is_ask = not is_long  # Reverse for the actual order

            logger.info(f"📈 Opening {'LONG' if is_long else 'SHORT'} {token} on Account {self.account_num}")

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
                logger.error(f"Failed to sign order: {error}")
                return None

            result = await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            logger.info(f"✅ Opened position on Account {self.account_num}")

            return {
                'success': True,
                'order_index': order_index,
                'result': str(result)
            }

        except Exception as e:
            logger.error(f"Failed to open position on Account {self.account_num}: {e}")
            return None

    async def close_position(self, token: str, market_index: int, base_amount: int,
                            is_long: bool, price: int, order_index: int) -> bool:
        """Close position"""
        try:
            nonce = await self.get_nonce()
            is_ask = is_long  # Reverse for closing

            logger.info(f"📉 Closing {'LONG' if is_long else 'SHORT'} {token} on Account {self.account_num}")

            tx_info, error = self.client.sign_create_order(
                market_index=market_index,
                client_order_index=order_index,
                base_amount=base_amount,
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
                return False

            await self.transaction_api.send_tx(
                tx_type=self.client.TX_TYPE_CREATE_ORDER,
                tx_info=tx_info
            )

            logger.info(f"✅ Closed position on Account {self.account_num}")
            return True

        except Exception as e:
            logger.error(f"Failed to close position on Account {self.account_num}: {e}")
            return False

    async def cleanup(self):
        """Cleanup resources before worker terminates"""
        try:
            # Close aiohttp sessions to prevent unclosed client session warnings
            if self.transaction_api and hasattr(self.transaction_api, 'api_client'):
                api_client = self.transaction_api.api_client
                if hasattr(api_client, 'rest_client') and hasattr(api_client.rest_client, 'pool_manager'):
                    # Close the connection pool
                    if hasattr(api_client.rest_client.pool_manager, 'close'):
                        await api_client.rest_client.pool_manager.close()

            logger.debug(f"🧹 Cleaned up resources for Account {self.account_num} worker")
        except Exception as e:
            logger.warning(f"Error during cleanup for Account {self.account_num}: {e}")


async def run_worker_command(account_num: int, config: Dict[str, Any],
                             command: str, params: Dict[str, Any]) -> Any:
    """
    Run a command in isolated worker process

    This function is the entry point that runs in a separate process
    """
    # Setup logging in worker process
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    worker = AccountWorker(account_num, config)

    # Initialize worker
    if not await worker.initialize():
        return {'error': 'Failed to initialize worker'}

    # Execute command with cleanup
    try:
        if command == 'set_leverage':
            result = await worker.set_leverage(
                params['token'],
                params['market_index'],
                params['leverage']
            )
            return {'success': result}

        elif command == 'open_position':
            result = await worker.open_position(
                params['token'],
                params['market_index'],
                params['base_amount'],
                params['is_long'],
                params['price'],
                params['order_index']
            )
            return result

        elif command == 'close_position':
            result = await worker.close_position(
                params['token'],
                params['market_index'],
                params['base_amount'],
                params['is_long'],
                params['price'],
                params['order_index']
            )
            return {'success': result}

        else:
            return {'error': f'Unknown command: {command}'}

    except Exception as e:
        logger.error(f"Error executing command {command}: {e}")
        return {'error': str(e)}

    finally:
        # Always cleanup resources before process terminates
        await worker.cleanup()


def worker_main(account_num: int, config: Dict[str, Any],
                command: str, params: Dict[str, Any], result_queue) -> None:
    """
    Worker process main function
    Runs in isolated process with its own global singleton
    """
    import signal

    # Ignore SIGINT in worker process - let it complete naturally
    signal.signal(signal.SIGINT, signal.SIG_IGN)

    try:
        # Run async command
        result = asyncio.run(run_worker_command(account_num, config, command, params))
        result_queue.put(result)
    except Exception as e:
        logger.error(f"Worker process exception: {e}")
        result_queue.put({'error': str(e)})
