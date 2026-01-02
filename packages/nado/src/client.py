"""
Nado.xyz API Client with EIP-712 Signing

Handles all API communication and cryptographic signing for Nado DEX.
"""
import time
import random
import logging
from typing import Optional, Dict, Any, List, Tuple
from dataclasses import dataclass

import httpx
from eth_account import Account
from eth_account.messages import encode_typed_data

from src.config import Config

logger = logging.getLogger(__name__)


@dataclass
class MarketPrice:
    """Market price data"""
    product_id: int
    bid: int  # x18 format
    ask: int  # x18 format

    @property
    def bid_float(self) -> float:
        return self.bid / 1e18

    @property
    def ask_float(self) -> float:
        return self.ask / 1e18

    @property
    def mid_price(self) -> float:
        return (self.bid + self.ask) / 2 / 1e18


@dataclass
class SubaccountInfo:
    """Subaccount balance and health info"""
    exists: bool
    spot_balances: Dict[int, int]  # product_id -> amount (x18)
    perp_balances: Dict[int, Dict[str, int]]  # product_id -> {amount, v_quote_balance}
    health_initial: int  # x18
    health_maintenance: int  # x18


class OrderAppendix:
    """
    Order appendix builder following Nado's bit layout.

    Bit layout (128-bit integer):
    | value   | reserved | trigger | reduce_only | order_type | isolated | version |
    | 64 bits | 50 bits  | 2 bits  | 1 bit       | 2 bits     | 1 bit    | 8 bits  |
    | 127..64 | 63..14   | 13..12  | 11          | 10..9      | 8        | 7..0    |
    """

    # Order types
    ORDER_TYPE_DEFAULT = 0  # Standard limit order
    ORDER_TYPE_IOC = 1      # Immediate or Cancel
    ORDER_TYPE_FOK = 2      # Fill or Kill
    ORDER_TYPE_POST_ONLY = 3

    # Trigger types
    TRIGGER_NONE = 0
    TRIGGER_PRICE = 1
    TRIGGER_TWAP = 2
    TRIGGER_TWAP_CUSTOM = 3

    @staticmethod
    def build(
        version: int = 1,
        isolated: bool = False,
        order_type: int = 1,  # IOC by default for fast trades
        reduce_only: bool = False,
        trigger: int = 0,
        value: int = 0
    ) -> str:
        """Build order appendix as string (for JSON payload)"""
        appendix = version & 0xFF  # 8 bits
        appendix |= (1 if isolated else 0) << 8  # 1 bit
        appendix |= (order_type & 0x3) << 9  # 2 bits
        appendix |= (1 if reduce_only else 0) << 11  # 1 bit
        appendix |= (trigger & 0x3) << 12  # 2 bits
        # reserved bits 14-63 = 0
        appendix |= (value & 0xFFFFFFFFFFFFFFFF) << 64  # 64 bits

        return str(appendix)

    @staticmethod
    def build_ioc(reduce_only: bool = False) -> str:
        """Build IOC order appendix (best for fast trading)"""
        return OrderAppendix.build(
            version=1,
            order_type=OrderAppendix.ORDER_TYPE_IOC,
            reduce_only=reduce_only
        )

    @staticmethod
    def build_fok(reduce_only: bool = False) -> str:
        """Build FOK order appendix"""
        return OrderAppendix.build(
            version=1,
            order_type=OrderAppendix.ORDER_TYPE_FOK,
            reduce_only=reduce_only
        )


