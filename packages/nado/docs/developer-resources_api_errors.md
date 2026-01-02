---
url: https://docs.nado.xyz/developer-resources/api/errors
title: Errors
---

- Developer Resources
[Developer Resources](/developer-resources)
- 📡API
[📡API](/developer-resources/api)

# Errors

Nado API errors.

List of possibleerrorvalues in the API Response:

`error`

### General

1000/1015

RateLimit

Too Many Requests: You have exceeded the rate limit. Please reduce your request frequency and try again later.

1001

BlacklistedAddress

This address has been blacklisted from accessing the sequencer due to a violation of the Terms of Service. If you believe this is an error, please reach out for assistance.

1002

BlockedLocation

Access from your current location ({location}) is blocked. Please check your location and try again.

1003

BlockedSubdivision

Access from your current location ({location} - {subdivision}) is blocked. Please check your location and try again.

1004

Maintenance

Service is temporarily unavailable due to scheduled maintenance. Please try again later.

### Execute / Query API

```
{
    "status": "failure",
    "signature": {signature},
    "error": "{error msg}",
    "error_code": {error_code}
}
```

```
{
    "status": "failure",
    "error": "{error msg}",
    "error_code": {error_code}
}
```

2000

InvalidPriceIncrement

Invalid order price: Order price, {order.price}, is not divisible by the price_increment_x18; price_increment_x18 for product {product_id}: {price_increment_x18}.

2001

InvalidAmountIncrement

Invalid order amount: Order amount, {order.amount}, must be divisible by the size_increment; size_increment for product {product_id}: {size_increment}.

2002

ZeroAmount

Invalid order amount: The provided amount is zero. Please specify a valid order amount.

2003

OrderAmountTooSmall

Invalid order amount: Order amount, {order.amount}, is too small. abs(amount) must be >= min_size; min_size for product {product_id}: {min_size}.

2004

OrderExpired

Invalid order expiration: The order has already expired. Please ensure the expiration date is in the future.

2005

MaxOrdersLimitReached

You have reached the maximum number of open orders allowed for this market.

2006

UnhealthyOrder

Insufficient account health. The execution of this order would lower your account health below the required threshold. Please adjust your order size or manage your positions to maintain a healthy account balance.

2007

OraclePriceDifference

Order price must be no less than 20% and no more than 500% of the determined oracle price.

2008

PostOnlyOrderCrossesBook

The order cannot be placed as it is post-only and crosses the book. Please adjust your order parameters.

2009

OrderTypeNotSupported

The order type you are trying to use is not currently supported.

2010

InvalidTaker

Invalid taker: The order placement health checks were successfully passed; however, the health checks failed upon matching.

2011

LateRecvExecution

Execute request received after ‘recv_time’. Ensure that your ‘recv_time’ allows adequate time for requests to be received.

2012

EarlyRevcExecution

Execute request received more than 100 seconds before the 'recv_time'. Ensure that the request is sent no more than 100 seconds prior to the 'recv_time'.

2013

DigestAlreadyExists

The provided digest already exists. Ensure that the provided digest is unique.

2014

UnauthorizedSubaccountCancellation

Operation failed. You're attempting to cancel an order for a different subaccount. Please verify the subaccount.

2015

MarketNotFound

The market for the given product or ticker ID was not found. Please try again with a different product or ticker ID.

2016

InvalidProductId

The provided 'product_id' is invalid. Please verify and input a valid 'product_id'.

2017

SpotExecuteExceedsBorrowLimit

Executing this action could result in exceeding your borrowing limit as your spot leverage is currently set to false. Please adjust your withdrawal amount or manage your borrowings to prevent potential risk.

2019

InappropriateSpotLeverage

Spot leverage cannot be applied to a non-spot product. Please ensure you're using the correct type of leverage for the product in question.

2020

OrderNotFound

Order with the provided digest ({digest}) could not be found. Please verify the order digest and try again.

2021

AddressRiskTooHigh

The risk associated with the provided address is too high. Please use a different address or mitigate the associated risk.

2022

InvalidNonce

