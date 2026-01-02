---
url: https://nadohq.github.io/nado-python-sdk/_modules/nado_protocol/indexer_client/types/query.html
---

# Source code for nado_protocol.indexer_client.types.query

```python

from nado_protocol.utils.enum import StrEnum
from typing import Dict, List, Optional, Tuple, Type, Union

from pydantic import Field, validator
from nado_protocol.indexer_client.types.models import (
    IndexerCandlestick,
    IndexerCandlesticksGranularity,
    IndexerEvent,
    IndexerEventType,
    IndexerHistoricalOrder,
    IndexerLiquidatableAccount,
    IndexerMarketMaker,
    IndexerMatch,
    IndexerOraclePrice,
    IndexerPerpContractInfo,
    IndexerProduct,
    IndexerMarketSnapshot,
    IndexerSubaccount,
    IndexerTickerInfo,
    IndexerTokenReward,
    IndexerTradeInfo,
    IndexerTx,
    IndexerMerkleProof,
    IndexerPayment,
)
from nado_protocol.utils.model import NadoBaseModel

[docs]class IndexerQueryType(StrEnum):
    """
    Enumeration of query types available in the Indexer service.
    """

    ORDERS = "orders"
    MATCHES = "matches"
    EVENTS = "events"
    SUMMARY = "summary"
    PRODUCTS = "products"
    MARKET_SNAPSHOTS = "market_snapshots"
    CANDLESTICKS = "candlesticks"
    FUNDING_RATE = "funding_rate"
    FUNDING_RATES = "funding_rates"
    PERP_PRICES = "price"
    ORACLE_PRICES = "oracle_price"
    REWARDS = "rewards"
    MAKER_STATISTICS = "maker_statistics"
    LIQUIDATION_FEED = "liquidation_feed"
    LINKED_SIGNER_RATE_LIMIT = "linked_signer_rate_limit"
    REFERRAL_CODE = "referral_code"
    SUBACCOUNTS = "subaccounts"
    QUOTE_PRICE = "quote_price"
    ACCOUNT_SNAPSHOTS = "account_snapshots"
    INTEREST_AND_FUNDING = "interest_and_funding"
    INK_AIRDROP = "ink_airdrop"

[docs]class IndexerBaseParams(NadoBaseModel):
    """
    Base parameters for the indexer queries.
    """

    idx: Optional[int] = Field(alias="submission_idx")
    max_time: Optional[int]
    limit: Optional[int]

[docs]    class Config:
        allow_population_by_field_name = True

[docs]class IndexerSubaccountHistoricalOrdersParams(IndexerBaseParams):
    """
    Parameters for querying historical orders by subaccounts.
    """

    subaccounts: Optional[list[str]]
    product_ids: Optional[list[int]]
    trigger_types: Optional[list[str]]
    isolated: Optional[bool]

[docs]    class Config:
        # Ensure this doesn't get confused with digest params
        extra = "forbid"

[docs]class IndexerHistoricalOrdersByDigestParams(NadoBaseModel):
    """
    Parameters for querying historical orders by digests.
    """

    digests: list[str]

[docs]    class Config:
        # Ensure this doesn't get confused with subaccount params
        extra = "forbid"

[docs]class IndexerMatchesParams(IndexerBaseParams):
    """
    Parameters for querying matches.
    """

    subaccounts: Optional[list[str]]
    product_ids: Optional[list[int]]
    isolated: Optional[bool]

[docs]class IndexerEventsRawLimit(NadoBaseModel):
    """
    Parameters for limiting by events count.
    """

    raw: int

[docs]class IndexerEventsTxsLimit(NadoBaseModel):
    """
    Parameters for limiting events by transaction count.
    """

    txs: int

IndexerEventsLimit = Union[IndexerEventsRawLimit, IndexerEventsTxsLimit]

[docs]class IndexerEventsParams(IndexerBaseParams):
    """
    Parameters for querying events.
    """

    subaccounts: Optional[list[str]]
    product_ids: Optional[list[int]]
    event_types: Optional[list[IndexerEventType]]
    isolated: Optional[bool]
    limit: Optional[IndexerEventsLimit]  # type: ignore

[docs]class IndexerProductSnapshotsParams(IndexerBaseParams):
    """
    Parameters for querying product snapshots.
    """

    product_id: int

class IndexerMarketSnapshotInterval(NadoBaseModel):
    count: int
    granularity: int
    max_time: Optional[int]

class IndexerMarketSnapshotsParams(NadoBaseModel):
    """
    Parameters for querying market snapshots.
    """

    interval: IndexerMarketSnapshotInterval
    product_ids: Optional[list[int]]

[docs]class IndexerCandlesticksParams(IndexerBaseParams):
    """
    Parameters for querying candlestick data.
    """

    product_id: int
    granularity: IndexerCandlesticksGranularity

[docs]    class Config:
        fields = {"idx": {"exclude": True}}

[docs]class IndexerFundingRateParams(NadoBaseModel):
    """
    Parameters for querying funding rates.
    """

    product_id: int

class IndexerFundingRatesParams(NadoBaseModel):
    """
    Parameters for querying funding rates.
    """

    product_ids: list

[docs]class IndexerPerpPricesParams(NadoBaseModel):
    """
    Parameters for querying perpetual prices.
    """

    product_id: int

[docs]class IndexerOraclePricesParams(NadoBaseModel):
    """
    Parameters for querying oracle prices.
    """

    product_ids: list[int]

[docs]class IndexerLiquidationFeedParams(NadoBaseModel):
    """
    Parameters for querying liquidation feed.
    """

    pass

[docs]class IndexerLinkedSignerRateLimitParams(NadoBaseModel):
    """
    Parameters for querying linked signer rate limits.
    """

    subaccount: str

[docs]class IndexerSubaccountsParams(NadoBaseModel):
    """
    Parameters for querying subaccounts.
    """

    address: Optional[str]
    limit: Optional[int]
    start: Optional[int]

class IndexerQuotePriceParams(NadoBaseModel):
    """
    Parameters for querying quote price.
    """

    pass

[docs]class IndexerInterestAndFundingParams(NadoBaseModel):
    """
    Parameters for querying interest and funding payments.
    """

    subaccount: str
    product_ids: list[int]
    max_idx: Optional[Union[str, int]]
    limit: int

class IndexerAccountSnapshotsParams(NadoBaseModel):
    """
    Parameters for querying account snapshots.
    """

    subaccounts: list[str]
    timestamps: list[int]
    isolated: Optional[bool] = None
    active: Optional[bool] = None

class IndexerInkAirdropParams(NadoBaseModel):
    """
    Parameters for querying Ink airdrop allocation.
    """

    address: str

IndexerParams = Union[
    IndexerSubaccountHistoricalOrdersParams,
    IndexerHistoricalOrdersByDigestParams,
    IndexerMatchesParams,
    IndexerEventsParams,
    IndexerProductSnapshotsParams,
    IndexerCandlesticksParams,
    IndexerFundingRateParams,
    IndexerPerpPricesParams,
    IndexerOraclePricesParams,
    IndexerLiquidationFeedParams,
    IndexerLinkedSignerRateLimitParams,
    IndexerSubaccountsParams,
    IndexerQuotePriceParams,
    IndexerMarketSnapshotsParams,
    IndexerInterestAndFundingParams,
    IndexerAccountSnapshotsParams,
    IndexerInkAirdropParams,
]

[docs]class IndexerHistoricalOrdersRequest(NadoBaseModel):
    """
    Request object for querying historical orders.
    """

    orders: Union[
        IndexerSubaccountHistoricalOrdersParams, IndexerHistoricalOrdersByDigestParams
    ]

[docs]    class Config:
        smart_union = True

[docs]class IndexerMatchesRequest(NadoBaseModel):
    """
    Request object for querying matches.
    """

    matches: IndexerMatchesParams

[docs]class IndexerEventsRequest(NadoBaseModel):
    """
    Request object for querying events.
    """

    events: IndexerEventsParams

[docs]class IndexerProductSnapshotsRequest(NadoBaseModel):
    """
    Request object for querying product snapshots.
    """

    products: IndexerProductSnapshotsParams

class IndexerMarketSnapshotsRequest(NadoBaseModel):
    """
    Request object for querying market snapshots.
    """

    market_snapshots: IndexerMarketSnapshotsParams

[docs]class IndexerCandlesticksRequest(NadoBaseModel):
    """
    Request object for querying candlestick data.
    """

    candlesticks: IndexerCandlesticksParams

[docs]class IndexerFundingRateRequest(NadoBaseModel):
    """
    Request object for querying funding rates.
    """

    funding_rate: IndexerFundingRateParams

[docs]class IndexerFundingRatesRequest(NadoBaseModel):
    """
    Request object for querying funding rates.
    """

    funding_rates: IndexerFundingRatesParams

[docs]class IndexerPerpPricesRequest(NadoBaseModel):
    """
    Request object for querying perpetual prices.
    """

    price: IndexerPerpPricesParams

[docs]class IndexerOraclePricesRequest(NadoBaseModel):
    """
    Request object for querying oracle prices.
    """

    oracle_price: IndexerOraclePricesParams

[docs]class IndexerLiquidationFeedRequest(NadoBaseModel):
    """
    Request object for querying liquidation feed.
    """

    liquidation_feed: IndexerLiquidationFeedParams

[docs]class IndexerLinkedSignerRateLimitRequest(NadoBaseModel):
    """
    Request object for querying linked signer rate limits.
    """

    linked_signer_rate_limit: IndexerLinkedSignerRateLimitParams

[docs]class IndexerSubaccountsRequest(NadoBaseModel):
    """
    Request object for querying subaccounts.
    """

    subaccounts: IndexerSubaccountsParams

class IndexerQuotePriceRequest(NadoBaseModel):
    """
    Request object for querying quote price.
    """

    quote_price: IndexerQuotePriceParams

[docs]class IndexerInterestAndFundingRequest(NadoBaseModel):
    """
    Request object for querying Interest and funding payments.
    """

    interest_and_funding: IndexerInterestAndFundingParams

class IndexerAccountSnapshotsRequest(NadoBaseModel):
    """
    Request object for querying account snapshots.
    """

    account_snapshots: IndexerAccountSnapshotsParams

class IndexerInkAirdropRequest(NadoBaseModel):
    """
    Request object for querying Ink airdrop allocation.
    """

    ink_airdrop: IndexerInkAirdropParams

IndexerRequest = Union[
    IndexerHistoricalOrdersRequest,
    IndexerMatchesRequest,
    IndexerEventsRequest,
    IndexerProductSnapshotsRequest,
    IndexerCandlesticksRequest,
    IndexerFundingRateRequest,
    IndexerPerpPricesRequest,
    IndexerOraclePricesRequest,
    IndexerLiquidationFeedRequest,
    IndexerLinkedSignerRateLimitRequest,
    IndexerSubaccountsRequest,
    IndexerQuotePriceRequest,
    IndexerMarketSnapshotsRequest,
    IndexerInterestAndFundingRequest,
    IndexerAccountSnapshotsRequest,
    IndexerInkAirdropRequest,
]

[docs]class IndexerHistoricalOrdersData(NadoBaseModel):
    """
    Data object for historical orders.
    """

    orders: list[IndexerHistoricalOrder]

[docs]class IndexerMatchesData(NadoBaseModel):
    """
    Data object for matches.
    """

    matches: list[IndexerMatch]
    txs: list[IndexerTx]

[docs]class IndexerEventsData(NadoBaseModel):
    """
    Data object for events.
    """

    events: list[IndexerEvent]
    txs: list[IndexerTx]

[docs]class IndexerProductSnapshotsData(NadoBaseModel):
    """
    Data object for product snapshots.
    """

    products: list[IndexerProduct]
    txs: list[IndexerTx]

class IndexerMarketSnapshotsData(NadoBaseModel):
    """
    Data object for market snapshots.
    """

    snapshots: list[IndexerMarketSnapshot]

[docs]class IndexerCandlesticksData(NadoBaseModel):
    """
    Data object for candlestick data.
    """

    candlesticks: list[IndexerCandlestick]

[docs]class IndexerFundingRateData(NadoBaseModel):
    """
    Data object for funding rates.
    """

    product_id: int
    funding_rate_x18: str
    update_time: str

IndexerFundingRatesData = Dict[str, IndexerFundingRateData]

[docs]class IndexerPerpPricesData(NadoBaseModel):
    """
    Data object for perpetual prices.
    """

    product_id: int
    index_price_x18: str
    mark_price_x18: str
    update_time: str

[docs]class IndexerOraclePricesData(NadoBaseModel):
    """
    Data object for oracle prices.
    """

    prices: list[IndexerOraclePrice]

[docs]class IndexerLinkedSignerRateLimitData(NadoBaseModel):
    """
    Data object for linked signer rate limits.
    """

    remaining_tx: str
    total_tx_limit: str
    wait_time: int
    signer: str

[docs]class IndexerSubaccountsData(NadoBaseModel):
    """
    Data object for subaccounts response from the indexer.
    """

    subaccounts: list[IndexerSubaccount]

[docs]class IndexerQuotePriceData(NadoBaseModel):
    """
    Data object for the quote price response from the indexer.
    """

    price_x18: str

[docs]class IndexerInterestAndFundingData(NadoBaseModel):
    """
    Data object for the interest and funding payments response from the indexer.
    """

    interest_payments: list[IndexerPayment]
    funding_payments: list[IndexerPayment]
    next_idx: str

IndexerLiquidationFeedData = list[IndexerLiquidatableAccount]

class IndexerAccountSnapshotsData(NadoBaseModel):
    """
    Data object for subaccount snapshots grouped by subaccount and timestamp.
    """

    snapshots: Dict[str, Dict[str, list[IndexerEvent]]]

class IndexerInkAirdropData(NadoBaseModel):
    """
    Data object for Ink airdrop allocation.
    """

    amount: str

IndexerResponseData = Union[
    IndexerHistoricalOrdersData,
    IndexerMatchesData,
    IndexerEventsData,
    IndexerProductSnapshotsData,
    IndexerCandlesticksData,
    IndexerFundingRateData,
    IndexerPerpPricesData,
    IndexerOraclePricesData,
    IndexerLinkedSignerRateLimitData,
    IndexerSubaccountsData,
    IndexerQuotePriceData,
    IndexerMarketSnapshotsData,
    IndexerInterestAndFundingData,
    IndexerLiquidationFeedData,
    IndexerFundingRatesData,
    IndexerAccountSnapshotsData,
    IndexerInkAirdropData,
]

[docs]class IndexerResponse(NadoBaseModel):
    """
    Represents the response returned by the indexer.

    Attributes:
        data (IndexerResponseData): The data contained in the response.
    """

    data: IndexerResponseData

def to_indexer_request(params: IndexerParams) -> IndexerRequest:
    """
    Converts an IndexerParams object to the corresponding IndexerRequest object.

    Args:
        params (IndexerParams): The IndexerParams object to convert.

    Returns:
        IndexerRequest: The converted IndexerRequest object.
    """
    indexer_request_mapping = {
        IndexerSubaccountHistoricalOrdersParams: (
            IndexerHistoricalOrdersRequest,
            IndexerQueryType.ORDERS.value,
        ),
        IndexerHistoricalOrdersByDigestParams: (
            IndexerHistoricalOrdersRequest,
            IndexerQueryType.ORDERS.value,
        ),
        IndexerMatchesParams: (IndexerMatchesRequest, IndexerQueryType.MATCHES.value),
        IndexerEventsParams: (IndexerEventsRequest, IndexerQueryType.EVENTS.value),
        IndexerProductSnapshotsParams: (
            IndexerProductSnapshotsRequest,
            IndexerQueryType.PRODUCTS.value,
        ),
        IndexerMarketSnapshotsParams: (
            IndexerMarketSnapshotsRequest,
            IndexerQueryType.MARKET_SNAPSHOTS.value,
        ),
        IndexerCandlesticksParams: (
            IndexerCandlesticksRequest,
            IndexerQueryType.CANDLESTICKS.value,
        ),
        IndexerFundingRateParams: (
            IndexerFundingRateRequest,
            IndexerQueryType.FUNDING_RATE.value,
        ),
        IndexerFundingRatesParams: (
            IndexerFundingRatesRequest,
            IndexerQueryType.FUNDING_RATES.value,
        ),
        IndexerPerpPricesParams: (
            IndexerPerpPricesRequest,
            IndexerQueryType.PERP_PRICES.value,
        ),
        IndexerOraclePricesParams: (
            IndexerOraclePricesRequest,
            IndexerQueryType.ORACLE_PRICES.value,
        ),
        IndexerLiquidationFeedParams: (
            IndexerLiquidationFeedRequest,
            IndexerQueryType.LIQUIDATION_FEED.value,
        ),
        IndexerLinkedSignerRateLimitParams: (
            IndexerLinkedSignerRateLimitRequest,
            IndexerQueryType.LINKED_SIGNER_RATE_LIMIT.value,
        ),
        IndexerSubaccountsParams: (
            IndexerSubaccountsRequest,
            IndexerQueryType.SUBACCOUNTS.value,
        ),
        IndexerQuotePriceParams: (
            IndexerQuotePriceRequest,
            IndexerQueryType.QUOTE_PRICE.value,
        ),
        IndexerInterestAndFundingParams: (
            IndexerInterestAndFundingRequest,
            IndexerQueryType.INTEREST_AND_FUNDING.value,
        ),
        IndexerAccountSnapshotsParams: (
            IndexerAccountSnapshotsRequest,
            IndexerQueryType.ACCOUNT_SNAPSHOTS.value,
        ),
        IndexerInkAirdropParams: (
            IndexerInkAirdropRequest,
            IndexerQueryType.INK_AIRDROP.value,
        ),
    }

    RequestClass, field_name = indexer_request_mapping[type(params)]
    return RequestClass.parse_obj({field_name: params.dict(exclude_none=False)})  # type: ignore[attr-defined]

IndexerTickersData = Dict[str, IndexerTickerInfo]

IndexerPerpContractsData = Dict[str, IndexerPerpContractInfo]

IndexerHistoricalTradesData = List[IndexerTradeInfo]

```