class NadoClient:
    """
    Nado.xyz API client with EIP-712 signing.

    Handles:
    - EIP-712 message signing
    - Order placement and cancellation
    - Market data queries
    - Subaccount management
    """

    # EIP-712 Type definitions
    ORDER_TYPES = {
        "Order": [
            {"name": "sender", "type": "bytes32"},
            {"name": "priceX18", "type": "int128"},
            {"name": "amount", "type": "int128"},
            {"name": "expiration", "type": "uint64"},
            {"name": "nonce", "type": "uint64"},
            {"name": "appendix", "type": "uint128"},
        ]
    }

    CANCELLATION_TYPES = {
        "Cancellation": [
            {"name": "sender", "type": "bytes32"},
            {"name": "productIds", "type": "uint64[]"},
            {"name": "digests", "type": "bytes32[]"},
            {"name": "nonce", "type": "uint64"},
        ]
    }

    def __init__(self):
        self.base_url = Config.get_gateway_rest()
        self.chain_id = Config.get_chain_id()
        self.endpoint_address = Config.get_endpoint_address()

        # Load account from private key
        self.account = Account.from_key(Config.PRIVATE_KEY)
        self.address = self.account.address

        # Build sender bytes32 (address + subaccount name)
        self.sender = self._build_sender(self.address, Config.SUBACCOUNT_NAME)

        # HTTP client
        self.http = httpx.AsyncClient(timeout=30.0)

        # Nonce tracking
        self._tx_nonce: Optional[int] = None

        logger.info(f"NadoClient initialized")
        logger.info(f"  Network: {Config.NETWORK}")
        logger.info(f"  Address: {self.address}")
        logger.info(f"  Subaccount: {Config.SUBACCOUNT_NAME}")
        logger.info(f"  Sender: {self.sender}")

    def _build_sender(self, address: str, subaccount_name: str) -> str:
        """
        Build sender bytes32: address (20 bytes) + subaccount name (12 bytes).
        """
        # Remove 0x prefix and ensure lowercase
        addr_hex = address.lower().replace("0x", "")

        # Encode subaccount name to bytes and pad to 12 bytes
        name_bytes = subaccount_name.encode('utf-8')
        name_hex = name_bytes.hex().ljust(24, '0')  # 12 bytes = 24 hex chars

        return "0x" + addr_hex + name_hex

    def _get_order_verifying_contract(self, product_id: int) -> str:
        """
        Get verifyingContract for order signing.
        For orders: verifyingContract = address(productId)
        """
        # Convert product_id to 20-byte address (40 hex chars)
        return "0x" + hex(product_id)[2:].zfill(40)

    def _get_eip712_domain(self, verifying_contract: str) -> Dict:
        """Build EIP-712 domain for signing"""
        return {
            "name": Config.EIP712_DOMAIN_NAME,
            "version": Config.EIP712_DOMAIN_VERSION,
            "chainId": self.chain_id,
            "verifyingContract": verifying_contract,
        }

    def _generate_nonce(self, offset_ms: int = None) -> int:
        """
        Generate order nonce.
        Format: (timestamp_ms + offset) << 20 | random_20_bits
        """
        if offset_ms is None:
            offset_ms = Config.NONCE_RECV_TIME_OFFSET_MS

        timestamp_ms = int(time.time() * 1000) + offset_ms
        random_bits = random.getrandbits(20)
        return (timestamp_ms << 20) | random_bits

    def _sign_typed_data(
        self,
        domain: Dict,
        types: Dict,
        primary_type: str,
        message: Dict
    ) -> str:
        """Sign EIP-712 typed data and return signature"""
        # Build full typed data structure
        typed_data = {
            "types": {
                "EIP712Domain": [
                    {"name": "name", "type": "string"},
                    {"name": "version", "type": "string"},
                    {"name": "chainId", "type": "uint256"},
                    {"name": "verifyingContract", "type": "address"},
                ],
                **types
            },
            "primaryType": primary_type,
            "domain": domain,
            "message": message,
        }

        # Sign using eth_account
        signable = encode_typed_data(full_message=typed_data)
        signed = self.account.sign_message(signable)

        return signed.signature.hex()

    async def _query(self, params: Dict) -> Dict:
        """Execute a query request"""
        try:
            response = await self.http.post(
                f"{self.base_url}/query",
                json=params
            )
            response.raise_for_status()
            data = response.json()

            if data.get("status") != "success":
                raise Exception(f"Query failed: {data}")

            return data.get("data", data)

        except httpx.HTTPError as e:
            logger.error(f"Query HTTP error: {e}")
            raise

    async def _execute(self, payload: Dict) -> Dict:
        """Execute a signed request"""
        try:
            response = await self.http.post(
                f"{self.base_url}/execute",
                json=payload
            )
            response.raise_for_status()
            data = response.json()

            if data.get("status") != "success":
                error_code = data.get("error_code")
                error_msg = data.get("error", data.get("message", str(data)))
                raise Exception(f"Execute failed [{error_code}]: {error_msg}")

            return data

        except httpx.HTTPError as e:
            logger.error(f"Execute HTTP error: {e}")
            raise

    # ==================== Query Methods ====================

    async def get_contracts(self) -> Dict:
        """Get chain_id and endpoint_addr"""
        return await self._query({"type": "contracts"})

    async def get_all_products(self) -> List[Dict]:
        """Get all available products"""
        data = await self._query({"type": "all_products"})
        return data.get("products", [])

    async def get_market_price(self, product_id: int) -> MarketPrice:
        """Get bid/ask for a product"""
        data = await self._query({
            "type": "market_price",
            "product_id": product_id
        })
        return MarketPrice(
            product_id=product_id,
            bid=int(data.get("bid", 0)),
            ask=int(data.get("ask", 0))
        )

    async def get_market_prices(self, product_ids: List[int]) -> List[MarketPrice]:
        """Get bid/ask for multiple products"""
        data = await self._query({
            "type": "market_prices",
            "product_ids": product_ids
        })
        prices = []
        for item in data.get("prices", []):
            prices.append(MarketPrice(
                product_id=item.get("product_id"),
                bid=int(item.get("bid", 0)),
                ask=int(item.get("ask", 0))
            ))
        return prices

    async def get_subaccount_info(self, subaccount: str = None) -> SubaccountInfo:
        """Get subaccount balances and health"""
        if subaccount is None:
            subaccount = self.sender

        data = await self._query({
            "type": "subaccount_info",
            "subaccount": subaccount
        })

        # Parse balances
        spot_balances = {}
        for product_id, amount in data.get("spot_balances", {}).items():
            spot_balances[int(product_id)] = int(amount)

        perp_balances = {}
        for product_id, info in data.get("perp_balances", {}).items():
            perp_balances[int(product_id)] = {
                "amount": int(info.get("amount", 0)),
                "v_quote_balance": int(info.get("v_quote_balance", 0))
            }

        # Parse health
        healths = data.get("healths", [])
        health_initial = int(healths[0].get("health", 0)) if len(healths) > 0 else 0
        health_maintenance = int(healths[1].get("health", 0)) if len(healths) > 1 else 0

        return SubaccountInfo(
            exists=data.get("exists", False),
            spot_balances=spot_balances,
            perp_balances=perp_balances,
            health_initial=health_initial,
            health_maintenance=health_maintenance
        )

    async def get_nonces(self) -> Tuple[int, int]:
        """Get current nonces (order_nonce, tx_nonce)"""
        data = await self._query({
            "type": "nonces",
            "address": self.address
        })
        return (
            int(data.get("order_nonce", 0)),
            int(data.get("tx_nonce", 0))
        )

    async def get_tx_nonce(self) -> int:
        """Get and cache tx_nonce for cancel operations"""
        if self._tx_nonce is None:
            _, self._tx_nonce = await self.get_nonces()
        return self._tx_nonce

    def increment_tx_nonce(self):
        """Increment cached tx_nonce after successful execute"""
        if self._tx_nonce is not None:
            self._tx_nonce += 1

    # ==================== Execute Methods ====================

    async def place_order(
        self,
        product_id: int,
        price: float,
        amount: float,
        is_buy: bool,
        order_type: int = OrderAppendix.ORDER_TYPE_IOC,
        reduce_only: bool = False,
        client_id: int = None
    ) -> Dict:
        """
        Place a single order.

        Args:
            product_id: Product to trade (2=ETH, 4=BTC, etc)
            price: Order price in USD
            amount: Order size in base asset units
            is_buy: True for buy, False for sell
            order_type: Order type (IOC, FOK, DEFAULT, POST_ONLY)
            reduce_only: Only reduce position
            client_id: Optional client ID for tracking

        Returns:
            Order result with digest
        """
        # Convert to x18 format
        price_x18 = int(price * 1e18)
        amount_x18 = int(amount * 1e18)

        # Negative amount for sell
        if not is_buy:
            amount_x18 = -amount_x18

        # Build order
        expiration = int(time.time()) + Config.ORDER_EXPIRATION_SECONDS
        nonce = self._generate_nonce()
        appendix = OrderAppendix.build(
            version=1,
            order_type=order_type,
            reduce_only=reduce_only
        )

        order = {
            "sender": self.sender,
            "priceX18": str(price_x18),
            "amount": str(amount_x18),
            "expiration": str(expiration),
            "nonce": str(nonce),
            "appendix": appendix
        }

        # Sign order
        verifying_contract = self._get_order_verifying_contract(product_id)
        domain = self._get_eip712_domain(verifying_contract)

        # Message for signing (use int values, not strings)
        sign_message = {
            "sender": bytes.fromhex(self.sender[2:]),
            "priceX18": price_x18,
            "amount": amount_x18,
            "expiration": expiration,
            "nonce": nonce,
            "appendix": int(appendix),
        }

        signature = self._sign_typed_data(
            domain=domain,
            types=self.ORDER_TYPES,
            primary_type="Order",
            message=sign_message
        )

        # Build request
        request = {
            "place_order": {
                "product_id": product_id,
                "order": order,
                "signature": "0x" + signature if not signature.startswith("0x") else signature,
                "spot_leverage": Config.USE_SPOT_LEVERAGE
            }
        }

        if client_id is not None:
            request["place_order"]["id"] = client_id

        logger.debug(f"Placing order: product={product_id}, price={price}, amount={amount}, is_buy={is_buy}")

        result = await self._execute(request)
        return result

    async def place_market_order(
        self,
        product_id: int,
        amount_usd: float,
        is_buy: bool,
        reduce_only: bool = False
    ) -> Dict:
        """
        Place a market order (IOC at extreme price).

        Args:
            product_id: Product to trade
            amount_usd: Trade size in USD
            is_buy: True for buy, False for sell
            reduce_only: Only reduce position
        """
        # Get current market price
        market = await self.get_market_price(product_id)

        if is_buy:
            # Buy at high price (will match with asks)
            price = market.ask_float * 1.05  # 5% above ask
            amount = amount_usd / market.ask_float
        else:
            # Sell at low price (will match with bids)
            price = market.bid_float * 0.95  # 5% below bid
            amount = amount_usd / market.bid_float

        return await self.place_order(
            product_id=product_id,
            price=price,
            amount=amount,
            is_buy=is_buy,
            order_type=OrderAppendix.ORDER_TYPE_IOC,
            reduce_only=reduce_only
        )

    async def cancel_orders(
        self,
        product_ids: List[int],
        digests: List[str]
    ) -> Dict:
        """
        Cancel specific orders by digest.

        Args:
            product_ids: List of product IDs
            digests: List of order digests (same length as product_ids)
        """
        if len(product_ids) != len(digests):
            raise ValueError("product_ids and digests must have same length")

        tx_nonce = await self.get_tx_nonce()
        nonce = self._generate_nonce()

        tx = {
            "sender": self.sender,
            "productIds": product_ids,
            "digests": digests,
            "nonce": str(nonce)
        }

        # Sign cancellation
        domain = self._get_eip712_domain(self.endpoint_address)

        sign_message = {
            "sender": bytes.fromhex(self.sender[2:]),
            "productIds": product_ids,
            "digests": [bytes.fromhex(d[2:] if d.startswith("0x") else d) for d in digests],
            "nonce": nonce,
        }

        signature = self._sign_typed_data(
            domain=domain,
            types=self.CANCELLATION_TYPES,
            primary_type="Cancellation",
            message=sign_message
        )

        request = {
            "cancel_orders": {
                "tx": tx,
                "signature": "0x" + signature if not signature.startswith("0x") else signature
            }
        }

        result = await self._execute(request)
        self.increment_tx_nonce()
        return result

    async def close(self):
        """Close HTTP client"""
        await self.http.aclose()


def to_x18(value: float) -> int:
    """Convert float to x18 integer format"""
    return int(value * 1e18)


def from_x18(value: int) -> float:
    """Convert x18 integer to float"""
    return value / 1e18