The provided nonce is invalid. Ensure the nonce is correct and try again.

2023

AddressScreeningPending

Risk screening check for the provided address is still in progress. Please wait until the check is complete before proceeding.

2024

NoPriorDeposit

The provided address has no previous deposits. Ensure you're using an address with prior deposits.

2025

SingleSignatureInsufficientAccountValue

Your account must hold a minimum value of 5 USDT0 to enable single signature sessions. Please ensure your account balance meets this requirement.

2026

DuplicateSignerLinking

You cannot link a signer to the same address more than once. Please provide a unique address for each signer.

2027

SignatureLength

The provided signature does not meet the required length specifications. Please verify and provide a valid signature.

2028

InvalidSigner

The provided signature does not match with the sender's or the linked signer's. Please verify and provide the correct signature.

2029

InvalidSignerZero

Signer cannot be zero. Please provide a valid non-zero signer.

2030

LinkedSignerUpdateLimitExceeded

Linked Signer update limit exceeded. Please wait for {{wait_time}} seconds before trying again.

2031

FillOrKillNotFilled

Your 'Fill or Kill' order could not be entirely filled. Slippage parameters may be too conservative or size too large.

2033

NonceMissingInPayload

No nonce provided in the request payload. Please ensure a valid nonce is included.

2034

InvalidSignatureV

Invalid Signature: The 'v' value of the signature you provided is not valid. Please verify your signature and try again.

2035

SignatureError

Signature error: {error_msg}

2036

SubaccountHealthTooLow

Subaccount health insufficient. Please ensure sufficient health level in your subaccount to proceed.

2037

ExcessiveLPTokenBurn

Attempt to burn more LP tokens than currently owned. Please adjust the amount to match or be less than your current LP token balance.

2038

InvalidExecuteMessage

The execute message provided is invalid. Please verify and provide a valid execute message.

2039

MismatchedDigestsAndProductIdsLength

'digests' and 'productIds' arrays should have the same length. Please ensure their lengths match.

2040

InvalidBool

The value you entered is not a valid boolean. Please try again with a value of true or false.

2041

RebateExecuteFormatting

The length of 'subaccounts' array does not match the length of 'amounts' array. Ensure that both arrays have the same number of elements and try again.

2042

NotLiquidatable

Failed to initiate liquidation: The account does not meet the requirements for liquidation.

2043

LiquidatorHealthTooLow

Failed to initiate liquidation: The liquidator's account health is too low.

2044

PositiveInitialHealthLiquidationAttempt

Failed to initiate liquidation: The account to be liquidated has positive initial health.

2045

InvalidLiquidationParameters

Failed to initiate liquidation: Attempted to liquidate quote or provided invalid liquidation parameters.

2046

PerpLiquidationSizeIncrementMismatch

Failed to initiate liquidation: Attempted to liquidate perpetual contract but the amount is not divisible by sizeIncrement.

2047

InvalidLiquidationAmount

Failed to initiate liquidation: Attempted to liquidate either too little, too much or the signs are different.

2048

LiabilitiesBeforePerpsLiquidationAttempt

Failed to initiate liquidation: Attempted to liquidate liabilities before perpetual contracts.

2049

TransferFailed

ERC20 Transfer failed. Please verify the transaction details.

2050

UnauthorizedAction

Unauthorized action attempted. Please ensure you have the necessary permissions.

2051

NotFinalizableSubaccount

Attempted to finalize a subaccount which is not eligible for finalization. Ensure that the subaccount meets all the necessary conditions before proceeding.

2052

InvalidMaker

The maker order subaccount is invalid or has failed the risk check. Please verify the subaccount and ensure it meets the necessary risk parameters.

2053

OrdersCannotBeMatched

Order failed to match due to an internal error. Please try again.

2054

SlippageTooHigh

The requested operation could not be completed due to excessive slippage. Please adjust your order to match market conditions.

2055

InvalidPrice

Invalid price provided. The price must be greater than 0. Please input a valid price.

2056

ImmediateOrCancelDoesNotCross

Your 'Immediate or Cancel' order does not cross the book. Please review the market conditions or adjust your order.

