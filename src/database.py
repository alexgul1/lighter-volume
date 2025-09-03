import asyncio
from datetime import datetime
from typing import Dict, Any, Optional, List
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING, DESCENDING
import logging

logger = logging.getLogger(__name__)


class Transaction:
    """Transaction model for futures trades"""

    def __init__(self, tx_type: str, position_type: str, token: str,
                 amount_usdc: float, base_amount: int, price: Optional[int] = None,
                 avg_entry_price: Optional[float] = None, tp_price: Optional[float] = None,
                 sl_price: Optional[float] = None, is_success: bool = False,
                 dependency: Optional[int] = None, order_id: Optional[str] = None,
                 tx_hash: Optional[str] = None, error: Optional[str] = None):
        self.date = datetime.utcnow()
        self.type = tx_type  # "open", "close", "tp_order", "sl_order"
        self.position_type = position_type  # "long" or "short"
        self.token = token
        self.amount_usdc = amount_usdc
        self.base_amount = base_amount
        self.price = price
        self.avg_entry_price = avg_entry_price
        self.tp_price = tp_price
        self.sl_price = sl_price
        self.is_success = is_success
        self.dependency = dependency
        self.order_id = order_id
        self.tx_hash = tx_hash
        self.error = error

    def to_dict(self) -> Dict[str, Any]:
        return {
            "date": self.date,
            "type": self.type,
            "position_type": self.position_type,
            "token": self.token,
            "amount_usdc": self.amount_usdc,
            "base_amount": self.base_amount,
            "price": self.price,
            "avg_entry_price": self.avg_entry_price,
            "tp_price": self.tp_price,
            "sl_price": self.sl_price,
            "is_success": self.is_success,
            "dependency": self.dependency,
            "order_id": self.order_id,
            "tx_hash": self.tx_hash,
            "error": self.error
        }


class DatabaseManager:
    """MongoDB database manager"""

    def __init__(self, uri: str, database: str, collection: str):
        self.uri = uri
        self.database_name = database
        self.collection_name = collection
        self.client: Optional[AsyncIOMotorClient] = None
        self.db = None
        self.collection = None
        self._tx_counter = 0
        self._counter_lock = asyncio.Lock()

    async def connect(self):
        """Connect to MongoDB"""
        try:
            self.client = AsyncIOMotorClient(self.uri)
            self.db = self.client[self.database_name]
            self.collection = self.db[self.collection_name]

            # Create indexes
            await self.collection.create_index([("txId", ASCENDING)], unique=True)
            await self.collection.create_index([("date", DESCENDING)])
            await self.collection.create_index([("type", ASCENDING)])
            await self.collection.create_index([("position_type", ASCENDING)])
            await self.collection.create_index([("token", ASCENDING)])

            # Initialize counter
            last_tx = await self.collection.find_one(sort=[("txId", -1)])
            if last_tx:
                self._tx_counter = last_tx.get("txId", 0)

            logger.info(f"Connected to MongoDB. Starting txId: {self._tx_counter + 1}")

        except Exception as e:
            logger.error(f"Failed to connect to MongoDB: {e}")
            raise

    async def disconnect(self):
        """Disconnect from MongoDB"""
        if self.client:
            self.client.close()

    async def get_next_tx_id(self) -> int:
        """Get next transaction ID"""
        async with self._counter_lock:
            self._tx_counter += 1
            return self._tx_counter

    async def log_transaction(self, transaction: Transaction) -> int:
        """Log a transaction to database"""
        tx_id = await self.get_next_tx_id()
        doc = transaction.to_dict()
        doc["txId"] = tx_id

        await self.collection.insert_one(doc)
        return tx_id