2057

MaxTriggerOrdersLimitReached

You have reached the maximum number of trigger orders allowed for this subaccount.

2058

TriggerOrderNotFound

Trigger order with the provided digest ({digest}) could not be found. Please verify the order digest and try again.

2059

NotTriggerOrder

Submitted order is not a trigger order.

2060

InvalidProductIds

The provided 'product_ids' is invalid. Please verify input contains only valid products and no duplicates.

2061

InvalidProductType

Invalid product type {{product_type}}. 'product_type' must be 'spot' or 'perp'

2062

MissingProductIds

The 'product_ids' provided is empty. Please ensure you include a non-empty list of validproduct_idsin your request.

`product_ids`

2063

InvalidQueryResponse

Invalid query response. Expected {{Response}}.

2064

ReduceOnlyIncreasesPosition

Reduce only order increases position.

2065

InvalidExpirationBits

Invalid expiration bits: The 4th to 6th most significant bits are reserved and must be unset.

2066

CancelAndPlaceDifferentSenderOrSigner

Sender or signer of cancel and place are not the same.

2067

ReduceOnlyNotTaker

Only taker orders can be set as reduce only.

2068

SystemUnderMaintenance

We're currently performing maintenance on the system. Please try again later.

2069

MarketTradingBlocked

Trading is blocked for this market.

2070

MarketMaxOpenInterest

Market has reached maximum open interest. Please only close positions at this time.

2071

MaxUtilization

Product at maximum utilization

2072

OrderBatchExceedLimit

The number of specified 'orders' exceeds the limit. Please reduce the 'orders' to meet the defined limit.

2073

SelfMatchNotAllowed

Self-match is not allowed.

2074

MismatchedProductIds

Product IDs do not match.

2075

NonDefaultPrivateBatchOrder

Private batch order types must all be default.

2076

InvalidTriggerPrivateBatchOrder

Private batch order cannot be trigger order.

2077

TransferQuoteAmountTooSmall

Transfer quote amount is too small. You must transfer a minimum of 5 USDT0.

2078

TransferQuoteNewRecipientLimitExceeded

Transfer quote to new recipients limit exceeded. Please wait 24hrs before transferring quote to new recipients.

2079

SelfTransferQuoteNotAllowed

Self-transfer quote is not allowed.

2080

WebsocketCompressionRequired

Subscriptions require the header 'Sec-WebSocket-Extensions' with value 'permessage-deflate'.

2081

IsolatedSubaccountCannotPlaceIsolatedOrder

An isolated subaccount cannot place an isolated order.

2082

IsolatedSubaccountInvalidProduct

Invalid product_id for isolated subaccount.

2083

InvalidIsolatedSpotOrder

Isolated orders cannot be placed on spots.

2084

InvalidIsolatedTriggerOrder

Isolated orders cannot be trigger orders.

2085

InvalidIsolatedReduceOnlyOrder

Isolated orders cannot be reduce-only.

2086

InvalidIsolatedMargin

Isolated margin must be non-negative.

2087

FailedToCreateIsolatedSubaccount

Failed to create isolated subaccount.

2088

InvalidOrderFromIsolatedSubaccount

Orders from isolated subaccount must be reduce-only.

2089

InvalidLinkSignerSender

Cannot link signer to isolated subaccount.

2090

MintNlpAmountTooSmall

Nlp minting amount is too small. You must mint a minimum of 1 USDT0.

2091

AmountTooLarge

Amount is too large.

2092

NAccountHealthTooLow

N_ACCOUNT health insufficient.

2093

NotCanonicalChain

Can not execute in non-canonical chains.

2094

OrderSizeTooSmall

Invalid order size: Order amount, {order.amount}, or price, {order.price}, is too small. abs(amount) * price must be >= min_size; min_size for product {product_id}: {min_size}.

2095

InvalidOrderVersion

Invalid Order Version: the order version in the appendix, {version}, does not match the expected version: {expected_version}

2096

UnlockedNlpInsufficient

Do not have enough unlocked NLP.

2097

InvalidTriggerOrder

Invalid trigger order appendix.

2098

InvalidTwap

Invalid TWAP order.

2099

InvalidTwapOrderType

TWAP order must be of type 'Immediate or Cancel'. Please ensure your TWAP order uses the correct order type.

2100

InvalidTwapTimes

Invalid TWAP times: {times}. TWAP times must be between 1 and 500.

2101

InvalidTwapAmountDistribution

Invalid TWAP amount distribution: amount {amount} is not evenly divisible by times {times}. For non-random TWAP orders, the total amount must be evenly divisible by the number of executions.

2102

InvalidTwapExpiration

Invalid TWAP expiration: expiration time {expiration} exceeds maximum allowed duration of 25 hours from current time {current_time}. Please adjust the expiration time.

2103

InvalidTwapInterval

Invalid TWAP interval: interval {interval} seconds exceeds maximum allowed interval of 3600 seconds (1 hour).

2104

InvalidTwapTotalDuration

Invalid TWAP total duration: total duration {duration} seconds exceeds maximum allowed duration of 86400 seconds (24 hours).

2105

InvalidTwapExpirationTiming

Invalid TWAP expiration timing: expiration {expiration} is before the minimum required time {min_time} for the given interval and times.

2106

InvalidTwapRandomConfiguration

Invalid TWAP random configuration: amounts array presence {amounts_present} does not match is_twap_random flag {is_random}.

2107

InvalidTwapAmount

Invalid TWAP amount: amount {amount} is zero or has different sign than order amount {order_amount}.

2108

InvalidTwapAmountsSum

Invalid TWAP amounts sum: sum of amounts {sum} does not match order amount {order_amount}.

2109

InvalidTwapTriggerAmountConfiguration

Invalid TWAP trigger amount configuration: trigger_amount presence {trigger_amount_present} does not match is_twap_random flag {is_random}.

2110

InvalidTwapIsolated

TWAP orders cannot be isolated. Please remove the isolated flag from your TWAP order.

2111

MaxOrderLimitExceeded

Cannot place more than 50 orders.

2112

NlpPoolAccountsCannotPlaceIsolatedOrder

NLP pool accounts cannot place isolated order.

2113

NlpPoolAccountsCannotPlaceTriggerOrder

NLP pool accounts cannot place trigger order.

2114

BatchSenderMismatch

All orders in a batch must have the same sender. Please ensure all orders are from the same account.

2115

LiquidationFrontrunByNlp

Liquidation succeeded but was executed by the NLP account instead of the requested liquidator.

### Indexer API

3000

DigestsNotAllowed

Unable to accept 'digests' in conjunction with 'subaccount' or 'product_ids'. Please make sure your request does not contain these fields simultaneously.

3001

DigestsExceedLimit

The number of specified 'digests' exceeds the specified limit. Please reduce the 'digests' to meet the defined limit.

3002

MissingSubaccount

A 'subaccount' is required but not specified. Please ensure you include a 'subaccount' in your request.

3003

InvalidInterval

Invalid interval: Please try again with a different 'max_timestamp', 'granularity', or 'count'.

3004

InvalidWithdrawalIdx

Invalid idx: withdrawal tx not found at idx {{idx}}. Check the input idx and try again later.

3005

NotEnoughFastWithdrawalSignatures

Not enough signatures for tx at idx {{idx}}, try again later.

### Others

4000

PerpTickFormatting

The length of the 'avg_price_diffs' array does not match the length of 'product_ids'. Ensure that the arrays are correctly formed and try again.

4001

NotImplemented

The feature you are trying to use is not yet implemented. Please check back later.

4002

TemporarilyDisabledMintLp

MintLp operation is currently disabled. Please try again later.

4003

EvmRevert

A critical error occurred while attempting match. Reverted with: {revert message}

4004

WithdrawRisk

Protocol risk: {limit} withdrawal limit over 24 hours exceeded; Try again later

5000

InternalError

Internal error: {message}

[PreviousRate limits](/developer-resources/api/rate-limits)
[NextSymbols](/developer-resources/api/symbols)

Last updated1 month ago