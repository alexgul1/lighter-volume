---
url: https://nadohq.github.io/nado-python-sdk/api-reference.html
---

# API Reference

Detailed API Reference for Nado Protocol SDK.

## nado_protocol.client

**classnado_protocol.client.NadoClient(context)[source]**
  Bases:objectThe primary client interface for interacting with Nado Protocol.This client consolidates the functionality of various aspects of Nado such as spot, market,
subaccount, and perpetual (perp) operations.To initialize an instance of this client, use thecreate_nado_clientutility.Attributes:context (NadoClientContext): The client context containing configuration for interacting with Nado.market (MarketAPI): Sub-client for executing and querying market operations.subaccount (SubaccountAPI): Sub-client for executing and querying subaccount operations.spot (SpotAPI): Sub-client for executing and querying spot operations.perp (PerpAPI): Sub-client for executing and querying perpetual operations.rewards (RewardsAPI): Sub-client for executing and querying rewards operations (e.g: staking, claiming, etc).__init__(context)[source]Initialize a new instance of the NadoClient.This constructor should not be called directly. Instead, use thecreate_nado_clientutility to
create a new NadoClient. This is because thecreate_nado_clientutility includes important
additional setup steps that aren’t included in this constructor.Args:context (NadoClientContext): The client context.Note:Usecreate_nado_clientfor creating instances.context:NadoClientContextmarket:MarketAPIsubaccount:SubaccountAPIspot:SpotAPIperp:PerpAPIrewards:RewardsAPI

Bases:object

The primary client interface for interacting with Nado Protocol.

This client consolidates the functionality of various aspects of Nado such as spot, market,
subaccount, and perpetual (perp) operations.

To initialize an instance of this client, use thecreate_nado_clientutility.

**Attributes:**
  context (NadoClientContext): The client context containing configuration for interacting with Nado.market (MarketAPI): Sub-client for executing and querying market operations.subaccount (SubaccountAPI): Sub-client for executing and querying subaccount operations.spot (SpotAPI): Sub-client for executing and querying spot operations.perp (PerpAPI): Sub-client for executing and querying perpetual operations.rewards (RewardsAPI): Sub-client for executing and querying rewards operations (e.g: staking, claiming, etc).
- context (NadoClientContext): The client context containing configuration for interacting with Nado.

context (NadoClientContext): The client context containing configuration for interacting with Nado.

- market (MarketAPI): Sub-client for executing and querying market operations.

market (MarketAPI): Sub-client for executing and querying market operations.

- subaccount (SubaccountAPI): Sub-client for executing and querying subaccount operations.

subaccount (SubaccountAPI): Sub-client for executing and querying subaccount operations.

- spot (SpotAPI): Sub-client for executing and querying spot operations.

spot (SpotAPI): Sub-client for executing and querying spot operations.

- perp (PerpAPI): Sub-client for executing and querying perpetual operations.

perp (PerpAPI): Sub-client for executing and querying perpetual operations.

- rewards (RewardsAPI): Sub-client for executing and querying rewards operations (e.g: staking, claiming, etc).

rewards (RewardsAPI): Sub-client for executing and querying rewards operations (e.g: staking, claiming, etc).

**__init__(context)[source]**
  Initialize a new instance of the NadoClient.This constructor should not be called directly. Instead, use thecreate_nado_clientutility to
create a new NadoClient. This is because thecreate_nado_clientutility includes important
additional setup steps that aren’t included in this constructor.Args:context (NadoClientContext): The client context.Note:Usecreate_nado_clientfor creating instances.

Initialize a new instance of the NadoClient.

This constructor should not be called directly. Instead, use thecreate_nado_clientutility to
create a new NadoClient. This is because thecreate_nado_clientutility includes important
additional setup steps that aren’t included in this constructor.

**Args:**
  context (NadoClientContext): The client context.

context (NadoClientContext): The client context.

**Note:**
  Usecreate_nado_clientfor creating instances.

Usecreate_nado_clientfor creating instances.

**context:NadoClientContext**

**market:MarketAPI**

**subaccount:SubaccountAPI**

**spot:SpotAPI**

**perp:PerpAPI**

**rewards:RewardsAPI**

**classnado_protocol.client.NadoClientMode(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumNadoClientMode is an enumeration representing the operational modes of the NadoClient.Attributes:MAINNET: For operating in Nado’s mainnet environment deployed on Ink.DEVNET: For local development.TESTING: For running tests.DEVNET='devnet'TESTING='testing'TESTNET='testnet'MAINNET='mainnet'

Bases:StrEnum

NadoClientMode is an enumeration representing the operational modes of the NadoClient.

**Attributes:**
  MAINNET: For operating in Nado’s mainnet environment deployed on Ink.DEVNET: For local development.TESTING: For running tests.

MAINNET: For operating in Nado’s mainnet environment deployed on Ink.

DEVNET: For local development.

TESTING: For running tests.

**DEVNET='devnet'**

**TESTING='testing'**

**TESTNET='testnet'**

**MAINNET='mainnet'**

**nado_protocol.client.create_nado_client(mode,signer=None,context_opts=None)[source]**
  Create a new NadoClient based on the given mode and signer.This function will create a new NadoClientContext based on the provided mode, and then
initialize a new NadoClient with that context.Ifcontext_optsare provided, they will be used to create the client context. Otherwise,
default context options for the given mode will be used.Return type:NadoClientArgs:mode (NadoClientMode): The mode in which to operate the client. Can be one of the following:NadoClientMode.DEVNET: For local development.signer (Signer, optional): An instance of LocalAccount or a private key string for signing transactions.context_opts (NadoClientContextOpts, optional): Options for creating the client context.If not provided, default options for the given mode will be used.Returns:NadoClient: The created NadoClient instance.

Create a new NadoClient based on the given mode and signer.

This function will create a new NadoClientContext based on the provided mode, and then
initialize a new NadoClient with that context.

Ifcontext_optsare provided, they will be used to create the client context. Otherwise,
default context options for the given mode will be used.

**Return type:**
  NadoClient

NadoClient

**Args:**
  mode (NadoClientMode): The mode in which to operate the client. Can be one of the following:NadoClientMode.DEVNET: For local development.signer (Signer, optional): An instance of LocalAccount or a private key string for signing transactions.context_opts (NadoClientContextOpts, optional): Options for creating the client context.If not provided, default options for the given mode will be used.

**mode (NadoClientMode): The mode in which to operate the client. Can be one of the following:**
  NadoClientMode.DEVNET: For local development.

NadoClientMode.DEVNET: For local development.

signer (Signer, optional): An instance of LocalAccount or a private key string for signing transactions.

**context_opts (NadoClientContextOpts, optional): Options for creating the client context.**
  If not provided, default options for the given mode will be used.

If not provided, default options for the given mode will be used.

**Returns:**
  NadoClient: The created NadoClient instance.

NadoClient: The created NadoClient instance.

**classnado_protocol.client.NadoClientContext(signer,engine_client,indexer_client,trigger_client,contracts)[source]**
  Bases:objectContext required to use the Nado client.signer:Optional[LocalAccount]engine_client:EngineClientindexer_client:IndexerClienttrigger_client:Optional[TriggerClient]contracts:NadoContracts__init__(signer,engine_client,indexer_client,trigger_client,contracts)

Bases:object

Context required to use the Nado client.

**signer:Optional[LocalAccount]**

**engine_client:EngineClient**

**indexer_client:IndexerClient**

**trigger_client:Optional[TriggerClient]**

**contracts:NadoContracts**

**__init__(signer,engine_client,indexer_client,trigger_client,contracts)**

**classnado_protocol.client.NadoClientContextOpts(**data)[source]**
  Bases:BaseModelcontracts_context:Optional[NadoContractsContext]rpc_node_url:Optional[AnyUrl]engine_endpoint_url:Optional[AnyUrl]indexer_endpoint_url:Optional[AnyUrl]trigger_endpoint_url:Optional[AnyUrl]

Bases:BaseModel

**contracts_context:Optional[NadoContractsContext]**

**rpc_node_url:Optional[AnyUrl]**

**engine_endpoint_url:Optional[AnyUrl]**

**indexer_endpoint_url:Optional[AnyUrl]**

**trigger_endpoint_url:Optional[AnyUrl]**

**nado_protocol.client.create_nado_client_context(opts,signer=None)[source]**
  Initializes a NadoClientContext instance with the provided signer and options.Return type:NadoClientContextArgs:opts (NadoClientContextOpts): Options including endpoints for the engine and indexer clients.signer (Signer, optional): An instance of LocalAccount or a private key string for signing transactions.Returns:NadoClientContext: The initialized Nado client context.Note:This helper attempts to fully set up the engine, indexer and trigger clients, including the necessary verifying contracts
to correctly sign executes. If this step fails, it is skipped and can be set up later, while logging the error.

Initializes a NadoClientContext instance with the provided signer and options.

**Return type:**
  NadoClientContext

NadoClientContext

**Args:**
  opts (NadoClientContextOpts): Options including endpoints for the engine and indexer clients.signer (Signer, optional): An instance of LocalAccount or a private key string for signing transactions.

opts (NadoClientContextOpts): Options including endpoints for the engine and indexer clients.

signer (Signer, optional): An instance of LocalAccount or a private key string for signing transactions.

**Returns:**
  NadoClientContext: The initialized Nado client context.

NadoClientContext: The initialized Nado client context.

**Note:**
  This helper attempts to fully set up the engine, indexer and trigger clients, including the necessary verifying contracts
to correctly sign executes. If this step fails, it is skipped and can be set up later, while logging the error.

This helper attempts to fully set up the engine, indexer and trigger clients, including the necessary verifying contracts
to correctly sign executes. If this step fails, it is skipped and can be set up later, while logging the error.

## nado_protocol.client.apis

**classnado_protocol.client.apis.NadoBaseAPI(context)[source]**
  Bases:objectThe base class for all Nado API classes, providing the foundation for API-specific classes in the Nado client.NadoBaseAPI serves as a foundation for the hierarchical structure of the Nado API classes. This structure allows for better
organization and separation of concerns, with each API-specific subclass handling a different aspect of the Nado client’s functionality.Attributes:context (NadoClientContext): The context in which the API operates, providing access to the client’s state and services.Note:This class is not meant to be used directly. It provides base functionality for other API classes in the Nado client.__init__(context)[source]Initialize an instance of NadoBaseAPI.NadoBaseAPI requires a context during instantiation, which should be an instance of NadoClientContext. This context
provides access to the state and services of the Nado client and allows the API to interact with these.Args:context (NadoClientContext): The context in which this API operates. Provides access to the state and services
of the Nado client.context:NadoClientContext

Bases:object

The base class for all Nado API classes, providing the foundation for API-specific classes in the Nado client.

NadoBaseAPI serves as a foundation for the hierarchical structure of the Nado API classes. This structure allows for better
organization and separation of concerns, with each API-specific subclass handling a different aspect of the Nado client’s functionality.

**Attributes:**
  context (NadoClientContext): The context in which the API operates, providing access to the client’s state and services.

context (NadoClientContext): The context in which the API operates, providing access to the client’s state and services.

**Note:**
  This class is not meant to be used directly. It provides base functionality for other API classes in the Nado client.

This class is not meant to be used directly. It provides base functionality for other API classes in the Nado client.

**__init__(context)[source]**
  Initialize an instance of NadoBaseAPI.NadoBaseAPI requires a context during instantiation, which should be an instance of NadoClientContext. This context
provides access to the state and services of the Nado client and allows the API to interact with these.Args:context (NadoClientContext): The context in which this API operates. Provides access to the state and services
of the Nado client.

Initialize an instance of NadoBaseAPI.

NadoBaseAPI requires a context during instantiation, which should be an instance of NadoClientContext. This context
provides access to the state and services of the Nado client and allows the API to interact with these.

**Args:**
  context (NadoClientContext): The context in which this API operates. Provides access to the state and services
of the Nado client.

context (NadoClientContext): The context in which this API operates. Provides access to the state and services
of the Nado client.

**context:NadoClientContext**

**classnado_protocol.client.apis.MarketAPI(context)[source]**
  Bases:MarketExecuteAPI,MarketQueryAPIA unified interface for market operations in the Nado Protocol.This class combines functionalities from both MarketExecuteAPI and MarketQueryAPI
into a single interface, providing a simpler and more consistent way to perform market operations.
It allows for both query (data retrieval) and execution (transaction) operations for market.Inheritance:MarketExecuteAPI: This provides functionalities to execute various operations related to market.
These include actions like placing an order, canceling an order, minting and burning LP tokens.MarketQueryAPI: This provides functionalities to retrieve various kinds of information related to market.
These include operations like retrieving order books, historical orders, market matches, and others.Attributes and Methods: Inherited from MarketExecuteAPI and MarketQueryAPI.

Bases:MarketExecuteAPI,MarketQueryAPI

A unified interface for market operations in the Nado Protocol.

This class combines functionalities from both MarketExecuteAPI and MarketQueryAPI
into a single interface, providing a simpler and more consistent way to perform market operations.
It allows for both query (data retrieval) and execution (transaction) operations for market.

**Inheritance:**
  MarketExecuteAPI: This provides functionalities to execute various operations related to market.
These include actions like placing an order, canceling an order, minting and burning LP tokens.MarketQueryAPI: This provides functionalities to retrieve various kinds of information related to market.
These include operations like retrieving order books, historical orders, market matches, and others.

MarketExecuteAPI: This provides functionalities to execute various operations related to market.
These include actions like placing an order, canceling an order, minting and burning LP tokens.

MarketQueryAPI: This provides functionalities to retrieve various kinds of information related to market.
These include operations like retrieving order books, historical orders, market matches, and others.

Attributes and Methods: Inherited from MarketExecuteAPI and MarketQueryAPI.

**classnado_protocol.client.apis.MarketExecuteAPI(context)[source]**
  Bases:NadoBaseAPIProvides functionality to interact with the Nado’s market execution APIs.
This class contains methods that allow clients to execute operations such as minting LP tokens, burning LP tokens,
placing and cancelling orders on the Nado market.Attributes:context (NadoClientContext): The context that provides connectivity configuration for NadoClient.Note:This class should not be instantiated directly, it is designed to be used through a NadoClient instance.mint_nlp(params)[source]Mint NLP tokens through the engine.Return type:ExecuteResponseArgs:params (MintNlpParams): Parameters required to mint NLP tokens.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.burn_nlp(params)[source]Burn NLP tokens through the engine.Return type:ExecuteResponseArgs:params (BurnNlpParams): Parameters required to burn NLP tokens.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.place_order(params)[source]Places an order through the engine.Return type:ExecuteResponseArgs:params (PlaceOrderParams): Parameters required to place an order.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.place_market_order(params)[source]Places a market order through the engine.Return type:ExecuteResponseArgs:params (PlaceMarketOrderParams): Parameters required to place a market order.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.cancel_orders(params)[source]Cancels orders through the engine.Return type:ExecuteResponseArgs:params (CancelOrdersParams): Parameters required to cancel orders.Returns:ExecuteResponse: The response from the engine execution containing information about the canceled product orders.Raises:Exception: If there is an error during the execution or the response status is not “success”.cancel_product_orders(params)[source]Cancels all orders for provided products through the engine.Return type:ExecuteResponseArgs:params (CancelProductOrdersParams): Parameters required to cancel product orders.Returns:ExecuteResponse: The response from the engine execution containing information about the canceled product orders.Raises:Exception: If there is an error during the execution or the response status is not “success”.cancel_and_place(params)[source]Cancels orders and places a new one through the engine on the same request.Return type:ExecuteResponseArgs:params (CancelAndPlaceParams): Parameters required to cancel orders and place a new one.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.close_position(subaccount,product_id)[source]Places an order through the engine to close a position for the providedproduct_id.Return type:ExecuteResponseAttributes:subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.place_trigger_order(params)[source]Return type:ExecuteResponsecancel_trigger_orders(params)[source]Return type:ExecuteResponsecancel_trigger_product_orders(params)[source]Return type:ExecuteResponseplace_twap_order(product_id,price_x18,total_amount_x18,times,slippage_frac,interval_seconds,sender=None,subaccount_owner=None,subaccount_name='default',expiration=None,nonce=None,custom_amounts_x18=None,reduce_only=False,spot_leverage=None,id=None)[source]Place a TWAP (Time-Weighted Average Price) order.This is a convenience method that creates a TWAP trigger order with the specified parameters.Return type:ExecuteResponseArgs:product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
total_amount_x18 (str): The total amount to trade multiplied by 1e18 (signed, negative for sell).
times (int): Number of TWAP executions (1-500).
slippage_frac (float): Slippage tolerance as a fraction (e.g., 0.01 for 1%).
interval_seconds (int): Time interval between executions in seconds.
sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, calculated as min(((times - 1) * interval_seconds) + 1 hour, 25 hours) from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
custom_amounts_x18 (Optional[List[str]]): Custom amounts for each execution multiplied by 1e18.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.Returns:ExecuteResponse: The response from placing the TWAP order.Raises:MissingTriggerClient: If trigger client is not configured.place_price_trigger_order(product_id,price_x18,amount_x18,trigger_price_x18,trigger_type,sender=None,subaccount_owner=None,subaccount_name='default',expiration=None,nonce=None,reduce_only=False,order_type=OrderType.DEFAULT,spot_leverage=None,id=None,dependency=None)[source]Place a price trigger order.This is a convenience method that creates a price trigger order with the specified parameters.Return type:ExecuteResponseArgs:product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
amount_x18 (str): The amount to trade multiplied by 1e18 (signed, negative for sell).
trigger_price_x18 (str): The trigger price multiplied by 1e18.
trigger_type (str): Type of price trigger - one of:“last_price_above”, “last_price_below”,
“oracle_price_above”, “oracle_price_below”,
“mid_price_above”, “mid_price_below”.sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, defaults to 7 days from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
order_type (OrderType): Order execution type (DEFAULT, IOC, FOK, POST_ONLY). Defaults to DEFAULT.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.
dependency (Optional[dict]): Optional dependency trigger dict with ‘digest’ and ‘on_partial_fill’ keys.Returns:ExecuteResponse: The response from placing the price trigger order.Raises:MissingTriggerClient: If trigger client is not configured.
ValueError: If trigger_type is not supported.

Bases:NadoBaseAPI

Provides functionality to interact with the Nado’s market execution APIs.
This class contains methods that allow clients to execute operations such as minting LP tokens, burning LP tokens,
placing and cancelling orders on the Nado market.

**Attributes:**
  context (NadoClientContext): The context that provides connectivity configuration for NadoClient.

context (NadoClientContext): The context that provides connectivity configuration for NadoClient.

**Note:**
  This class should not be instantiated directly, it is designed to be used through a NadoClient instance.

This class should not be instantiated directly, it is designed to be used through a NadoClient instance.

**mint_nlp(params)[source]**
  Mint NLP tokens through the engine.Return type:ExecuteResponseArgs:params (MintNlpParams): Parameters required to mint NLP tokens.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Mint NLP tokens through the engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (MintNlpParams): Parameters required to mint NLP tokens.

params (MintNlpParams): Parameters required to mint NLP tokens.

**Returns:**
  ExecuteResponse: The response from the engine execution.

ExecuteResponse: The response from the engine execution.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**burn_nlp(params)[source]**
  Burn NLP tokens through the engine.Return type:ExecuteResponseArgs:params (BurnNlpParams): Parameters required to burn NLP tokens.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Burn NLP tokens through the engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (BurnNlpParams): Parameters required to burn NLP tokens.

params (BurnNlpParams): Parameters required to burn NLP tokens.

**Returns:**
  ExecuteResponse: The response from the engine execution.

ExecuteResponse: The response from the engine execution.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**place_order(params)[source]**
  Places an order through the engine.Return type:ExecuteResponseArgs:params (PlaceOrderParams): Parameters required to place an order.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Places an order through the engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (PlaceOrderParams): Parameters required to place an order.

params (PlaceOrderParams): Parameters required to place an order.

**Returns:**
  ExecuteResponse: The response from the engine execution.

ExecuteResponse: The response from the engine execution.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**place_market_order(params)[source]**
  Places a market order through the engine.Return type:ExecuteResponseArgs:params (PlaceMarketOrderParams): Parameters required to place a market order.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Places a market order through the engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (PlaceMarketOrderParams): Parameters required to place a market order.

params (PlaceMarketOrderParams): Parameters required to place a market order.

**Returns:**
  ExecuteResponse: The response from the engine execution.

ExecuteResponse: The response from the engine execution.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**cancel_orders(params)[source]**
  Cancels orders through the engine.Return type:ExecuteResponseArgs:params (CancelOrdersParams): Parameters required to cancel orders.Returns:ExecuteResponse: The response from the engine execution containing information about the canceled product orders.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Cancels orders through the engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (CancelOrdersParams): Parameters required to cancel orders.

params (CancelOrdersParams): Parameters required to cancel orders.

**Returns:**
  ExecuteResponse: The response from the engine execution containing information about the canceled product orders.

ExecuteResponse: The response from the engine execution containing information about the canceled product orders.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**cancel_product_orders(params)[source]**
  Cancels all orders for provided products through the engine.Return type:ExecuteResponseArgs:params (CancelProductOrdersParams): Parameters required to cancel product orders.Returns:ExecuteResponse: The response from the engine execution containing information about the canceled product orders.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Cancels all orders for provided products through the engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (CancelProductOrdersParams): Parameters required to cancel product orders.

params (CancelProductOrdersParams): Parameters required to cancel product orders.

**Returns:**
  ExecuteResponse: The response from the engine execution containing information about the canceled product orders.

ExecuteResponse: The response from the engine execution containing information about the canceled product orders.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**cancel_and_place(params)[source]**
  Cancels orders and places a new one through the engine on the same request.Return type:ExecuteResponseArgs:params (CancelAndPlaceParams): Parameters required to cancel orders and place a new one.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Cancels orders and places a new one through the engine on the same request.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (CancelAndPlaceParams): Parameters required to cancel orders and place a new one.

params (CancelAndPlaceParams): Parameters required to cancel orders and place a new one.

**Returns:**
  ExecuteResponse: The response from the engine execution.

ExecuteResponse: The response from the engine execution.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**close_position(subaccount,product_id)[source]**
  Places an order through the engine to close a position for the providedproduct_id.Return type:ExecuteResponseAttributes:subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Places an order through the engine to close a position for the providedproduct_id.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Attributes:**
  subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.Returns:ExecuteResponse: The response from the engine execution.

subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.

**Returns:**
  ExecuteResponse: The response from the engine execution.

ExecuteResponse: The response from the engine execution.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**place_trigger_order(params)[source]**
  Return type:ExecuteResponse

**Return type:**
  ExecuteResponse

ExecuteResponse

**cancel_trigger_orders(params)[source]**
  Return type:ExecuteResponse

**Return type:**
  ExecuteResponse

ExecuteResponse

**cancel_trigger_product_orders(params)[source]**
  Return type:ExecuteResponse

**Return type:**
  ExecuteResponse

ExecuteResponse

**place_twap_order(product_id,price_x18,total_amount_x18,times,slippage_frac,interval_seconds,sender=None,subaccount_owner=None,subaccount_name='default',expiration=None,nonce=None,custom_amounts_x18=None,reduce_only=False,spot_leverage=None,id=None)[source]**
  Place a TWAP (Time-Weighted Average Price) order.This is a convenience method that creates a TWAP trigger order with the specified parameters.Return type:ExecuteResponseArgs:product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
total_amount_x18 (str): The total amount to trade multiplied by 1e18 (signed, negative for sell).
times (int): Number of TWAP executions (1-500).
slippage_frac (float): Slippage tolerance as a fraction (e.g., 0.01 for 1%).
interval_seconds (int): Time interval between executions in seconds.
sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, calculated as min(((times - 1) * interval_seconds) + 1 hour, 25 hours) from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
custom_amounts_x18 (Optional[List[str]]): Custom amounts for each execution multiplied by 1e18.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.Returns:ExecuteResponse: The response from placing the TWAP order.Raises:MissingTriggerClient: If trigger client is not configured.

Place a TWAP (Time-Weighted Average Price) order.

This is a convenience method that creates a TWAP trigger order with the specified parameters.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
total_amount_x18 (str): The total amount to trade multiplied by 1e18 (signed, negative for sell).
times (int): Number of TWAP executions (1-500).
slippage_frac (float): Slippage tolerance as a fraction (e.g., 0.01 for 1%).
interval_seconds (int): Time interval between executions in seconds.
sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, calculated as min(((times - 1) * interval_seconds) + 1 hour, 25 hours) from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
custom_amounts_x18 (Optional[List[str]]): Custom amounts for each execution multiplied by 1e18.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.

product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
total_amount_x18 (str): The total amount to trade multiplied by 1e18 (signed, negative for sell).
times (int): Number of TWAP executions (1-500).
slippage_frac (float): Slippage tolerance as a fraction (e.g., 0.01 for 1%).
interval_seconds (int): Time interval between executions in seconds.
sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, calculated as min(((times - 1) * interval_seconds) + 1 hour, 25 hours) from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
custom_amounts_x18 (Optional[List[str]]): Custom amounts for each execution multiplied by 1e18.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.

**Returns:**
  ExecuteResponse: The response from placing the TWAP order.

ExecuteResponse: The response from placing the TWAP order.

**Raises:**
  MissingTriggerClient: If trigger client is not configured.

MissingTriggerClient: If trigger client is not configured.

**place_price_trigger_order(product_id,price_x18,amount_x18,trigger_price_x18,trigger_type,sender=None,subaccount_owner=None,subaccount_name='default',expiration=None,nonce=None,reduce_only=False,order_type=OrderType.DEFAULT,spot_leverage=None,id=None,dependency=None)[source]**
  Place a price trigger order.This is a convenience method that creates a price trigger order with the specified parameters.Return type:ExecuteResponseArgs:product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
amount_x18 (str): The amount to trade multiplied by 1e18 (signed, negative for sell).
trigger_price_x18 (str): The trigger price multiplied by 1e18.
trigger_type (str): Type of price trigger - one of:“last_price_above”, “last_price_below”,
“oracle_price_above”, “oracle_price_below”,
“mid_price_above”, “mid_price_below”.sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, defaults to 7 days from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
order_type (OrderType): Order execution type (DEFAULT, IOC, FOK, POST_ONLY). Defaults to DEFAULT.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.
dependency (Optional[dict]): Optional dependency trigger dict with ‘digest’ and ‘on_partial_fill’ keys.Returns:ExecuteResponse: The response from placing the price trigger order.Raises:MissingTriggerClient: If trigger client is not configured.
ValueError: If trigger_type is not supported.

Place a price trigger order.

This is a convenience method that creates a price trigger order with the specified parameters.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
amount_x18 (str): The amount to trade multiplied by 1e18 (signed, negative for sell).
trigger_price_x18 (str): The trigger price multiplied by 1e18.
trigger_type (str): Type of price trigger - one of:“last_price_above”, “last_price_below”,
“oracle_price_above”, “oracle_price_below”,
“mid_price_above”, “mid_price_below”.sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, defaults to 7 days from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
order_type (OrderType): Order execution type (DEFAULT, IOC, FOK, POST_ONLY). Defaults to DEFAULT.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.
dependency (Optional[dict]): Optional dependency trigger dict with ‘digest’ and ‘on_partial_fill’ keys.

product_id (int): The product ID for the order.
price_x18 (str): The limit price multiplied by 1e18.
amount_x18 (str): The amount to trade multiplied by 1e18 (signed, negative for sell).
trigger_price_x18 (str): The trigger price multiplied by 1e18.
trigger_type (str): Type of price trigger - one of:

“last_price_above”, “last_price_below”,
“oracle_price_above”, “oracle_price_below”,
“mid_price_above”, “mid_price_below”.

sender (Optional[str]): The sender address (32 bytes hex or SubaccountParams). If provided, takes precedence over subaccount_owner/subaccount_name.
subaccount_owner (Optional[str]): The subaccount owner address. If not provided, uses client’s signer address. Ignored if sender is provided.
subaccount_name (str): The subaccount name. Defaults to “default”. Ignored if sender is provided.
expiration (Optional[int]): Order expiration timestamp. If not provided, defaults to 7 days from now.
nonce (Optional[int]): Order nonce. If not provided, will be auto-generated.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
order_type (OrderType): Order execution type (DEFAULT, IOC, FOK, POST_ONLY). Defaults to DEFAULT.
spot_leverage (Optional[bool]): Whether to use spot leverage.
id (Optional[int]): Optional order ID.
dependency (Optional[dict]): Optional dependency trigger dict with ‘digest’ and ‘on_partial_fill’ keys.

**Returns:**
  ExecuteResponse: The response from placing the price trigger order.

ExecuteResponse: The response from placing the price trigger order.

**Raises:**
  MissingTriggerClient: If trigger client is not configured.
ValueError: If trigger_type is not supported.

MissingTriggerClient: If trigger client is not configured.
ValueError: If trigger_type is not supported.

**classnado_protocol.client.apis.MarketQueryAPI(context)[source]**
  Bases:NadoBaseAPIThe MarketQueryAPI class provides methods to interact with the Nado’s market querying APIs.This class provides functionality for querying various details about the market including fetching
information about order books, fetching historical orders, and retrieving market matches, among others.Attributes:context (NadoClientContext): The context that provides connectivity configuration for NadoClient.Note:This class should not be instantiated directly, it is designed to be used through a NadoClient instance.get_all_engine_markets()[source]Retrieves all market states from the off-chain engine.Return type:AllProductsDataReturns:AllProductsData: A data class object containing information about all products in the engine.get_all_product_symbols()[source]Retrieves all product symbols from the off-chain engineReturn type:list[ProductSymbol]Returns:ProductSymbolsData: A list of all products with corresponding symbol.get_market_liquidity(product_id,depth)[source]Retrieves liquidity per price tick from the engine.The engine will skip price levels that have no liquidity,
so it is not guaranteed that the bids/asks are evenly spacedReturn type:MarketLiquidityDataParameters:product_id (int): The product ID for which liquidity is to be fetched.
depth (int): The depth of the order book to retrieve liquidity from.Returns:MarketLiquidityData: A data class object containing liquidity information for the specified product.get_latest_market_price(product_id)[source]Retrieves the latest off-chain orderbook price from the engine for a specific product.Return type:MarketPriceDataArgs:product_id (int): The identifier for the product to retrieve the latest market price.Returns:MarketPriceData: A data class object containing information about the latest market price for the given product.get_subaccount_open_orders(product_id,sender)[source]Queries the off-chain engine to retrieve the status of any open orders for a given subaccount.This function fetches any open orders that a specific subaccount might have
for a specific product from the off-chain engine. The orders are returned as
an SubaccountOpenOrdersData object.Return type:SubaccountOpenOrdersDataArgs:product_id (int): The identifier for the product to fetch open orders.sender (str): The address and subaccount identifier as a bytes32 hex string.Returns:SubaccountOpenOrdersData: A data class object containing information about the open orders of a subaccount.get_subaccount_multi_products_open_orders(product_ids,sender)[source]Queries the off-chain engine to retrieve the status of any open orders for a given subaccount across multiple products.This function fetches any open orders that a specific subaccount might have
for products product from the off-chain engine. The orders are returned as
an SubaccountMultiProductsOpenOrdersData object.Return type:SubaccountMultiProductsOpenOrdersDataArgs:product_ids (list[int]): List of product ids to fetch open orders for.sender (str): The address and subaccount identifier as a bytes32 hex string.Returns:SubaccountMultiProductsOpenOrdersData: A data class object containing information about the open orders of a subaccount.get_subaccount_historical_orders(params)[source]Queries the indexer to fetch historical orders of a specific subaccount.This function retrieves a list of historical orders that a specific subaccount has placed.
The order data can be filtered using various parameters provided in the
IndexerSubaccountHistoricalOrdersParams object. The fetched historical orders data
is returned as an IndexerHistoricalOrdersData object.Return type:IndexerHistoricalOrdersDataArgs:params (IndexerSubaccountHistoricalOrdersParams): Parameters to filter the historical orders data:subaccount (str): The address and subaccount identifier as a bytes32 hex string.product_ids (list[int], optional): A list of identifiers for the products to fetch orders for. If provided, the function will return orders related to these products.idx (int, optional): Submission index. If provided, the function will return orders submitted before this index.max_time (int, optional): Maximum timestamp for the orders. The function will return orders submitted before this time.limit (int, optional): Maximum number of orders to return. If provided, the function will return at most ‘limit’ number of orders.Returns:IndexerHistoricalOrdersData: A data class object containing information about the historical orders of a subaccount.get_historical_orders_by_digest(digests)[source]Queries the indexer to fetch historical orders based on a list of provided digests.This function retrieves historical order data for a given list of order digests.
Each digest represents a unique order. The returned object includes the historical
order data for each digest in the provided list.Return type:IndexerHistoricalOrdersDataArgs:digests (list[str]): List of order digests. An order digest is a unique identifier for each order.Returns:IndexerHistoricalOrdersData: A data class object containing information about the historical orders associated with the provided digests.get_max_order_size(params)[source]Queries the engine to determine the maximum order size that can be submitted within
health requirements.Return type:MaxOrderSizeDataArgs:params (QueryMaxOrderSizeParams):sender (str): The address and subaccount identifier in a bytes32 hex string.product_id (int): The identifier for the spot/perp product.price_x18 (str): The price of the order in x18 format as a string.direction (MaxOrderSizeDirection): ‘long’ for max bid or ‘short’ for max ask.spot_leverage (Optional[bool]): If False, calculates max size without borrowing. Defaults to True.Returns:MaxOrderSizeData: The maximum size of the order that can be placed.get_max_nlp_mintable(product_id,sender,spot_leverage=None)[source]Queries the engine to determine the maximum base amount that can be contributed for minting LPs.Return type:MaxLpMintableDataArgs:product_id (int): The identifier for the spot/perp product.sender (str): The address and subaccount identifier in a bytes32 hex string.spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.Returns:MaxLpMintableData: Maximum base amount that can be contributed for minting LPs, in string format.get_candlesticks(params)[source]Fetches historical candlestick data for a specific product using the indexer.Return type:IndexerCandlesticksDataArgs:params (IndexerCandlesticksParams): Parameters for the query, which include:product_id (int): The identifier for the product.granularity (IndexerCandlesticksGranularity): Duration for each candlestick in seconds.Returns:IndexerCandlesticksData: Contains a list of historical candlestick data (IndexerCandlestick)
for the specified product at the specified granularity.Note:For obtaining the latest orderbook prices, consider using the ‘get_latest_market_price()’ method.get_perp_funding_rate(product_id)[source]Fetches the latest funding rate for a specific perp product.Return type:IndexerFundingRateDataArgs:product_id (int): Identifier for the perp product.Returns:IndexerFundingRateData: Contains the latest funding rate and related details for the given perp product.get_perp_funding_rates(product_ids)[source]Fetches the latest funding rates for a list of perp products.Return type:Dict[str,IndexerFundingRateData]Args:product_ids (list): List of identifiers for the perp products.Returns:dict: A dictionary mapping each product_id to its latest funding rate and related details.get_product_snapshots(params)[source]Fetches the historical snapshots for a specific product from the indexer.Return type:IndexerProductSnapshotsDataArgs:params (IndexerProductSnapshotsParams): Query parameters consisting of:product_id (int): Identifier for the product.idx (int, optional): Submission index to filter the returned snapshots.max_time (int, optional): Maximum timestamp to filter the returned snapshots.limit (int, optional): Maximum number of snapshots to return.Returns:IndexerProductSnapshotsData: Object containing lists of product snapshots and related transaction data.get_market_snapshots(params)[source]Fetches the historical market snapshots from the indexer.Return type:IndexerMarketSnapshotsDataArgs:params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.Returns:IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.get_trigger_orders(params)[source]Return type:TriggerQueryResponseget_isolated_positions(subaccount)[source]Retrieve isolated positions for a specific subaccount.Return type:IsolatedPositionsDataArgs:subaccount (str): Unique identifier for the subaccount.Returns:IsolatedPositionsData: A data class object containing information about the isolated positions for the specified subaccount.

Bases:NadoBaseAPI

The MarketQueryAPI class provides methods to interact with the Nado’s market querying APIs.

This class provides functionality for querying various details about the market including fetching
information about order books, fetching historical orders, and retrieving market matches, among others.

**Attributes:**
  context (NadoClientContext): The context that provides connectivity configuration for NadoClient.

context (NadoClientContext): The context that provides connectivity configuration for NadoClient.

**Note:**
  This class should not be instantiated directly, it is designed to be used through a NadoClient instance.

This class should not be instantiated directly, it is designed to be used through a NadoClient instance.

**get_all_engine_markets()[source]**
  Retrieves all market states from the off-chain engine.Return type:AllProductsDataReturns:AllProductsData: A data class object containing information about all products in the engine.

Retrieves all market states from the off-chain engine.

**Return type:**
  AllProductsData

AllProductsData

**Returns:**
  AllProductsData: A data class object containing information about all products in the engine.

AllProductsData: A data class object containing information about all products in the engine.

**get_all_product_symbols()[source]**
  Retrieves all product symbols from the off-chain engineReturn type:list[ProductSymbol]Returns:ProductSymbolsData: A list of all products with corresponding symbol.

Retrieves all product symbols from the off-chain engine

**Return type:**
  list[ProductSymbol]

list[ProductSymbol]

**Returns:**
  ProductSymbolsData: A list of all products with corresponding symbol.

ProductSymbolsData: A list of all products with corresponding symbol.

**get_market_liquidity(product_id,depth)[source]**
  Retrieves liquidity per price tick from the engine.The engine will skip price levels that have no liquidity,
so it is not guaranteed that the bids/asks are evenly spacedReturn type:MarketLiquidityDataParameters:product_id (int): The product ID for which liquidity is to be fetched.
depth (int): The depth of the order book to retrieve liquidity from.Returns:MarketLiquidityData: A data class object containing liquidity information for the specified product.

Retrieves liquidity per price tick from the engine.

The engine will skip price levels that have no liquidity,
so it is not guaranteed that the bids/asks are evenly spaced

**Return type:**
  MarketLiquidityData

MarketLiquidityData

**Parameters:**
  product_id (int): The product ID for which liquidity is to be fetched.
depth (int): The depth of the order book to retrieve liquidity from.

product_id (int): The product ID for which liquidity is to be fetched.
depth (int): The depth of the order book to retrieve liquidity from.

**Returns:**
  MarketLiquidityData: A data class object containing liquidity information for the specified product.

MarketLiquidityData: A data class object containing liquidity information for the specified product.

**get_latest_market_price(product_id)[source]**
  Retrieves the latest off-chain orderbook price from the engine for a specific product.Return type:MarketPriceDataArgs:product_id (int): The identifier for the product to retrieve the latest market price.Returns:MarketPriceData: A data class object containing information about the latest market price for the given product.

Retrieves the latest off-chain orderbook price from the engine for a specific product.

**Return type:**
  MarketPriceData

MarketPriceData

**Args:**
  product_id (int): The identifier for the product to retrieve the latest market price.

product_id (int): The identifier for the product to retrieve the latest market price.

**Returns:**
  MarketPriceData: A data class object containing information about the latest market price for the given product.

MarketPriceData: A data class object containing information about the latest market price for the given product.

**get_subaccount_open_orders(product_id,sender)[source]**
  Queries the off-chain engine to retrieve the status of any open orders for a given subaccount.This function fetches any open orders that a specific subaccount might have
for a specific product from the off-chain engine. The orders are returned as
an SubaccountOpenOrdersData object.Return type:SubaccountOpenOrdersDataArgs:product_id (int): The identifier for the product to fetch open orders.sender (str): The address and subaccount identifier as a bytes32 hex string.Returns:SubaccountOpenOrdersData: A data class object containing information about the open orders of a subaccount.

Queries the off-chain engine to retrieve the status of any open orders for a given subaccount.

This function fetches any open orders that a specific subaccount might have
for a specific product from the off-chain engine. The orders are returned as
an SubaccountOpenOrdersData object.

**Return type:**
  SubaccountOpenOrdersData

SubaccountOpenOrdersData

**Args:**
  product_id (int): The identifier for the product to fetch open orders.sender (str): The address and subaccount identifier as a bytes32 hex string.

product_id (int): The identifier for the product to fetch open orders.

sender (str): The address and subaccount identifier as a bytes32 hex string.

**Returns:**
  SubaccountOpenOrdersData: A data class object containing information about the open orders of a subaccount.

SubaccountOpenOrdersData: A data class object containing information about the open orders of a subaccount.

**get_subaccount_multi_products_open_orders(product_ids,sender)[source]**
  Queries the off-chain engine to retrieve the status of any open orders for a given subaccount across multiple products.This function fetches any open orders that a specific subaccount might have
for products product from the off-chain engine. The orders are returned as
an SubaccountMultiProductsOpenOrdersData object.Return type:SubaccountMultiProductsOpenOrdersDataArgs:product_ids (list[int]): List of product ids to fetch open orders for.sender (str): The address and subaccount identifier as a bytes32 hex string.Returns:SubaccountMultiProductsOpenOrdersData: A data class object containing information about the open orders of a subaccount.

Queries the off-chain engine to retrieve the status of any open orders for a given subaccount across multiple products.

This function fetches any open orders that a specific subaccount might have
for products product from the off-chain engine. The orders are returned as
an SubaccountMultiProductsOpenOrdersData object.

**Return type:**
  SubaccountMultiProductsOpenOrdersData

SubaccountMultiProductsOpenOrdersData

**Args:**
  product_ids (list[int]): List of product ids to fetch open orders for.sender (str): The address and subaccount identifier as a bytes32 hex string.

product_ids (list[int]): List of product ids to fetch open orders for.

sender (str): The address and subaccount identifier as a bytes32 hex string.

**Returns:**
  SubaccountMultiProductsOpenOrdersData: A data class object containing information about the open orders of a subaccount.

SubaccountMultiProductsOpenOrdersData: A data class object containing information about the open orders of a subaccount.

**get_subaccount_historical_orders(params)[source]**
  Queries the indexer to fetch historical orders of a specific subaccount.This function retrieves a list of historical orders that a specific subaccount has placed.
The order data can be filtered using various parameters provided in the
IndexerSubaccountHistoricalOrdersParams object. The fetched historical orders data
is returned as an IndexerHistoricalOrdersData object.Return type:IndexerHistoricalOrdersDataArgs:params (IndexerSubaccountHistoricalOrdersParams): Parameters to filter the historical orders data:subaccount (str): The address and subaccount identifier as a bytes32 hex string.product_ids (list[int], optional): A list of identifiers for the products to fetch orders for. If provided, the function will return orders related to these products.idx (int, optional): Submission index. If provided, the function will return orders submitted before this index.max_time (int, optional): Maximum timestamp for the orders. The function will return orders submitted before this time.limit (int, optional): Maximum number of orders to return. If provided, the function will return at most ‘limit’ number of orders.Returns:IndexerHistoricalOrdersData: A data class object containing information about the historical orders of a subaccount.

Queries the indexer to fetch historical orders of a specific subaccount.

This function retrieves a list of historical orders that a specific subaccount has placed.
The order data can be filtered using various parameters provided in the
IndexerSubaccountHistoricalOrdersParams object. The fetched historical orders data
is returned as an IndexerHistoricalOrdersData object.

**Return type:**
  IndexerHistoricalOrdersData

IndexerHistoricalOrdersData

**Args:**
  params (IndexerSubaccountHistoricalOrdersParams): Parameters to filter the historical orders data:subaccount (str): The address and subaccount identifier as a bytes32 hex string.product_ids (list[int], optional): A list of identifiers for the products to fetch orders for. If provided, the function will return orders related to these products.idx (int, optional): Submission index. If provided, the function will return orders submitted before this index.max_time (int, optional): Maximum timestamp for the orders. The function will return orders submitted before this time.limit (int, optional): Maximum number of orders to return. If provided, the function will return at most ‘limit’ number of orders.

**params (IndexerSubaccountHistoricalOrdersParams): Parameters to filter the historical orders data:**
  subaccount (str): The address and subaccount identifier as a bytes32 hex string.product_ids (list[int], optional): A list of identifiers for the products to fetch orders for. If provided, the function will return orders related to these products.idx (int, optional): Submission index. If provided, the function will return orders submitted before this index.max_time (int, optional): Maximum timestamp for the orders. The function will return orders submitted before this time.limit (int, optional): Maximum number of orders to return. If provided, the function will return at most ‘limit’ number of orders.
- subaccount (str): The address and subaccount identifier as a bytes32 hex string.

subaccount (str): The address and subaccount identifier as a bytes32 hex string.

- product_ids (list[int], optional): A list of identifiers for the products to fetch orders for. If provided, the function will return orders related to these products.

product_ids (list[int], optional): A list of identifiers for the products to fetch orders for. If provided, the function will return orders related to these products.

- idx (int, optional): Submission index. If provided, the function will return orders submitted before this index.

idx (int, optional): Submission index. If provided, the function will return orders submitted before this index.

- max_time (int, optional): Maximum timestamp for the orders. The function will return orders submitted before this time.

max_time (int, optional): Maximum timestamp for the orders. The function will return orders submitted before this time.

- limit (int, optional): Maximum number of orders to return. If provided, the function will return at most ‘limit’ number of orders.

limit (int, optional): Maximum number of orders to return. If provided, the function will return at most ‘limit’ number of orders.

**Returns:**
  IndexerHistoricalOrdersData: A data class object containing information about the historical orders of a subaccount.

IndexerHistoricalOrdersData: A data class object containing information about the historical orders of a subaccount.

**get_historical_orders_by_digest(digests)[source]**
  Queries the indexer to fetch historical orders based on a list of provided digests.This function retrieves historical order data for a given list of order digests.
Each digest represents a unique order. The returned object includes the historical
order data for each digest in the provided list.Return type:IndexerHistoricalOrdersDataArgs:digests (list[str]): List of order digests. An order digest is a unique identifier for each order.Returns:IndexerHistoricalOrdersData: A data class object containing information about the historical orders associated with the provided digests.

Queries the indexer to fetch historical orders based on a list of provided digests.

This function retrieves historical order data for a given list of order digests.
Each digest represents a unique order. The returned object includes the historical
order data for each digest in the provided list.

**Return type:**
  IndexerHistoricalOrdersData

IndexerHistoricalOrdersData

**Args:**
  digests (list[str]): List of order digests. An order digest is a unique identifier for each order.

digests (list[str]): List of order digests. An order digest is a unique identifier for each order.

**Returns:**
  IndexerHistoricalOrdersData: A data class object containing information about the historical orders associated with the provided digests.

IndexerHistoricalOrdersData: A data class object containing information about the historical orders associated with the provided digests.

**get_max_order_size(params)[source]**
  Queries the engine to determine the maximum order size that can be submitted within
health requirements.Return type:MaxOrderSizeDataArgs:params (QueryMaxOrderSizeParams):sender (str): The address and subaccount identifier in a bytes32 hex string.product_id (int): The identifier for the spot/perp product.price_x18 (str): The price of the order in x18 format as a string.direction (MaxOrderSizeDirection): ‘long’ for max bid or ‘short’ for max ask.spot_leverage (Optional[bool]): If False, calculates max size without borrowing. Defaults to True.Returns:MaxOrderSizeData: The maximum size of the order that can be placed.

Queries the engine to determine the maximum order size that can be submitted within
health requirements.

**Return type:**
  MaxOrderSizeData

MaxOrderSizeData

**Args:**
  params (QueryMaxOrderSizeParams):sender (str): The address and subaccount identifier in a bytes32 hex string.product_id (int): The identifier for the spot/perp product.price_x18 (str): The price of the order in x18 format as a string.direction (MaxOrderSizeDirection): ‘long’ for max bid or ‘short’ for max ask.spot_leverage (Optional[bool]): If False, calculates max size without borrowing. Defaults to True.

**params (QueryMaxOrderSizeParams):**
  sender (str): The address and subaccount identifier in a bytes32 hex string.product_id (int): The identifier for the spot/perp product.price_x18 (str): The price of the order in x18 format as a string.direction (MaxOrderSizeDirection): ‘long’ for max bid or ‘short’ for max ask.spot_leverage (Optional[bool]): If False, calculates max size without borrowing. Defaults to True.
- sender (str): The address and subaccount identifier in a bytes32 hex string.

sender (str): The address and subaccount identifier in a bytes32 hex string.

- product_id (int): The identifier for the spot/perp product.

product_id (int): The identifier for the spot/perp product.

- price_x18 (str): The price of the order in x18 format as a string.

price_x18 (str): The price of the order in x18 format as a string.

- direction (MaxOrderSizeDirection): ‘long’ for max bid or ‘short’ for max ask.

direction (MaxOrderSizeDirection): ‘long’ for max bid or ‘short’ for max ask.

- spot_leverage (Optional[bool]): If False, calculates max size without borrowing. Defaults to True.

spot_leverage (Optional[bool]): If False, calculates max size without borrowing. Defaults to True.

**Returns:**
  MaxOrderSizeData: The maximum size of the order that can be placed.

MaxOrderSizeData: The maximum size of the order that can be placed.

**get_max_nlp_mintable(product_id,sender,spot_leverage=None)[source]**
  Queries the engine to determine the maximum base amount that can be contributed for minting LPs.Return type:MaxLpMintableDataArgs:product_id (int): The identifier for the spot/perp product.sender (str): The address and subaccount identifier in a bytes32 hex string.spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.Returns:MaxLpMintableData: Maximum base amount that can be contributed for minting LPs, in string format.

Queries the engine to determine the maximum base amount that can be contributed for minting LPs.

**Return type:**
  MaxLpMintableData

MaxLpMintableData

**Args:**
  product_id (int): The identifier for the spot/perp product.sender (str): The address and subaccount identifier in a bytes32 hex string.spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.

product_id (int): The identifier for the spot/perp product.

sender (str): The address and subaccount identifier in a bytes32 hex string.

spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.

**Returns:**
  MaxLpMintableData: Maximum base amount that can be contributed for minting LPs, in string format.

MaxLpMintableData: Maximum base amount that can be contributed for minting LPs, in string format.

**get_candlesticks(params)[source]**
  Fetches historical candlestick data for a specific product using the indexer.Return type:IndexerCandlesticksDataArgs:params (IndexerCandlesticksParams): Parameters for the query, which include:product_id (int): The identifier for the product.granularity (IndexerCandlesticksGranularity): Duration for each candlestick in seconds.Returns:IndexerCandlesticksData: Contains a list of historical candlestick data (IndexerCandlestick)
for the specified product at the specified granularity.Note:For obtaining the latest orderbook prices, consider using the ‘get_latest_market_price()’ method.

Fetches historical candlestick data for a specific product using the indexer.

**Return type:**
  IndexerCandlesticksData

IndexerCandlesticksData

**Args:**
  params (IndexerCandlesticksParams): Parameters for the query, which include:product_id (int): The identifier for the product.granularity (IndexerCandlesticksGranularity): Duration for each candlestick in seconds.

**params (IndexerCandlesticksParams): Parameters for the query, which include:**
  product_id (int): The identifier for the product.granularity (IndexerCandlesticksGranularity): Duration for each candlestick in seconds.
- product_id (int): The identifier for the product.

product_id (int): The identifier for the product.

- granularity (IndexerCandlesticksGranularity): Duration for each candlestick in seconds.

granularity (IndexerCandlesticksGranularity): Duration for each candlestick in seconds.

**Returns:**
  IndexerCandlesticksData: Contains a list of historical candlestick data (IndexerCandlestick)
for the specified product at the specified granularity.

IndexerCandlesticksData: Contains a list of historical candlestick data (IndexerCandlestick)
for the specified product at the specified granularity.

**Note:**
  For obtaining the latest orderbook prices, consider using the ‘get_latest_market_price()’ method.

For obtaining the latest orderbook prices, consider using the ‘get_latest_market_price()’ method.

**get_perp_funding_rate(product_id)[source]**
  Fetches the latest funding rate for a specific perp product.Return type:IndexerFundingRateDataArgs:product_id (int): Identifier for the perp product.Returns:IndexerFundingRateData: Contains the latest funding rate and related details for the given perp product.

Fetches the latest funding rate for a specific perp product.

**Return type:**
  IndexerFundingRateData

IndexerFundingRateData

**Args:**
  product_id (int): Identifier for the perp product.

product_id (int): Identifier for the perp product.

**Returns:**
  IndexerFundingRateData: Contains the latest funding rate and related details for the given perp product.

IndexerFundingRateData: Contains the latest funding rate and related details for the given perp product.

**get_perp_funding_rates(product_ids)[source]**
  Fetches the latest funding rates for a list of perp products.Return type:Dict[str,IndexerFundingRateData]Args:product_ids (list): List of identifiers for the perp products.Returns:dict: A dictionary mapping each product_id to its latest funding rate and related details.

Fetches the latest funding rates for a list of perp products.

**Return type:**
  Dict[str,IndexerFundingRateData]

Dict[str,IndexerFundingRateData]

**Args:**
  product_ids (list): List of identifiers for the perp products.

product_ids (list): List of identifiers for the perp products.

**Returns:**
  dict: A dictionary mapping each product_id to its latest funding rate and related details.

dict: A dictionary mapping each product_id to its latest funding rate and related details.

**get_product_snapshots(params)[source]**
  Fetches the historical snapshots for a specific product from the indexer.Return type:IndexerProductSnapshotsDataArgs:params (IndexerProductSnapshotsParams): Query parameters consisting of:product_id (int): Identifier for the product.idx (int, optional): Submission index to filter the returned snapshots.max_time (int, optional): Maximum timestamp to filter the returned snapshots.limit (int, optional): Maximum number of snapshots to return.Returns:IndexerProductSnapshotsData: Object containing lists of product snapshots and related transaction data.

Fetches the historical snapshots for a specific product from the indexer.

**Return type:**
  IndexerProductSnapshotsData

IndexerProductSnapshotsData

**Args:**
  params (IndexerProductSnapshotsParams): Query parameters consisting of:product_id (int): Identifier for the product.idx (int, optional): Submission index to filter the returned snapshots.max_time (int, optional): Maximum timestamp to filter the returned snapshots.limit (int, optional): Maximum number of snapshots to return.

**params (IndexerProductSnapshotsParams): Query parameters consisting of:**
  product_id (int): Identifier for the product.idx (int, optional): Submission index to filter the returned snapshots.max_time (int, optional): Maximum timestamp to filter the returned snapshots.limit (int, optional): Maximum number of snapshots to return.
- product_id (int): Identifier for the product.

product_id (int): Identifier for the product.

- idx (int, optional): Submission index to filter the returned snapshots.

idx (int, optional): Submission index to filter the returned snapshots.

- max_time (int, optional): Maximum timestamp to filter the returned snapshots.

max_time (int, optional): Maximum timestamp to filter the returned snapshots.

- limit (int, optional): Maximum number of snapshots to return.

limit (int, optional): Maximum number of snapshots to return.

**Returns:**
  IndexerProductSnapshotsData: Object containing lists of product snapshots and related transaction data.

IndexerProductSnapshotsData: Object containing lists of product snapshots and related transaction data.

**get_market_snapshots(params)[source]**
  Fetches the historical market snapshots from the indexer.Return type:IndexerMarketSnapshotsDataArgs:params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.Returns:IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.

Fetches the historical market snapshots from the indexer.

**Return type:**
  IndexerMarketSnapshotsData

IndexerMarketSnapshotsData

**Args:**
  params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.

params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.

**Returns:**
  IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.

IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.

**get_trigger_orders(params)[source]**
  Return type:TriggerQueryResponse

**Return type:**
  TriggerQueryResponse

TriggerQueryResponse

**get_isolated_positions(subaccount)[source]**
  Retrieve isolated positions for a specific subaccount.Return type:IsolatedPositionsDataArgs:subaccount (str): Unique identifier for the subaccount.Returns:IsolatedPositionsData: A data class object containing information about the isolated positions for the specified subaccount.

Retrieve isolated positions for a specific subaccount.

**Return type:**
  IsolatedPositionsData

IsolatedPositionsData

**Args:**
  subaccount (str): Unique identifier for the subaccount.

subaccount (str): Unique identifier for the subaccount.

**Returns:**
  IsolatedPositionsData: A data class object containing information about the isolated positions for the specified subaccount.

IsolatedPositionsData: A data class object containing information about the isolated positions for the specified subaccount.

**classnado_protocol.client.apis.SpotAPI(context)[source]**
  Bases:SpotExecuteAPI,SpotQueryAPIA unified interface for spot operations in the Nado Protocol.This class combines functionalities from both SpotExecuteAPI and SpotQueryAPI
into a single interface, providing a simpler and more consistent way to perform spot operations.
It allows for both query (data retrieval) and execution (transaction) operations for spot products.Inheritance:SpotExecuteAPI: This provides functionalities to execute various operations related to spot products,
such as depositing a specified amount into a spot product.SpotQueryAPI: This provides functionalities to retrieve various kinds of information related to spot products,
such as getting the wallet token balance of a given spot product.Attributes and Methods: Inherited from SpotExecuteAPI and SpotQueryAPI.

Bases:SpotExecuteAPI,SpotQueryAPI

A unified interface for spot operations in the Nado Protocol.

This class combines functionalities from both SpotExecuteAPI and SpotQueryAPI
into a single interface, providing a simpler and more consistent way to perform spot operations.
It allows for both query (data retrieval) and execution (transaction) operations for spot products.

**Inheritance:**
  SpotExecuteAPI: This provides functionalities to execute various operations related to spot products,
such as depositing a specified amount into a spot product.SpotQueryAPI: This provides functionalities to retrieve various kinds of information related to spot products,
such as getting the wallet token balance of a given spot product.

SpotExecuteAPI: This provides functionalities to execute various operations related to spot products,
such as depositing a specified amount into a spot product.

SpotQueryAPI: This provides functionalities to retrieve various kinds of information related to spot products,
such as getting the wallet token balance of a given spot product.

Attributes and Methods: Inherited from SpotExecuteAPI and SpotQueryAPI.

**classnado_protocol.client.apis.BaseSpotAPI(context)[source]**
  Bases:NadoBaseAPIBase class for Spot operations in the Nado Protocol.This class provides basic functionality for retrieving product-specific information
from the spot market of the Nado Protocol, such as the associated ERC20 token contract for a given spot product.Attributes:context (NadoClientContext): Provides connectivity details for accessing Nado APIs.Methods:get_token_contract_for_product: Retrieves the associated ERC20 token contract for a given spot product.get_token_contract_for_product(product_id)[source]Retrieves the associated ERC20 token contract for a given spot product.Return type:ContractArgs:product_id (int): The identifier for the spot product.Returns:Contract: The associated ERC20 token contract for the specified spot product.Raises:InvalidProductId: If the provided product ID is not valid.

Bases:NadoBaseAPI

Base class for Spot operations in the Nado Protocol.

This class provides basic functionality for retrieving product-specific information
from the spot market of the Nado Protocol, such as the associated ERC20 token contract for a given spot product.

**Attributes:**
  context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

**Methods:**
  get_token_contract_for_product: Retrieves the associated ERC20 token contract for a given spot product.

get_token_contract_for_product: Retrieves the associated ERC20 token contract for a given spot product.

**get_token_contract_for_product(product_id)[source]**
  Retrieves the associated ERC20 token contract for a given spot product.Return type:ContractArgs:product_id (int): The identifier for the spot product.Returns:Contract: The associated ERC20 token contract for the specified spot product.Raises:InvalidProductId: If the provided product ID is not valid.

Retrieves the associated ERC20 token contract for a given spot product.

**Return type:**
  Contract

Contract

**Args:**
  product_id (int): The identifier for the spot product.

product_id (int): The identifier for the spot product.

**Returns:**
  Contract: The associated ERC20 token contract for the specified spot product.

Contract: The associated ERC20 token contract for the specified spot product.

**Raises:**
  InvalidProductId: If the provided product ID is not valid.

InvalidProductId: If the provided product ID is not valid.

**classnado_protocol.client.apis.SpotExecuteAPI(context)[source]**
  Bases:BaseSpotAPIClass providing execution operations for the spot market in the Nado Protocol.This class provides functionality for executing transactions related to spot products,
such as depositing a specified amount into a spot product.Inheritance:BaseSpotAPI: Base class for Spot operations. Inherits connectivity context and base functionalities.deposit(params,signer=None)[source]Executes the operation of depositing a specified amount into a spot product.Return type:strArgs:params (DepositCollateralParams): Parameters required for depositing collateral.signer (LocalAccount, optional):  The account that will sign the deposit transaction. If no signer is provided, the signer set in the client context will be used.Raises:MissingSignerException: Raised when there is no signer provided and no signer set in the client context.Returns:str: The deposit collateral transaction hash.withdraw(params)[source]Executes a withdrawal for the specified spot product via the off-chain engine.Return type:ExecuteResponseArgs:params (WithdrawCollateralParams): Parameters needed to execute the withdrawal.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.approve_allowance(product_id,amount,signer=None)[source]Approves an allowance for a certain amount of tokens for a spot product.Return type:strArgs:product_id (int): The identifier of the spot product for which to approve an allowance.amount (int): The amount of the tokens to be approved.signer (LocalAccount, optional):  The account that will sign the approval transaction. If no signer is provided, the signer set in the client context will be used.Returns:str: The approve allowance transaction hash.Raises:MissingSignerException: Raised when there is no signer provided and no signer set in the client context.
InvalidProductId: If the provided product ID is not valid.

Bases:BaseSpotAPI

Class providing execution operations for the spot market in the Nado Protocol.

This class provides functionality for executing transactions related to spot products,
such as depositing a specified amount into a spot product.

**Inheritance:**
  BaseSpotAPI: Base class for Spot operations. Inherits connectivity context and base functionalities.

BaseSpotAPI: Base class for Spot operations. Inherits connectivity context and base functionalities.

**deposit(params,signer=None)[source]**
  Executes the operation of depositing a specified amount into a spot product.Return type:strArgs:params (DepositCollateralParams): Parameters required for depositing collateral.signer (LocalAccount, optional):  The account that will sign the deposit transaction. If no signer is provided, the signer set in the client context will be used.Raises:MissingSignerException: Raised when there is no signer provided and no signer set in the client context.Returns:str: The deposit collateral transaction hash.

Executes the operation of depositing a specified amount into a spot product.

**Return type:**
  str

str

**Args:**
  params (DepositCollateralParams): Parameters required for depositing collateral.signer (LocalAccount, optional):  The account that will sign the deposit transaction. If no signer is provided, the signer set in the client context will be used.

params (DepositCollateralParams): Parameters required for depositing collateral.

signer (LocalAccount, optional):  The account that will sign the deposit transaction. If no signer is provided, the signer set in the client context will be used.

**Raises:**
  MissingSignerException: Raised when there is no signer provided and no signer set in the client context.

MissingSignerException: Raised when there is no signer provided and no signer set in the client context.

**Returns:**
  str: The deposit collateral transaction hash.

str: The deposit collateral transaction hash.

**withdraw(params)[source]**
  Executes a withdrawal for the specified spot product via the off-chain engine.Return type:ExecuteResponseArgs:params (WithdrawCollateralParams): Parameters needed to execute the withdrawal.Returns:ExecuteResponse: The response from the engine execution.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Executes a withdrawal for the specified spot product via the off-chain engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (WithdrawCollateralParams): Parameters needed to execute the withdrawal.

params (WithdrawCollateralParams): Parameters needed to execute the withdrawal.

**Returns:**
  ExecuteResponse: The response from the engine execution.

ExecuteResponse: The response from the engine execution.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**approve_allowance(product_id,amount,signer=None)[source]**
  Approves an allowance for a certain amount of tokens for a spot product.Return type:strArgs:product_id (int): The identifier of the spot product for which to approve an allowance.amount (int): The amount of the tokens to be approved.signer (LocalAccount, optional):  The account that will sign the approval transaction. If no signer is provided, the signer set in the client context will be used.Returns:str: The approve allowance transaction hash.Raises:MissingSignerException: Raised when there is no signer provided and no signer set in the client context.
InvalidProductId: If the provided product ID is not valid.

Approves an allowance for a certain amount of tokens for a spot product.

**Return type:**
  str

str

**Args:**
  product_id (int): The identifier of the spot product for which to approve an allowance.amount (int): The amount of the tokens to be approved.signer (LocalAccount, optional):  The account that will sign the approval transaction. If no signer is provided, the signer set in the client context will be used.

product_id (int): The identifier of the spot product for which to approve an allowance.

amount (int): The amount of the tokens to be approved.

signer (LocalAccount, optional):  The account that will sign the approval transaction. If no signer is provided, the signer set in the client context will be used.

**Returns:**
  str: The approve allowance transaction hash.

str: The approve allowance transaction hash.

**Raises:**
  MissingSignerException: Raised when there is no signer provided and no signer set in the client context.
InvalidProductId: If the provided product ID is not valid.

MissingSignerException: Raised when there is no signer provided and no signer set in the client context.
InvalidProductId: If the provided product ID is not valid.

**classnado_protocol.client.apis.SpotQueryAPI(context)[source]**
  Bases:BaseSpotAPIClass providing querying operations for the spot market in the Nado Protocol.This class allows for retrieval of various kinds of information related to spot products,
such as getting wallet token balance of a given spot product.Inheritance:BaseSpotAPI: Base class for Spot operations. Inherits connectivity context and base functionalities.get_max_withdrawable(product_id,sender,spot_leverage=None)[source]Retrieves the estimated maximum withdrawable amount for a provided spot product.Return type:MaxWithdrawableDataArgs:product_id (int): The identifier for the spot product.sender (str): The address and subaccount identifier in a bytes32 hex string.spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.Returns:MaxWithdrawableData: The maximum withdrawable amount for the spot product.get_token_wallet_balance(product_id,address)[source]Retrieves the balance of a specific token in the user’s wallet (i.e. not in a Nado subaccount)Return type:floatArgs:product_id (int): Identifier for the spot product.address (str): User’s wallet address.Returns:float: The balance of the token in the user’s wallet in decimal form.Raises:InvalidProductId: If the provided product ID is not valid.get_token_allowance(product_id,address)[source]Retrieves the current token allowance of a specified spot product.Return type:floatArgs:product_id (int): Identifier for the spot product.address (str): The user’s wallet address.Returns:float: The current token allowance of the user’s wallet address to the associated spot product.Raises:InvalidProductId: If the provided product ID is not valid.

Bases:BaseSpotAPI

Class providing querying operations for the spot market in the Nado Protocol.

This class allows for retrieval of various kinds of information related to spot products,
such as getting wallet token balance of a given spot product.

**Inheritance:**
  BaseSpotAPI: Base class for Spot operations. Inherits connectivity context and base functionalities.

BaseSpotAPI: Base class for Spot operations. Inherits connectivity context and base functionalities.

**get_max_withdrawable(product_id,sender,spot_leverage=None)[source]**
  Retrieves the estimated maximum withdrawable amount for a provided spot product.Return type:MaxWithdrawableDataArgs:product_id (int): The identifier for the spot product.sender (str): The address and subaccount identifier in a bytes32 hex string.spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.Returns:MaxWithdrawableData: The maximum withdrawable amount for the spot product.

Retrieves the estimated maximum withdrawable amount for a provided spot product.

**Return type:**
  MaxWithdrawableData

MaxWithdrawableData

**Args:**
  product_id (int): The identifier for the spot product.sender (str): The address and subaccount identifier in a bytes32 hex string.spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.

product_id (int): The identifier for the spot product.

sender (str): The address and subaccount identifier in a bytes32 hex string.

spot_leverage (Optional[bool]): If False, calculates max amount without considering leverage. Defaults to True.

**Returns:**
  MaxWithdrawableData: The maximum withdrawable amount for the spot product.

MaxWithdrawableData: The maximum withdrawable amount for the spot product.

**get_token_wallet_balance(product_id,address)[source]**
  Retrieves the balance of a specific token in the user’s wallet (i.e. not in a Nado subaccount)Return type:floatArgs:product_id (int): Identifier for the spot product.address (str): User’s wallet address.Returns:float: The balance of the token in the user’s wallet in decimal form.Raises:InvalidProductId: If the provided product ID is not valid.

Retrieves the balance of a specific token in the user’s wallet (i.e. not in a Nado subaccount)

**Return type:**
  float

float

**Args:**
  product_id (int): Identifier for the spot product.address (str): User’s wallet address.

product_id (int): Identifier for the spot product.

address (str): User’s wallet address.

**Returns:**
  float: The balance of the token in the user’s wallet in decimal form.

float: The balance of the token in the user’s wallet in decimal form.

**Raises:**
  InvalidProductId: If the provided product ID is not valid.

InvalidProductId: If the provided product ID is not valid.

**get_token_allowance(product_id,address)[source]**
  Retrieves the current token allowance of a specified spot product.Return type:floatArgs:product_id (int): Identifier for the spot product.address (str): The user’s wallet address.Returns:float: The current token allowance of the user’s wallet address to the associated spot product.Raises:InvalidProductId: If the provided product ID is not valid.

Retrieves the current token allowance of a specified spot product.

**Return type:**
  float

float

**Args:**
  product_id (int): Identifier for the spot product.address (str): The user’s wallet address.

product_id (int): Identifier for the spot product.

address (str): The user’s wallet address.

**Returns:**
  float: The current token allowance of the user’s wallet address to the associated spot product.

float: The current token allowance of the user’s wallet address to the associated spot product.

**Raises:**
  InvalidProductId: If the provided product ID is not valid.

InvalidProductId: If the provided product ID is not valid.

**classnado_protocol.client.apis.SubaccountAPI(context)[source]**
  Bases:SubaccountExecuteAPI,SubaccountQueryAPIA unified interface for subaccount operations in the Nado Protocol.This class combines functionalities from both SubaccountExecuteAPI and SubaccountQueryAPI
into a single interface, providing a simpler and more consistent way to perform subaccount operations.
It allows for both query (data retrieval) and execution (transaction) operations for subaccounts.Inheritance:SubaccountExecuteAPI: This provides functionalities to execute various operations related to subaccounts.
These include actions like liquidating a subaccount or linking a signer to a subaccount.SubaccountQueryAPI: This provides functionalities to retrieve various kinds of information related to subaccounts.
These include operations like retrieving a summary of a subaccount’s state, retrieving the fee rates associated with a
subaccount, querying token rewards for a wallet, and getting linked signer rate limits for a subaccount.Attributes and Methods: Inherited from SubaccountExecuteAPI and SubaccountQueryAPI.

Bases:SubaccountExecuteAPI,SubaccountQueryAPI

A unified interface for subaccount operations in the Nado Protocol.

This class combines functionalities from both SubaccountExecuteAPI and SubaccountQueryAPI
into a single interface, providing a simpler and more consistent way to perform subaccount operations.
It allows for both query (data retrieval) and execution (transaction) operations for subaccounts.

**Inheritance:**
  SubaccountExecuteAPI: This provides functionalities to execute various operations related to subaccounts.
These include actions like liquidating a subaccount or linking a signer to a subaccount.SubaccountQueryAPI: This provides functionalities to retrieve various kinds of information related to subaccounts.
These include operations like retrieving a summary of a subaccount’s state, retrieving the fee rates associated with a
subaccount, querying token rewards for a wallet, and getting linked signer rate limits for a subaccount.

SubaccountExecuteAPI: This provides functionalities to execute various operations related to subaccounts.
These include actions like liquidating a subaccount or linking a signer to a subaccount.

SubaccountQueryAPI: This provides functionalities to retrieve various kinds of information related to subaccounts.
These include operations like retrieving a summary of a subaccount’s state, retrieving the fee rates associated with a
subaccount, querying token rewards for a wallet, and getting linked signer rate limits for a subaccount.

Attributes and Methods: Inherited from SubaccountExecuteAPI and SubaccountQueryAPI.

**classnado_protocol.client.apis.SubaccountExecuteAPI(context)[source]**
  Bases:NadoBaseAPIProvides functionalities for executing operations related to subaccounts in the Nado Protocol.Inherits from NadoBaseAPI, which provides a basic context setup for accessing Nado.
This class extends the base class to provide specific functionalities for executing actions related to subaccounts.The provided methods include:
-liquidate_subaccount: Performs the liquidation of a subaccount.
-link_signer: Links a signer to a subaccount, granting them transaction signing permissions.Attributes:context (NadoClientContext): Provides connectivity details for accessing Nado APIs.liquidate_subaccount(params)[source]Liquidates a subaccount through the engine.Return type:ExecuteResponseArgs:params (LiquidateSubaccountParams): Parameters for liquidating the subaccount.Returns:ExecuteResponse: Execution response from the engine.Raises:Exception: If there is an error during the execution or the response status is not “success”.link_signer(params)[source]Links a signer to a subaccount to allow them to sign transactions on behalf of the subaccount.Return type:ExecuteResponseArgs:params (LinkSignerParams): Parameters for linking a signer to a subaccount.Returns:ExecuteResponse: Execution response from the engine.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Bases:NadoBaseAPI

Provides functionalities for executing operations related to subaccounts in the Nado Protocol.

Inherits from NadoBaseAPI, which provides a basic context setup for accessing Nado.
This class extends the base class to provide specific functionalities for executing actions related to subaccounts.

The provided methods include:
-liquidate_subaccount: Performs the liquidation of a subaccount.
-link_signer: Links a signer to a subaccount, granting them transaction signing permissions.

**Attributes:**
  context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

**liquidate_subaccount(params)[source]**
  Liquidates a subaccount through the engine.Return type:ExecuteResponseArgs:params (LiquidateSubaccountParams): Parameters for liquidating the subaccount.Returns:ExecuteResponse: Execution response from the engine.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Liquidates a subaccount through the engine.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (LiquidateSubaccountParams): Parameters for liquidating the subaccount.

params (LiquidateSubaccountParams): Parameters for liquidating the subaccount.

**Returns:**
  ExecuteResponse: Execution response from the engine.

ExecuteResponse: Execution response from the engine.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**link_signer(params)[source]**
  Links a signer to a subaccount to allow them to sign transactions on behalf of the subaccount.Return type:ExecuteResponseArgs:params (LinkSignerParams): Parameters for linking a signer to a subaccount.Returns:ExecuteResponse: Execution response from the engine.Raises:Exception: If there is an error during the execution or the response status is not “success”.

Links a signer to a subaccount to allow them to sign transactions on behalf of the subaccount.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (LinkSignerParams): Parameters for linking a signer to a subaccount.

params (LinkSignerParams): Parameters for linking a signer to a subaccount.

**Returns:**
  ExecuteResponse: Execution response from the engine.

ExecuteResponse: Execution response from the engine.

**Raises:**
  Exception: If there is an error during the execution or the response status is not “success”.

Exception: If there is an error during the execution or the response status is not “success”.

**classnado_protocol.client.apis.SubaccountQueryAPI(context)[source]**
  Bases:NadoBaseAPIProvides functionalities for querying data related to subaccounts in the Nado Protocol.Inherits from NadoBaseAPI, which provides a basic context setup for accessing Nado Clearinghouse.
This class extends the base class to provide specific functionalities for querying data related to subaccounts.Attributes:context (NadoClientContext): Provides connectivity details for accessing Nado APIs.get_engine_subaccount_summary(subaccount,txs=None)[source]Retrieve a comprehensive summary of the specified subaccount’s state as per the off-chain engine.You can optionally provide a list of txs to get an estimated view of your subaccount.Return type:SubaccountInfoDataArgs:subaccount (str): Unique identifier for the subaccount.txs (list[QuerySubaccountInfoTx], optional): Optional list of transactions for the subaccount.Returns:SubaccountInfoData: A data class object containing detailed state information about the queried subaccount.get_subaccount_fee_rates(subaccount)[source]Retrieve the fee rates associated with a specific subaccount from the off-chain engine.Return type:FeeRatesDataArgs:subaccount (str): Unique identifier for the subaccount.Returns:FeeRatesData: A data class object containing detailed fee rates data for the specified subaccount.get_subaccount_linked_signer_rate_limits(subaccount)[source]Retrieve the current linked signer and their rate limit for a specified subaccount from the indexer.Return type:IndexerLinkedSignerRateLimitDataArgs:subaccount (str): Unique identifier for the subaccount.Returns:IndexerLinkedSignerRateLimitData: A data class object containing information about the current linked signer and their rate limits for the queried subaccount.get_subaccounts(address=None,start_idx=None,limit=None)[source]List nado subaccounts via the indexer.Return type:IndexerSubaccountsDataArgs:address (Optional[str]): An optional wallet address to find all subaccounts associated to it.
start_idx (Optional[int]): Optional subaccount id to start from. Used for pagination. Defaults to 0.
limit (Optional[int]): Maximum number of subaccounts to return. Defaults to 100. Max of 500.Returns:IndexerSubaccountsData: A data class object containing the list of subaccounts found.get_interest_and_funding_payments(subaccount,product_ids,limit,max_idx=None)[source]List interests and funding payments for a subaccount and provided products from the indexer.Return type:IndexerInterestAndFundingDataArgs:subaccount (str): Subaccount to fetch interest / funding payments for.
product_ids (list[int]): List of product IDs to fetch interest / funding payments for.
limit (int): Max number of records to return. Max possible of 100.
max_idx (Optional[int]): When provided, only return records with idx <= max_idx. Used for pagination.Returns:IndexerInterestAndFundingData: A data class object containing the list of interest / funding payments found.

Bases:NadoBaseAPI

Provides functionalities for querying data related to subaccounts in the Nado Protocol.

Inherits from NadoBaseAPI, which provides a basic context setup for accessing Nado Clearinghouse.
This class extends the base class to provide specific functionalities for querying data related to subaccounts.

**Attributes:**
  context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

**get_engine_subaccount_summary(subaccount,txs=None)[source]**
  Retrieve a comprehensive summary of the specified subaccount’s state as per the off-chain engine.You can optionally provide a list of txs to get an estimated view of your subaccount.Return type:SubaccountInfoDataArgs:subaccount (str): Unique identifier for the subaccount.txs (list[QuerySubaccountInfoTx], optional): Optional list of transactions for the subaccount.Returns:SubaccountInfoData: A data class object containing detailed state information about the queried subaccount.

Retrieve a comprehensive summary of the specified subaccount’s state as per the off-chain engine.

You can optionally provide a list of txs to get an estimated view of your subaccount.

**Return type:**
  SubaccountInfoData

SubaccountInfoData

**Args:**
  subaccount (str): Unique identifier for the subaccount.txs (list[QuerySubaccountInfoTx], optional): Optional list of transactions for the subaccount.

subaccount (str): Unique identifier for the subaccount.

txs (list[QuerySubaccountInfoTx], optional): Optional list of transactions for the subaccount.

**Returns:**
  SubaccountInfoData: A data class object containing detailed state information about the queried subaccount.

SubaccountInfoData: A data class object containing detailed state information about the queried subaccount.

**get_subaccount_fee_rates(subaccount)[source]**
  Retrieve the fee rates associated with a specific subaccount from the off-chain engine.Return type:FeeRatesDataArgs:subaccount (str): Unique identifier for the subaccount.Returns:FeeRatesData: A data class object containing detailed fee rates data for the specified subaccount.

Retrieve the fee rates associated with a specific subaccount from the off-chain engine.

**Return type:**
  FeeRatesData

FeeRatesData

**Args:**
  subaccount (str): Unique identifier for the subaccount.

subaccount (str): Unique identifier for the subaccount.

**Returns:**
  FeeRatesData: A data class object containing detailed fee rates data for the specified subaccount.

FeeRatesData: A data class object containing detailed fee rates data for the specified subaccount.

**get_subaccount_linked_signer_rate_limits(subaccount)[source]**
  Retrieve the current linked signer and their rate limit for a specified subaccount from the indexer.Return type:IndexerLinkedSignerRateLimitDataArgs:subaccount (str): Unique identifier for the subaccount.Returns:IndexerLinkedSignerRateLimitData: A data class object containing information about the current linked signer and their rate limits for the queried subaccount.

Retrieve the current linked signer and their rate limit for a specified subaccount from the indexer.

**Return type:**
  IndexerLinkedSignerRateLimitData

IndexerLinkedSignerRateLimitData

**Args:**
  subaccount (str): Unique identifier for the subaccount.

subaccount (str): Unique identifier for the subaccount.

**Returns:**
  IndexerLinkedSignerRateLimitData: A data class object containing information about the current linked signer and their rate limits for the queried subaccount.

IndexerLinkedSignerRateLimitData: A data class object containing information about the current linked signer and their rate limits for the queried subaccount.

**get_subaccounts(address=None,start_idx=None,limit=None)[source]**
  List nado subaccounts via the indexer.Return type:IndexerSubaccountsDataArgs:address (Optional[str]): An optional wallet address to find all subaccounts associated to it.
start_idx (Optional[int]): Optional subaccount id to start from. Used for pagination. Defaults to 0.
limit (Optional[int]): Maximum number of subaccounts to return. Defaults to 100. Max of 500.Returns:IndexerSubaccountsData: A data class object containing the list of subaccounts found.

List nado subaccounts via the indexer.

**Return type:**
  IndexerSubaccountsData

IndexerSubaccountsData

**Args:**
  address (Optional[str]): An optional wallet address to find all subaccounts associated to it.
start_idx (Optional[int]): Optional subaccount id to start from. Used for pagination. Defaults to 0.
limit (Optional[int]): Maximum number of subaccounts to return. Defaults to 100. Max of 500.

address (Optional[str]): An optional wallet address to find all subaccounts associated to it.
start_idx (Optional[int]): Optional subaccount id to start from. Used for pagination. Defaults to 0.
limit (Optional[int]): Maximum number of subaccounts to return. Defaults to 100. Max of 500.

**Returns:**
  IndexerSubaccountsData: A data class object containing the list of subaccounts found.

IndexerSubaccountsData: A data class object containing the list of subaccounts found.

**get_interest_and_funding_payments(subaccount,product_ids,limit,max_idx=None)[source]**
  List interests and funding payments for a subaccount and provided products from the indexer.Return type:IndexerInterestAndFundingDataArgs:subaccount (str): Subaccount to fetch interest / funding payments for.
product_ids (list[int]): List of product IDs to fetch interest / funding payments for.
limit (int): Max number of records to return. Max possible of 100.
max_idx (Optional[int]): When provided, only return records with idx <= max_idx. Used for pagination.Returns:IndexerInterestAndFundingData: A data class object containing the list of interest / funding payments found.

List interests and funding payments for a subaccount and provided products from the indexer.

**Return type:**
  IndexerInterestAndFundingData

IndexerInterestAndFundingData

**Args:**
  subaccount (str): Subaccount to fetch interest / funding payments for.
product_ids (list[int]): List of product IDs to fetch interest / funding payments for.
limit (int): Max number of records to return. Max possible of 100.
max_idx (Optional[int]): When provided, only return records with idx <= max_idx. Used for pagination.

subaccount (str): Subaccount to fetch interest / funding payments for.
product_ids (list[int]): List of product IDs to fetch interest / funding payments for.
limit (int): Max number of records to return. Max possible of 100.
max_idx (Optional[int]): When provided, only return records with idx <= max_idx. Used for pagination.

**Returns:**
  IndexerInterestAndFundingData: A data class object containing the list of interest / funding payments found.

IndexerInterestAndFundingData: A data class object containing the list of interest / funding payments found.

**classnado_protocol.client.apis.PerpAPI(context)[source]**
  Bases:PerpQueryAPIA unified interface for Perpetual (Perp) operations in the Nado Protocol.This class extends functionalities from PerpQueryAPI into a single interface, providing a simpler and more consistent way to perform Perp operations.
Currently, it allows for querying (data retrieval) operations for Perp products.Inheritance:PerpQueryAPI: This provides functionalities to retrieve various kinds of information related to Perp products.
These include operations like retrieving the latest index and mark price for a specific Perp product.Attributes and Methods: Inherited from PerpQueryAPI.

Bases:PerpQueryAPI

A unified interface for Perpetual (Perp) operations in the Nado Protocol.

This class extends functionalities from PerpQueryAPI into a single interface, providing a simpler and more consistent way to perform Perp operations.
Currently, it allows for querying (data retrieval) operations for Perp products.

**Inheritance:**
  PerpQueryAPI: This provides functionalities to retrieve various kinds of information related to Perp products.
These include operations like retrieving the latest index and mark price for a specific Perp product.

PerpQueryAPI: This provides functionalities to retrieve various kinds of information related to Perp products.
These include operations like retrieving the latest index and mark price for a specific Perp product.

Attributes and Methods: Inherited from PerpQueryAPI.

**classnado_protocol.client.apis.PerpQueryAPI(context)[source]**
  Bases:NadoBaseAPIProvides functionalities for querying data related to Perpetual (Perp) products in the Nado Protocol.Inherits from NadoBaseAPI, which provides a basic context setup for accessing Nado.
This class extends the base class to provide specific functionalities for querying data related to Perp products.Attributes:context (NadoClientContext): Provides connectivity details for accessing Nado APIs.get_prices(product_id)[source]Retrieves the latest index and mark price for a specific perp product from the indexer.Return type:IndexerPerpPricesDataArgs:product_id (int): The identifier for the perp product.Returns:IndexerPerpPricesData: An object containing the latest index and mark price for the specified product.product_id (int): The identifier for the perp product.index_price_x18 (str): The latest index price for the product, scaled by 1e18.mark_price_x18 (str): The latest mark price for the product, scaled by 1e18.update_time (str): The timestamp of the last price update.

Bases:NadoBaseAPI

Provides functionalities for querying data related to Perpetual (Perp) products in the Nado Protocol.

Inherits from NadoBaseAPI, which provides a basic context setup for accessing Nado.
This class extends the base class to provide specific functionalities for querying data related to Perp products.

**Attributes:**
  context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

context (NadoClientContext): Provides connectivity details for accessing Nado APIs.

**get_prices(product_id)[source]**
  Retrieves the latest index and mark price for a specific perp product from the indexer.Return type:IndexerPerpPricesDataArgs:product_id (int): The identifier for the perp product.Returns:IndexerPerpPricesData: An object containing the latest index and mark price for the specified product.product_id (int): The identifier for the perp product.index_price_x18 (str): The latest index price for the product, scaled by 1e18.mark_price_x18 (str): The latest mark price for the product, scaled by 1e18.update_time (str): The timestamp of the last price update.

Retrieves the latest index and mark price for a specific perp product from the indexer.

**Return type:**
  IndexerPerpPricesData

IndexerPerpPricesData

**Args:**
  product_id (int): The identifier for the perp product.

product_id (int): The identifier for the perp product.

**Returns:**
  IndexerPerpPricesData: An object containing the latest index and mark price for the specified product.product_id (int): The identifier for the perp product.index_price_x18 (str): The latest index price for the product, scaled by 1e18.mark_price_x18 (str): The latest mark price for the product, scaled by 1e18.update_time (str): The timestamp of the last price update.

**IndexerPerpPricesData: An object containing the latest index and mark price for the specified product.**
  product_id (int): The identifier for the perp product.index_price_x18 (str): The latest index price for the product, scaled by 1e18.mark_price_x18 (str): The latest mark price for the product, scaled by 1e18.update_time (str): The timestamp of the last price update.
- product_id (int): The identifier for the perp product.

product_id (int): The identifier for the perp product.

- index_price_x18 (str): The latest index price for the product, scaled by 1e18.

index_price_x18 (str): The latest index price for the product, scaled by 1e18.

- mark_price_x18 (str): The latest mark price for the product, scaled by 1e18.

mark_price_x18 (str): The latest mark price for the product, scaled by 1e18.

- update_time (str): The timestamp of the last price update.

update_time (str): The timestamp of the last price update.

**classnado_protocol.client.apis.RewardsAPI(context)[source]**
  Bases:RewardsExecuteAPI,RewardsQueryAPI

Bases:RewardsExecuteAPI,RewardsQueryAPI

**classnado_protocol.client.apis.RewardsExecuteAPI(context)[source]**
  Bases:NadoBaseAPIclaim(params,signer=None)[source]Return type:strclaim_and_stake(params,signer=None)[source]Return type:strstake(amount,signer=None)[source]Return type:strunstake(amount,signer=None)[source]Return type:strwithdraw_unstaked(signer=None)[source]claim_usdc_rewards(signer=None)[source]claim_and_stake_usdc_rewards(signer=None)[source]claim_foundation_rewards(signer=None)[source]Claims all available foundation rewards. Foundation rewards are tokens associated with the chain. For example, ARB on Arbitrum.

Bases:NadoBaseAPI

**claim(params,signer=None)[source]**
  Return type:str

**Return type:**
  str

str

**claim_and_stake(params,signer=None)[source]**
  Return type:str

**Return type:**
  str

str

**stake(amount,signer=None)[source]**
  Return type:str

**Return type:**
  str

str

**unstake(amount,signer=None)[source]**
  Return type:str

**Return type:**
  str

str

**withdraw_unstaked(signer=None)[source]**

**claim_usdc_rewards(signer=None)[source]**

**claim_and_stake_usdc_rewards(signer=None)[source]**

**claim_foundation_rewards(signer=None)[source]**
  Claims all available foundation rewards. Foundation rewards are tokens associated with the chain. For example, ARB on Arbitrum.

Claims all available foundation rewards. Foundation rewards are tokens associated with the chain. For example, ARB on Arbitrum.

**classnado_protocol.client.apis.RewardsQueryAPI(context)[source]**
  Bases:NadoBaseAPIget_claim_and_stake_estimated_tokens(wallet)[source]Estimates the amount of USDC -> TOKEN swap when claiming + staking USDC rewardsReturn type:int

Bases:NadoBaseAPI

**get_claim_and_stake_estimated_tokens(wallet)[source]**
  Estimates the amount of USDC -> TOKEN swap when claiming + staking USDC rewardsReturn type:int

Estimates the amount of USDC -> TOKEN swap when claiming + staking USDC rewards

**Return type:**
  int

int

## nado-protocol.engine_client

**classnado_protocol.engine_client.EngineClient(opts)[source]**
  Bases:EngineQueryClient,EngineExecuteClientClient for interacting with the engine service.It allows users to both query data from and execute commands on the engine service.Attributes:opts (EngineClientOpts): Client configuration options for connecting and interacting with the engine service.Methods:__init__: Initializes theEngineClientwith the provided options.__init__(opts)[source]Initializes the EngineClient with the provided options.Args:opts (EngineClientOpts): Client configuration options for connecting and interacting with the engine service.

Bases:EngineQueryClient,EngineExecuteClient

Client for interacting with the engine service.

It allows users to both query data from and execute commands on the engine service.

**Attributes:**
  opts (EngineClientOpts): Client configuration options for connecting and interacting with the engine service.

opts (EngineClientOpts): Client configuration options for connecting and interacting with the engine service.

**Methods:**
  __init__: Initializes theEngineClientwith the provided options.

__init__: Initializes theEngineClientwith the provided options.

**__init__(opts)[source]**
  Initializes the EngineClient with the provided options.Args:opts (EngineClientOpts): Client configuration options for connecting and interacting with the engine service.

Initializes the EngineClient with the provided options.

**Args:**
  opts (EngineClientOpts): Client configuration options for connecting and interacting with the engine service.

opts (EngineClientOpts): Client configuration options for connecting and interacting with the engine service.

**classnado_protocol.engine_client.EngineClientOpts(**data)[source]**
  Bases:NadoClientOptsModel defining the configuration options for the Engine Client.

Bases:NadoClientOpts

Model defining the configuration options for the Engine Client.

**classnado_protocol.engine_client.EngineExecuteClient(opts,querier=None)[source]**
  Bases:NadoBaseExecuteClient class for executing operations against the off-chain engine.__init__(opts,querier=None)[source]Initialize the EngineExecuteClient with provided options.Args:opts (EngineClientOpts): Options for the client.querier (EngineQueryClient, optional): An EngineQueryClient instance. If not provided, a new one is created.tx_nonce(sender)[source]Get the transaction nonce. Used to perform executes such aswithdraw_collateral.Return type:intReturns:int: The transaction nonce.execute(params)[source]Executes the operation defined by the provided parameters.Return type:ExecuteResponseArgs:params (ExecuteParams): The parameters for the operation to execute. This can represent a variety of operations, such as placing orders, cancelling orders, and more.Returns:ExecuteResponse: The response from the executed operation.place_order(params)[source]Execute a place order operation.Return type:ExecuteResponseArgs:params (PlaceOrderParams): Parameters required for placing an order.
The parameters include the order details and the product_id.Returns:ExecuteResponse: Response of the execution, including status and potential error message.place_market_order(params)[source]Places an FOK order using top of the book price with provided slippage.Return type:ExecuteResponseArgs:params (PlaceMarketOrderParams): Parameters required for placing a market order.Returns:ExecuteResponse: Response of the execution, including status and potential error message.cancel_orders(params)[source]Execute a cancel orders operation.Return type:ExecuteResponseArgs:params (CancelOrdersParams): Parameters required for canceling orders.
The parameters include the order digests to be cancelled.Returns:ExecuteResponse: Response of the execution, including status and potential error message.cancel_product_orders(params)[source]Execute a cancel product orders operation.Return type:ExecuteResponseArgs:params (CancelProductOrdersParams): Parameters required for bulk canceling orders of specific products.
The parameters include a list of product ids to bulk cancel orders for.Returns:ExecuteResponse: Response of the execution, including status and potential error message.cancel_and_place(params)[source]Execute a cancel and place operation.Return type:ExecuteResponseArgs:params (CancelAndPlaceParams): Parameters required for cancel and place.Returns:ExecuteResponse: Response of the execution, including status and potential error message.withdraw_collateral(params)[source]Execute a withdraw collateral operation.Return type:ExecuteResponseArgs:params (WithdrawCollateralParams): Parameters required for withdrawing collateral.
The parameters include the collateral details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.liquidate_subaccount(params)[source]Execute a liquidate subaccount operation.Return type:ExecuteResponseArgs:params (LiquidateSubaccountParams): Parameters required for liquidating a subaccount.
The parameters include the liquidatee details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.mint_nlp(params)[source]Execute a mint NLP tokens operation.Return type:ExecuteResponseArgs:params (MintNlpParams): Parameters required for minting NLP tokens.
The parameters include the LP details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.burn_nlp(params)[source]Execute a burn NLP tokens operation.Return type:ExecuteResponseArgs:params (BurnNlpParams): Parameters required for burning LP tokens.
The parameters include the LP details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.link_signer(params)[source]Execute a link signer operation.Return type:ExecuteResponseArgs:params (LinkSignerParams): Parameters required for linking a signer.
The parameters include the signer details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.close_position(subaccount,product_id)[source]Execute a place order operation to close a position for the providedproduct_id.Return type:ExecuteResponseAttributes:subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Bases:NadoBaseExecute

Client class for executing operations against the off-chain engine.

**__init__(opts,querier=None)[source]**
  Initialize the EngineExecuteClient with provided options.Args:opts (EngineClientOpts): Options for the client.querier (EngineQueryClient, optional): An EngineQueryClient instance. If not provided, a new one is created.

Initialize the EngineExecuteClient with provided options.

**Args:**
  opts (EngineClientOpts): Options for the client.querier (EngineQueryClient, optional): An EngineQueryClient instance. If not provided, a new one is created.

opts (EngineClientOpts): Options for the client.

querier (EngineQueryClient, optional): An EngineQueryClient instance. If not provided, a new one is created.

**tx_nonce(sender)[source]**
  Get the transaction nonce. Used to perform executes such aswithdraw_collateral.Return type:intReturns:int: The transaction nonce.

Get the transaction nonce. Used to perform executes such aswithdraw_collateral.

**Return type:**
  int

int

**Returns:**
  int: The transaction nonce.

int: The transaction nonce.

**execute(params)[source]**
  Executes the operation defined by the provided parameters.Return type:ExecuteResponseArgs:params (ExecuteParams): The parameters for the operation to execute. This can represent a variety of operations, such as placing orders, cancelling orders, and more.Returns:ExecuteResponse: The response from the executed operation.

Executes the operation defined by the provided parameters.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (ExecuteParams): The parameters for the operation to execute. This can represent a variety of operations, such as placing orders, cancelling orders, and more.

params (ExecuteParams): The parameters for the operation to execute. This can represent a variety of operations, such as placing orders, cancelling orders, and more.

**Returns:**
  ExecuteResponse: The response from the executed operation.

ExecuteResponse: The response from the executed operation.

**place_order(params)[source]**
  Execute a place order operation.Return type:ExecuteResponseArgs:params (PlaceOrderParams): Parameters required for placing an order.
The parameters include the order details and the product_id.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a place order operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (PlaceOrderParams): Parameters required for placing an order.
The parameters include the order details and the product_id.

params (PlaceOrderParams): Parameters required for placing an order.
The parameters include the order details and the product_id.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**place_market_order(params)[source]**
  Places an FOK order using top of the book price with provided slippage.Return type:ExecuteResponseArgs:params (PlaceMarketOrderParams): Parameters required for placing a market order.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Places an FOK order using top of the book price with provided slippage.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (PlaceMarketOrderParams): Parameters required for placing a market order.

params (PlaceMarketOrderParams): Parameters required for placing a market order.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**cancel_orders(params)[source]**
  Execute a cancel orders operation.Return type:ExecuteResponseArgs:params (CancelOrdersParams): Parameters required for canceling orders.
The parameters include the order digests to be cancelled.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a cancel orders operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (CancelOrdersParams): Parameters required for canceling orders.
The parameters include the order digests to be cancelled.

params (CancelOrdersParams): Parameters required for canceling orders.
The parameters include the order digests to be cancelled.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**cancel_product_orders(params)[source]**
  Execute a cancel product orders operation.Return type:ExecuteResponseArgs:params (CancelProductOrdersParams): Parameters required for bulk canceling orders of specific products.
The parameters include a list of product ids to bulk cancel orders for.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a cancel product orders operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (CancelProductOrdersParams): Parameters required for bulk canceling orders of specific products.
The parameters include a list of product ids to bulk cancel orders for.

params (CancelProductOrdersParams): Parameters required for bulk canceling orders of specific products.
The parameters include a list of product ids to bulk cancel orders for.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**cancel_and_place(params)[source]**
  Execute a cancel and place operation.Return type:ExecuteResponseArgs:params (CancelAndPlaceParams): Parameters required for cancel and place.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a cancel and place operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (CancelAndPlaceParams): Parameters required for cancel and place.

params (CancelAndPlaceParams): Parameters required for cancel and place.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**withdraw_collateral(params)[source]**
  Execute a withdraw collateral operation.Return type:ExecuteResponseArgs:params (WithdrawCollateralParams): Parameters required for withdrawing collateral.
The parameters include the collateral details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a withdraw collateral operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (WithdrawCollateralParams): Parameters required for withdrawing collateral.
The parameters include the collateral details.

params (WithdrawCollateralParams): Parameters required for withdrawing collateral.
The parameters include the collateral details.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**liquidate_subaccount(params)[source]**
  Execute a liquidate subaccount operation.Return type:ExecuteResponseArgs:params (LiquidateSubaccountParams): Parameters required for liquidating a subaccount.
The parameters include the liquidatee details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a liquidate subaccount operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (LiquidateSubaccountParams): Parameters required for liquidating a subaccount.
The parameters include the liquidatee details.

params (LiquidateSubaccountParams): Parameters required for liquidating a subaccount.
The parameters include the liquidatee details.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**mint_nlp(params)[source]**
  Execute a mint NLP tokens operation.Return type:ExecuteResponseArgs:params (MintNlpParams): Parameters required for minting NLP tokens.
The parameters include the LP details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a mint NLP tokens operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (MintNlpParams): Parameters required for minting NLP tokens.
The parameters include the LP details.

params (MintNlpParams): Parameters required for minting NLP tokens.
The parameters include the LP details.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**burn_nlp(params)[source]**
  Execute a burn NLP tokens operation.Return type:ExecuteResponseArgs:params (BurnNlpParams): Parameters required for burning LP tokens.
The parameters include the LP details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a burn NLP tokens operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (BurnNlpParams): Parameters required for burning LP tokens.
The parameters include the LP details.

params (BurnNlpParams): Parameters required for burning LP tokens.
The parameters include the LP details.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**link_signer(params)[source]**
  Execute a link signer operation.Return type:ExecuteResponseArgs:params (LinkSignerParams): Parameters required for linking a signer.
The parameters include the signer details.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a link signer operation.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Args:**
  params (LinkSignerParams): Parameters required for linking a signer.
The parameters include the signer details.

params (LinkSignerParams): Parameters required for linking a signer.
The parameters include the signer details.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**close_position(subaccount,product_id)[source]**
  Execute a place order operation to close a position for the providedproduct_id.Return type:ExecuteResponseAttributes:subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.Returns:ExecuteResponse: Response of the execution, including status and potential error message.

Execute a place order operation to close a position for the providedproduct_id.

**Return type:**
  ExecuteResponse

ExecuteResponse

**Attributes:**
  subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.

subaccount (Subaccount): The subaccount to close position for.
product_id (int): The ID of the product to close position for.

**Returns:**
  ExecuteResponse: Response of the execution, including status and potential error message.

ExecuteResponse: Response of the execution, including status and potential error message.

**classnado_protocol.engine_client.EngineQueryClient(opts)[source]**
  Bases:objectClient class for querying the off-chain engine.__init__(opts)[source]Initialize EngineQueryClient with provided options.Args:opts (EngineClientOpts): Options for the client.query(req)[source]Send a query to the engine.Return type:QueryResponseArgs:req (QueryRequest): The query request parameters.Returns:QueryResponse: The response from the engine.Raises:BadStatusCodeException: If the response status code is not 200.
QueryFailedException: If the query status is not “success”.get_product_symbols()[source]Retrieves symbols for all available products.Return type:list[ProductSymbol]Returns:ProductSymbolsData: Symbols for all available products.get_status()[source]Query the engine for its status.Return type:EngineStatusReturns:StatusData: The status of the engine.get_contracts()[source]Query the engine for Nado contract addresses.Use this to fetch verifying contracts needed for signing executes.Return type:ContractsDataReturns:ContractsData: Nado contracts info.get_nonces(address)[source]Query the engine for nonces of a specific address.Return type:NoncesDataArgs:address (str): Wallet address to fetch nonces for.Returns:NoncesData: The nonces of the address.get_order(product_id,digest)[source]Query the engine for an order with a specific product id and digest.Return type:OrderDataArgs:product_id (int): The id of the product.digest (str): The digest of the order.Returns:OrderData: The order data.get_subaccount_info(subaccount,txs=None,pre_state=None)[source]Query the engine for the state of a subaccount, including balances.Return type:SubaccountInfoDataArgs:subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.txs (list[QuerySubaccountInfoTx], optional): You can optionally provide a list of txs, to get an estimated view
of what the subaccount state would look like if the transactions were applied.pre_state (bool, optional): When True and txs are provided, returns the subaccount state before the
transactions were applied in the pre_state field. Defaults to False.Returns:SubaccountInfoData: Information about the specified subaccount.get_subaccount_open_orders(product_id,sender)[source]Retrieves the open orders for a subaccount on a specific product.Return type:SubaccountOpenOrdersDataArgs:product_id (int): The identifier of the product for which open orders are to be fetched.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:SubaccountOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.get_subaccount_multi_products_open_orders(product_ids,sender)[source]Retrieves the open orders for a subaccount on a specific product.Return type:SubaccountMultiProductsOpenOrdersDataArgs:product_ids (list[int]): List of product ids to fetch open orders for.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:SubaccountMultiProductsOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.get_market_liquidity(product_id,depth)[source]Query the engine for market liquidity data for a specific product.Return type:MarketLiquidityDataArgs:product_id (int): The id of the product.depth (int): The depth of the market.Returns:MarketLiquidityData: Market liquidity data for the specified product.get_symbols(product_type=None,product_ids=None)[source]Query engine for symbols and product infoReturn type:SymbolsDataArgs:product_type (Optional[str): “spot” or “perp” productsproduct_ids (Optional[list[int]]): product_ids to return info forget_all_products()[source]Retrieves info about all available products,
including: product id, oracle price, configuration, state, etc.Return type:AllProductsDataReturns:AllProductsData: Data about all products.get_market_price(product_id)[source]Retrieves the highest bid and lowest ask price levels
from the orderbook for a given product.Return type:MarketPriceDataArgs:product_id (int): The id of the product.Returns:MarketPriceData: Market price data for the specified product.get_max_order_size(params)[source]Retrieves the maximum order size of a given product for a specified subaccount.Return type:MaxOrderSizeDataArgs:params (QueryMaxOrderSizeParams): The parameters object that contains
the details of the subaccount and product for which the max order size is to be fetched.Returns:MaxOrderSizeData: A data object containing the maximum order size possible
for the given subaccount and product.get_max_withdrawable(product_id,sender,spot_leverage=None)[source]Retrieves the maximum withdrawable amount for a given spot product for a subaccount.Return type:MaxWithdrawableDataArgs:product_id (int): ID of the spot product.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.spot_leverage (bool, optional): If False, calculates without borrowing. Defaults to True.Returns:MaxWithdrawableData: Contains the maximum withdrawable amount.get_max_nlp_mintable(product_id,sender,spot_leverage=None)[source]Retrieves the maximum LP token amount mintable for a given product for a subaccount.Return type:MaxLpMintableDataArgs:product_id (int): ID of the product.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.spot_leverage (bool, optional): If False, calculates without considering borrowing. Defaults to True.Returns:MaxLpMintableData: Contains the maximum LP token mintable amount.get_fee_rates(sender)[source]Retrieves the fee rates associated with a specific subaccount.Return type:FeeRatesDataArgs:sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:FeeRatesData: Contains fee rates information associated with the subaccount.get_health_groups()[source]Retrieves all available health groups. A health group represents a set of perp
and spot products whose health is calculated together, such as BTC
and BTC-PERP.Return type:HealthGroupsDataReturns:HealthGroupsData: Contains health group information, each including both a spot
and a perp product.get_linked_signer(subaccount)[source]Retrieves the current linked signer for the specified subaccount.Return type:LinkedSignerDataArgs:subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:LinkedSignerData: Information about the currently linked signer for the subaccount.get_isolated_positions(subaccount)[source]Retrieves the isolated positions for a specific subaccount.Return type:IsolatedPositionsDataArgs:subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:IsolatedPositionsData: A data object containing the isolated positions for the specified subaccount.get_assets()[source]Return type:list[Asset]get_pairs(market_type=None)[source]Return type:list[MarketPair]get_spots_apr()[source]Return type:list[SpotApr]get_orderbook(ticker_id,depth)[source]Return type:Orderbook

Bases:object

Client class for querying the off-chain engine.

**__init__(opts)[source]**
  Initialize EngineQueryClient with provided options.Args:opts (EngineClientOpts): Options for the client.

Initialize EngineQueryClient with provided options.

**Args:**
  opts (EngineClientOpts): Options for the client.

opts (EngineClientOpts): Options for the client.

**query(req)[source]**
  Send a query to the engine.Return type:QueryResponseArgs:req (QueryRequest): The query request parameters.Returns:QueryResponse: The response from the engine.Raises:BadStatusCodeException: If the response status code is not 200.
QueryFailedException: If the query status is not “success”.

Send a query to the engine.

**Return type:**
  QueryResponse

QueryResponse

**Args:**
  req (QueryRequest): The query request parameters.

req (QueryRequest): The query request parameters.

**Returns:**
  QueryResponse: The response from the engine.

QueryResponse: The response from the engine.

**Raises:**
  BadStatusCodeException: If the response status code is not 200.
QueryFailedException: If the query status is not “success”.

BadStatusCodeException: If the response status code is not 200.
QueryFailedException: If the query status is not “success”.

**get_product_symbols()[source]**
  Retrieves symbols for all available products.Return type:list[ProductSymbol]Returns:ProductSymbolsData: Symbols for all available products.

Retrieves symbols for all available products.

**Return type:**
  list[ProductSymbol]

list[ProductSymbol]

**Returns:**
  ProductSymbolsData: Symbols for all available products.

ProductSymbolsData: Symbols for all available products.

**get_status()[source]**
  Query the engine for its status.Return type:EngineStatusReturns:StatusData: The status of the engine.

Query the engine for its status.

**Return type:**
  EngineStatus

EngineStatus

**Returns:**
  StatusData: The status of the engine.

StatusData: The status of the engine.

**get_contracts()[source]**
  Query the engine for Nado contract addresses.Use this to fetch verifying contracts needed for signing executes.Return type:ContractsDataReturns:ContractsData: Nado contracts info.

Query the engine for Nado contract addresses.

Use this to fetch verifying contracts needed for signing executes.

**Return type:**
  ContractsData

ContractsData

**Returns:**
  ContractsData: Nado contracts info.

ContractsData: Nado contracts info.

**get_nonces(address)[source]**
  Query the engine for nonces of a specific address.Return type:NoncesDataArgs:address (str): Wallet address to fetch nonces for.Returns:NoncesData: The nonces of the address.

Query the engine for nonces of a specific address.

**Return type:**
  NoncesData

NoncesData

**Args:**
  address (str): Wallet address to fetch nonces for.

address (str): Wallet address to fetch nonces for.

**Returns:**
  NoncesData: The nonces of the address.

NoncesData: The nonces of the address.

**get_order(product_id,digest)[source]**
  Query the engine for an order with a specific product id and digest.Return type:OrderDataArgs:product_id (int): The id of the product.digest (str): The digest of the order.Returns:OrderData: The order data.

Query the engine for an order with a specific product id and digest.

**Return type:**
  OrderData

OrderData

**Args:**
  product_id (int): The id of the product.digest (str): The digest of the order.

product_id (int): The id of the product.

digest (str): The digest of the order.

**Returns:**
  OrderData: The order data.

OrderData: The order data.

**get_subaccount_info(subaccount,txs=None,pre_state=None)[source]**
  Query the engine for the state of a subaccount, including balances.Return type:SubaccountInfoDataArgs:subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.txs (list[QuerySubaccountInfoTx], optional): You can optionally provide a list of txs, to get an estimated view
of what the subaccount state would look like if the transactions were applied.pre_state (bool, optional): When True and txs are provided, returns the subaccount state before the
transactions were applied in the pre_state field. Defaults to False.Returns:SubaccountInfoData: Information about the specified subaccount.

Query the engine for the state of a subaccount, including balances.

**Return type:**
  SubaccountInfoData

SubaccountInfoData

**Args:**
  subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.txs (list[QuerySubaccountInfoTx], optional): You can optionally provide a list of txs, to get an estimated view
of what the subaccount state would look like if the transactions were applied.pre_state (bool, optional): When True and txs are provided, returns the subaccount state before the
transactions were applied in the pre_state field. Defaults to False.

subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

txs (list[QuerySubaccountInfoTx], optional): You can optionally provide a list of txs, to get an estimated view
of what the subaccount state would look like if the transactions were applied.

pre_state (bool, optional): When True and txs are provided, returns the subaccount state before the
transactions were applied in the pre_state field. Defaults to False.

**Returns:**
  SubaccountInfoData: Information about the specified subaccount.

SubaccountInfoData: Information about the specified subaccount.

**get_subaccount_open_orders(product_id,sender)[source]**
  Retrieves the open orders for a subaccount on a specific product.Return type:SubaccountOpenOrdersDataArgs:product_id (int): The identifier of the product for which open orders are to be fetched.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:SubaccountOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.

Retrieves the open orders for a subaccount on a specific product.

**Return type:**
  SubaccountOpenOrdersData

SubaccountOpenOrdersData

**Args:**
  product_id (int): The identifier of the product for which open orders are to be fetched.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

product_id (int): The identifier of the product for which open orders are to be fetched.

sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

**Returns:**
  SubaccountOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.

SubaccountOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.

**get_subaccount_multi_products_open_orders(product_ids,sender)[source]**
  Retrieves the open orders for a subaccount on a specific product.Return type:SubaccountMultiProductsOpenOrdersDataArgs:product_ids (list[int]): List of product ids to fetch open orders for.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:SubaccountMultiProductsOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.

Retrieves the open orders for a subaccount on a specific product.

**Return type:**
  SubaccountMultiProductsOpenOrdersData

SubaccountMultiProductsOpenOrdersData

**Args:**
  product_ids (list[int]): List of product ids to fetch open orders for.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

product_ids (list[int]): List of product ids to fetch open orders for.

sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

**Returns:**
  SubaccountMultiProductsOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.

SubaccountMultiProductsOpenOrdersData: A data object containing the open orders for the
specified subaccount on the provided product.

**get_market_liquidity(product_id,depth)[source]**
  Query the engine for market liquidity data for a specific product.Return type:MarketLiquidityDataArgs:product_id (int): The id of the product.depth (int): The depth of the market.Returns:MarketLiquidityData: Market liquidity data for the specified product.

Query the engine for market liquidity data for a specific product.

**Return type:**
  MarketLiquidityData

MarketLiquidityData

**Args:**
  product_id (int): The id of the product.depth (int): The depth of the market.

product_id (int): The id of the product.

depth (int): The depth of the market.

**Returns:**
  MarketLiquidityData: Market liquidity data for the specified product.

MarketLiquidityData: Market liquidity data for the specified product.

**get_symbols(product_type=None,product_ids=None)[source]**
  Query engine for symbols and product infoReturn type:SymbolsDataArgs:product_type (Optional[str): “spot” or “perp” productsproduct_ids (Optional[list[int]]): product_ids to return info for

Query engine for symbols and product info

**Return type:**
  SymbolsData

SymbolsData

**Args:**
  product_type (Optional[str): “spot” or “perp” productsproduct_ids (Optional[list[int]]): product_ids to return info for

product_type (Optional[str): “spot” or “perp” products

product_ids (Optional[list[int]]): product_ids to return info for

**get_all_products()[source]**
  Retrieves info about all available products,
including: product id, oracle price, configuration, state, etc.Return type:AllProductsDataReturns:AllProductsData: Data about all products.

Retrieves info about all available products,
including: product id, oracle price, configuration, state, etc.

**Return type:**
  AllProductsData

AllProductsData

**Returns:**
  AllProductsData: Data about all products.

AllProductsData: Data about all products.

**get_market_price(product_id)[source]**
  Retrieves the highest bid and lowest ask price levels
from the orderbook for a given product.Return type:MarketPriceDataArgs:product_id (int): The id of the product.Returns:MarketPriceData: Market price data for the specified product.

Retrieves the highest bid and lowest ask price levels
from the orderbook for a given product.

**Return type:**
  MarketPriceData

MarketPriceData

**Args:**
  product_id (int): The id of the product.

product_id (int): The id of the product.

**Returns:**
  MarketPriceData: Market price data for the specified product.

MarketPriceData: Market price data for the specified product.

**get_max_order_size(params)[source]**
  Retrieves the maximum order size of a given product for a specified subaccount.Return type:MaxOrderSizeDataArgs:params (QueryMaxOrderSizeParams): The parameters object that contains
the details of the subaccount and product for which the max order size is to be fetched.Returns:MaxOrderSizeData: A data object containing the maximum order size possible
for the given subaccount and product.

Retrieves the maximum order size of a given product for a specified subaccount.

**Return type:**
  MaxOrderSizeData

MaxOrderSizeData

**Args:**
  params (QueryMaxOrderSizeParams): The parameters object that contains
the details of the subaccount and product for which the max order size is to be fetched.

params (QueryMaxOrderSizeParams): The parameters object that contains
the details of the subaccount and product for which the max order size is to be fetched.

**Returns:**
  MaxOrderSizeData: A data object containing the maximum order size possible
for the given subaccount and product.

MaxOrderSizeData: A data object containing the maximum order size possible
for the given subaccount and product.

**get_max_withdrawable(product_id,sender,spot_leverage=None)[source]**
  Retrieves the maximum withdrawable amount for a given spot product for a subaccount.Return type:MaxWithdrawableDataArgs:product_id (int): ID of the spot product.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.spot_leverage (bool, optional): If False, calculates without borrowing. Defaults to True.Returns:MaxWithdrawableData: Contains the maximum withdrawable amount.

Retrieves the maximum withdrawable amount for a given spot product for a subaccount.

**Return type:**
  MaxWithdrawableData

MaxWithdrawableData

**Args:**
  product_id (int): ID of the spot product.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.spot_leverage (bool, optional): If False, calculates without borrowing. Defaults to True.

product_id (int): ID of the spot product.

sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

spot_leverage (bool, optional): If False, calculates without borrowing. Defaults to True.

**Returns:**
  MaxWithdrawableData: Contains the maximum withdrawable amount.

MaxWithdrawableData: Contains the maximum withdrawable amount.

**get_max_nlp_mintable(product_id,sender,spot_leverage=None)[source]**
  Retrieves the maximum LP token amount mintable for a given product for a subaccount.Return type:MaxLpMintableDataArgs:product_id (int): ID of the product.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.spot_leverage (bool, optional): If False, calculates without considering borrowing. Defaults to True.Returns:MaxLpMintableData: Contains the maximum LP token mintable amount.

Retrieves the maximum LP token amount mintable for a given product for a subaccount.

**Return type:**
  MaxLpMintableData

MaxLpMintableData

**Args:**
  product_id (int): ID of the product.sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.spot_leverage (bool, optional): If False, calculates without considering borrowing. Defaults to True.

product_id (int): ID of the product.

sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

spot_leverage (bool, optional): If False, calculates without considering borrowing. Defaults to True.

**Returns:**
  MaxLpMintableData: Contains the maximum LP token mintable amount.

MaxLpMintableData: Contains the maximum LP token mintable amount.

**get_fee_rates(sender)[source]**
  Retrieves the fee rates associated with a specific subaccount.Return type:FeeRatesDataArgs:sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:FeeRatesData: Contains fee rates information associated with the subaccount.

Retrieves the fee rates associated with a specific subaccount.

**Return type:**
  FeeRatesData

FeeRatesData

**Args:**
  sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

sender (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

**Returns:**
  FeeRatesData: Contains fee rates information associated with the subaccount.

FeeRatesData: Contains fee rates information associated with the subaccount.

**get_health_groups()[source]**
  Retrieves all available health groups. A health group represents a set of perp
and spot products whose health is calculated together, such as BTC
and BTC-PERP.Return type:HealthGroupsDataReturns:HealthGroupsData: Contains health group information, each including both a spot
and a perp product.

Retrieves all available health groups. A health group represents a set of perp
and spot products whose health is calculated together, such as BTC
and BTC-PERP.

**Return type:**
  HealthGroupsData

HealthGroupsData

**Returns:**
  HealthGroupsData: Contains health group information, each including both a spot
and a perp product.

HealthGroupsData: Contains health group information, each including both a spot
and a perp product.

**get_linked_signer(subaccount)[source]**
  Retrieves the current linked signer for the specified subaccount.Return type:LinkedSignerDataArgs:subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:LinkedSignerData: Information about the currently linked signer for the subaccount.

Retrieves the current linked signer for the specified subaccount.

**Return type:**
  LinkedSignerData

LinkedSignerData

**Args:**
  subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

**Returns:**
  LinkedSignerData: Information about the currently linked signer for the subaccount.

LinkedSignerData: Information about the currently linked signer for the subaccount.

**get_isolated_positions(subaccount)[source]**
  Retrieves the isolated positions for a specific subaccount.Return type:IsolatedPositionsDataArgs:subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.Returns:IsolatedPositionsData: A data object containing the isolated positions for the specified subaccount.

Retrieves the isolated positions for a specific subaccount.

**Return type:**
  IsolatedPositionsData

IsolatedPositionsData

**Args:**
  subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

subaccount (str): Identifier of the subaccount (owner’s address + subaccount name) sent as a hex string.

**Returns:**
  IsolatedPositionsData: A data object containing the isolated positions for the specified subaccount.

IsolatedPositionsData: A data object containing the isolated positions for the specified subaccount.

**get_assets()[source]**
  Return type:list[Asset]

**Return type:**
  list[Asset]

list[Asset]

**get_pairs(market_type=None)[source]**
  Return type:list[MarketPair]

**Return type:**
  list[MarketPair]

list[MarketPair]

**get_spots_apr()[source]**
  Return type:list[SpotApr]

**Return type:**
  list[SpotApr]

list[SpotApr]

**get_orderbook(ticker_id,depth)[source]**
  Return type:Orderbook

**Return type:**
  Orderbook

Orderbook

## nado-protocol.engine_client.types

**classnado_protocol.engine_client.types.SignatureParams(**data)[source]**
  Bases:NadoBaseModelClass for defining signature parameters in a request sent to the Nado API.Attributes:signature (Optional[str]): An optional string representing the signature for the request.signature:Optional[str]

Bases:NadoBaseModel

Class for defining signature parameters in a request sent to the Nado API.

**Attributes:**
  signature (Optional[str]): An optional string representing the signature for the request.

signature (Optional[str]): An optional string representing the signature for the request.

**signature:Optional[str]**

**classnado_protocol.engine_client.types.BaseParamsSigned(**data)[source]**
  Bases:BaseParams,SignatureParamsClass that combines the base parameters and signature parameters for a signed request
to the Nado API. Inherits attributes from BaseParams and SignatureParams.

Bases:BaseParams,SignatureParams

Class that combines the base parameters and signature parameters for a signed request
to the Nado API. Inherits attributes from BaseParams and SignatureParams.

**classnado_protocol.engine_client.types.OrderParams(**data)[source]**
  Bases:MarketOrderParamsClass for defining the parameters of an order.Attributes:priceX18 (int): The price of the order with a precision of 18 decimal places.expiration (int): The unix timestamp at which the order will expire.amount (int): The amount of the asset to be bought or sold in the order. Positive for alongposition and negative for ashort.nonce (Optional[int]): A unique number used to prevent replay attacks.appendix (int): Additional data or instructions related to the order. Use to encode order type and other related data.priceX18:intexpiration:intappendix:int

Bases:MarketOrderParams

Class for defining the parameters of an order.

**Attributes:**
  priceX18 (int): The price of the order with a precision of 18 decimal places.expiration (int): The unix timestamp at which the order will expire.amount (int): The amount of the asset to be bought or sold in the order. Positive for alongposition and negative for ashort.nonce (Optional[int]): A unique number used to prevent replay attacks.appendix (int): Additional data or instructions related to the order. Use to encode order type and other related data.

priceX18 (int): The price of the order with a precision of 18 decimal places.

expiration (int): The unix timestamp at which the order will expire.

amount (int): The amount of the asset to be bought or sold in the order. Positive for alongposition and negative for ashort.

nonce (Optional[int]): A unique number used to prevent replay attacks.

appendix (int): Additional data or instructions related to the order. Use to encode order type and other related data.

**priceX18:int**

**expiration:int**

**appendix:int**

**classnado_protocol.engine_client.types.PlaceOrderParams(**data)[source]**
  Bases:SignatureParamsClass for defining the parameters needed to place an order.Attributes:id (Optional[int]): An optional custom order id that is echoed back in subscription events e.g: fill orders, etc.product_id (int): The id of the product for which the order is being placed.order (OrderParams): The parameters of the order.digest (Optional[str]): An optional hash of the order data.spot_leverage (Optional[bool]): An optional flag indicating whether leverage should be used for the order. By default, leverage is assumed.id:Optional[int]product_id:intorder:OrderParamsdigest:Optional[str]spot_leverage:Optional[bool]

Bases:SignatureParams

Class for defining the parameters needed to place an order.

**Attributes:**
  id (Optional[int]): An optional custom order id that is echoed back in subscription events e.g: fill orders, etc.product_id (int): The id of the product for which the order is being placed.order (OrderParams): The parameters of the order.digest (Optional[str]): An optional hash of the order data.spot_leverage (Optional[bool]): An optional flag indicating whether leverage should be used for the order. By default, leverage is assumed.

id (Optional[int]): An optional custom order id that is echoed back in subscription events e.g: fill orders, etc.

product_id (int): The id of the product for which the order is being placed.

order (OrderParams): The parameters of the order.

digest (Optional[str]): An optional hash of the order data.

spot_leverage (Optional[bool]): An optional flag indicating whether leverage should be used for the order. By default, leverage is assumed.

**id:Optional[int]**

**product_id:int**

**order:OrderParams**

**digest:Optional[str]**

**spot_leverage:Optional[bool]**

**classnado_protocol.engine_client.types.CancelOrdersParams(**data)[source]**
  Bases:BaseParamsSignedParameters to cancel specific orders.Args:productIds (list[int]): List of product IDs for the orders to be canceled.digests (list[Digest]): List of digests of the orders to be canceled.nonce (Optional[int]): A unique number used to prevent replay attacks.Methods:serialize_digests: Validates and converts a list of hex digests to bytes32.productIds:list[int]digests:list[Union[str,bytes]]nonce:Optional[int]classmethodserialize_digests(v)[source]Return type:list[bytes]

Bases:BaseParamsSigned

Parameters to cancel specific orders.

**Args:**
  productIds (list[int]): List of product IDs for the orders to be canceled.digests (list[Digest]): List of digests of the orders to be canceled.nonce (Optional[int]): A unique number used to prevent replay attacks.

productIds (list[int]): List of product IDs for the orders to be canceled.

digests (list[Digest]): List of digests of the orders to be canceled.

nonce (Optional[int]): A unique number used to prevent replay attacks.

**Methods:**
  serialize_digests: Validates and converts a list of hex digests to bytes32.

serialize_digests: Validates and converts a list of hex digests to bytes32.

**productIds:list[int]**

**digests:list[Union[str,bytes]]**

**nonce:Optional[int]**

**classmethodserialize_digests(v)[source]**
  Return type:list[bytes]

**Return type:**
  list[bytes]

list[bytes]

**classnado_protocol.engine_client.types.CancelProductOrdersParams(**data)[source]**
  Bases:BaseParamsSignedParameters to cancel all orders for specific products.Args:productIds (list[int]): List of product IDs for the orders to be canceled.digest (str, optional): Optional EIP-712 digest of the CancelProductOrder request.nonce (Optional[int]): A unique number used to prevent replay attacks.productIds:list[int]digest:Optional[str]nonce:Optional[int]

Bases:BaseParamsSigned

Parameters to cancel all orders for specific products.

**Args:**
  productIds (list[int]): List of product IDs for the orders to be canceled.digest (str, optional): Optional EIP-712 digest of the CancelProductOrder request.nonce (Optional[int]): A unique number used to prevent replay attacks.

productIds (list[int]): List of product IDs for the orders to be canceled.

digest (str, optional): Optional EIP-712 digest of the CancelProductOrder request.

nonce (Optional[int]): A unique number used to prevent replay attacks.

**productIds:list[int]**

**digest:Optional[str]**

**nonce:Optional[int]**

**classnado_protocol.engine_client.types.CancelAndPlaceParams(**data)[source]**
  Bases:NadoBaseModelParameters to perform an order cancellation + order placement in the same request.Args:cancel_orders (CancelOrdersParams): Order cancellation object.
place_order (PlaceOrderParams): Order placement object.cancel_orders:CancelOrdersParamsplace_order:PlaceOrderParams

Bases:NadoBaseModel

Parameters to perform an order cancellation + order placement in the same request.

**Args:**
  cancel_orders (CancelOrdersParams): Order cancellation object.
place_order (PlaceOrderParams): Order placement object.

cancel_orders (CancelOrdersParams): Order cancellation object.
place_order (PlaceOrderParams): Order placement object.

**cancel_orders:CancelOrdersParams**

**place_order:PlaceOrderParams**

**classnado_protocol.engine_client.types.WithdrawCollateralParams(**data)[source]**
  Bases:BaseParamsSignedParameters required to withdraw collateral from a specific product.Attributes:productId (int): The ID of the product to withdraw collateral from.amount (int): The amount of collateral to be withdrawn.spot_leverage (Optional[bool]): Indicates whether leverage is to be used. Defaults to True.
If set to False, the transaction fails if it causes a borrow on the subaccount.productId:intamount:intspot_leverage:Optional[bool]

Bases:BaseParamsSigned

Parameters required to withdraw collateral from a specific product.

**Attributes:**
  productId (int): The ID of the product to withdraw collateral from.amount (int): The amount of collateral to be withdrawn.spot_leverage (Optional[bool]): Indicates whether leverage is to be used. Defaults to True.
If set to False, the transaction fails if it causes a borrow on the subaccount.

productId (int): The ID of the product to withdraw collateral from.

amount (int): The amount of collateral to be withdrawn.

spot_leverage (Optional[bool]): Indicates whether leverage is to be used. Defaults to True.
If set to False, the transaction fails if it causes a borrow on the subaccount.

**productId:int**

**amount:int**

**spot_leverage:Optional[bool]**

**classnado_protocol.engine_client.types.LiquidateSubaccountParams(**data)[source]**
  Bases:BaseParamsSignedParameters required to liquidate a subaccount.Attributes:liquidatee (Subaccount): The subaccount that is to be liquidated.productId (int): ID of product to liquidate.isEncodedSpread (bool): When set to True, productId is expected to encode a perp and spot product Ids as follows: (perp_id << 16) | spot_idamount (int): The amount to be liquidated.Methods:serialize_liquidatee(cls, v: Subaccount) -> bytes: Validates and converts the liquidatee subaccount to bytes32 format.liquidatee:Union[str,bytes,SubaccountParams]productId:intisEncodedSpread:boolamount:intclassmethodserialize_liquidatee(v)[source]Return type:bytes

Bases:BaseParamsSigned

Parameters required to liquidate a subaccount.

**Attributes:**
  liquidatee (Subaccount): The subaccount that is to be liquidated.productId (int): ID of product to liquidate.isEncodedSpread (bool): When set to True, productId is expected to encode a perp and spot product Ids as follows: (perp_id << 16) | spot_idamount (int): The amount to be liquidated.

liquidatee (Subaccount): The subaccount that is to be liquidated.

productId (int): ID of product to liquidate.

isEncodedSpread (bool): When set to True, productId is expected to encode a perp and spot product Ids as follows: (perp_id << 16) | spot_id

amount (int): The amount to be liquidated.

**Methods:**
  serialize_liquidatee(cls, v: Subaccount) -> bytes: Validates and converts the liquidatee subaccount to bytes32 format.

serialize_liquidatee(cls, v: Subaccount) -> bytes: Validates and converts the liquidatee subaccount to bytes32 format.

**liquidatee:Union[str,bytes,SubaccountParams]**

**productId:int**

**isEncodedSpread:bool**

**amount:int**

**classmethodserialize_liquidatee(v)[source]**
  Return type:bytes

**Return type:**
  bytes

bytes

**classnado_protocol.engine_client.types.MintNlpParams(**data)[source]**
  Bases:BaseParamsSignedParameters required for minting Nado Liquidity Provider (NLP) tokens for a specific product in a subaccount.Attributes:quoteAmount (int): The amount of quote to be consumed by minting NLP multiplied by 1e18.spot_leverage (Optional[bool]): Indicates whether leverage is to be used. Defaults to True.
If set to False, the transaction fails if it causes a borrow on the subaccount.quoteAmount:intspot_leverage:Optional[bool]

Bases:BaseParamsSigned

Parameters required for minting Nado Liquidity Provider (NLP) tokens for a specific product in a subaccount.

**Attributes:**
  quoteAmount (int): The amount of quote to be consumed by minting NLP multiplied by 1e18.spot_leverage (Optional[bool]): Indicates whether leverage is to be used. Defaults to True.
If set to False, the transaction fails if it causes a borrow on the subaccount.

quoteAmount (int): The amount of quote to be consumed by minting NLP multiplied by 1e18.

spot_leverage (Optional[bool]): Indicates whether leverage is to be used. Defaults to True.
If set to False, the transaction fails if it causes a borrow on the subaccount.

**quoteAmount:int**

**spot_leverage:Optional[bool]**

**classnado_protocol.engine_client.types.BurnNlpParams(**data)[source]**
  Bases:BaseParamsSignedThis class represents the parameters required to burn Nado Liquidity Provider (NLP)
tokens for a specific subaccount.Attributes:productId (int): The ID of the product.nlpAmount (int): Amount of NLP tokens to burn multiplied by 1e18.nlpAmount:int

Bases:BaseParamsSigned

This class represents the parameters required to burn Nado Liquidity Provider (NLP)
tokens for a specific subaccount.

**Attributes:**
  productId (int): The ID of the product.nlpAmount (int): Amount of NLP tokens to burn multiplied by 1e18.

productId (int): The ID of the product.

nlpAmount (int): Amount of NLP tokens to burn multiplied by 1e18.

**nlpAmount:int**

**classnado_protocol.engine_client.types.LinkSignerParams(**data)[source]**
  Bases:BaseParamsSignedThis class represents the parameters required to link a signer to a subaccount.Attributes:signer (Subaccount): The subaccount to be linked.Methods:serialize_signer(cls, v: Subaccount) -> bytes: Validates and converts the subaccount to bytes32 format.signer:Union[str,bytes,SubaccountParams]classmethodserialize_signer(v)[source]Return type:bytes

Bases:BaseParamsSigned

This class represents the parameters required to link a signer to a subaccount.

**Attributes:**
  signer (Subaccount): The subaccount to be linked.

signer (Subaccount): The subaccount to be linked.

**Methods:**
  serialize_signer(cls, v: Subaccount) -> bytes: Validates and converts the subaccount to bytes32 format.

serialize_signer(cls, v: Subaccount) -> bytes: Validates and converts the subaccount to bytes32 format.

**signer:Union[str,bytes,SubaccountParams]**

**classmethodserialize_signer(v)[source]**
  Return type:bytes

**Return type:**
  bytes

bytes

**classnado_protocol.engine_client.types.TxRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a transaction request.Attributes:tx (dict): The transaction details.signature (str): The signature for the transaction.spot_leverage (Optional[bool]): Indicates whether leverage should be used. If set to false,
it denotes no borrowing. Defaults to true.digest (Optional[str]): The digest of the transaction.Methods:serialize: Validates and serializes the transaction parameters.tx:dictsignature:strspot_leverage:Optional[bool]digest:Optional[str]classmethodserialize(v)[source]Validates and serializes the transaction parameters.Return type:dictArgs:v (dict): The transaction parameters to be validated and serialized.Raises:ValueError: If the ‘nonce’ attribute is missing in the transaction parameters.Returns:dict: The validated and serialized transaction parameters.

Bases:NadoBaseModel

Parameters for a transaction request.

**Attributes:**
  tx (dict): The transaction details.signature (str): The signature for the transaction.spot_leverage (Optional[bool]): Indicates whether leverage should be used. If set to false,
it denotes no borrowing. Defaults to true.digest (Optional[str]): The digest of the transaction.

tx (dict): The transaction details.

signature (str): The signature for the transaction.

spot_leverage (Optional[bool]): Indicates whether leverage should be used. If set to false,
it denotes no borrowing. Defaults to true.

digest (Optional[str]): The digest of the transaction.

**Methods:**
  serialize: Validates and serializes the transaction parameters.

serialize: Validates and serializes the transaction parameters.

**tx:dict**

**signature:str**

**spot_leverage:Optional[bool]**

**digest:Optional[str]**

**classmethodserialize(v)[source]**
  Validates and serializes the transaction parameters.Return type:dictArgs:v (dict): The transaction parameters to be validated and serialized.Raises:ValueError: If the ‘nonce’ attribute is missing in the transaction parameters.Returns:dict: The validated and serialized transaction parameters.

Validates and serializes the transaction parameters.

**Return type:**
  dict

dict

**Args:**
  v (dict): The transaction parameters to be validated and serialized.

v (dict): The transaction parameters to be validated and serialized.

**Raises:**
  ValueError: If the ‘nonce’ attribute is missing in the transaction parameters.

ValueError: If the ‘nonce’ attribute is missing in the transaction parameters.

**Returns:**
  dict: The validated and serialized transaction parameters.

dict: The validated and serialized transaction parameters.

**classnado_protocol.engine_client.types.PlaceOrderRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a request to place an order.Attributes:place_order (PlaceOrderParams): The parameters for the order to be placed.Methods:serialize: Validates and serializes the order parameters.place_order:PlaceOrderParamsclassmethodserialize(v)[source]Return type:PlaceOrderParams

Bases:NadoBaseModel

Parameters for a request to place an order.

**Attributes:**
  place_order (PlaceOrderParams): The parameters for the order to be placed.

place_order (PlaceOrderParams): The parameters for the order to be placed.

**Methods:**
  serialize: Validates and serializes the order parameters.

serialize: Validates and serializes the order parameters.

**place_order:PlaceOrderParams**

**classmethodserialize(v)[source]**
  Return type:PlaceOrderParams

**Return type:**
  PlaceOrderParams

PlaceOrderParams

**classnado_protocol.engine_client.types.CancelOrdersRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a cancel orders request.Attributes:cancel_orders (CancelOrdersParams): The parameters of the orders to be cancelled.Methods:serialize: Serializes ‘digests’ in ‘cancel_orders’ into their hexadecimal representation.to_tx_request: Validates and converts ‘cancel_orders’ into a transaction request.cancel_orders:CancelOrdersParamsclassmethodserialize(v)[source]Serializes ‘digests’ in ‘cancel_orders’ into their hexadecimal representation.Return type:CancelOrdersParamsArgs:v (CancelOrdersParams): The parameters of the orders to be cancelled.Returns:CancelOrdersParams: The ‘cancel_orders’ with serialized ‘digests’.

Bases:NadoBaseModel

Parameters for a cancel orders request.

**Attributes:**
  cancel_orders (CancelOrdersParams): The parameters of the orders to be cancelled.

cancel_orders (CancelOrdersParams): The parameters of the orders to be cancelled.

**Methods:**
  serialize: Serializes ‘digests’ in ‘cancel_orders’ into their hexadecimal representation.to_tx_request: Validates and converts ‘cancel_orders’ into a transaction request.

serialize: Serializes ‘digests’ in ‘cancel_orders’ into their hexadecimal representation.

to_tx_request: Validates and converts ‘cancel_orders’ into a transaction request.

**cancel_orders:CancelOrdersParams**

**classmethodserialize(v)[source]**
  Serializes ‘digests’ in ‘cancel_orders’ into their hexadecimal representation.Return type:CancelOrdersParamsArgs:v (CancelOrdersParams): The parameters of the orders to be cancelled.Returns:CancelOrdersParams: The ‘cancel_orders’ with serialized ‘digests’.

Serializes ‘digests’ in ‘cancel_orders’ into their hexadecimal representation.

**Return type:**
  CancelOrdersParams

CancelOrdersParams

**Args:**
  v (CancelOrdersParams): The parameters of the orders to be cancelled.

v (CancelOrdersParams): The parameters of the orders to be cancelled.

**Returns:**
  CancelOrdersParams: The ‘cancel_orders’ with serialized ‘digests’.

CancelOrdersParams: The ‘cancel_orders’ with serialized ‘digests’.

**classnado_protocol.engine_client.types.CancelProductOrdersRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a cancel product orders request.Attributes:cancel_product_orders (CancelProductOrdersParams): The parameters of the product orders to be cancelled.Methods:to_tx_request: Validates and converts ‘cancel_product_orders’ into a transaction request.cancel_product_orders:CancelProductOrdersParams

Bases:NadoBaseModel

Parameters for a cancel product orders request.

**Attributes:**
  cancel_product_orders (CancelProductOrdersParams): The parameters of the product orders to be cancelled.

cancel_product_orders (CancelProductOrdersParams): The parameters of the product orders to be cancelled.

**Methods:**
  to_tx_request: Validates and converts ‘cancel_product_orders’ into a transaction request.

to_tx_request: Validates and converts ‘cancel_product_orders’ into a transaction request.

**cancel_product_orders:CancelProductOrdersParams**

**classnado_protocol.engine_client.types.CancelAndPlaceRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a cancel and place request.Attributes:cancel_and_place (CancelAndPlaceParams): Request parameters for engine cancel_and_place executioncancel_and_place:CancelAndPlaceParamsclassmethodserialize(v)[source]Return type:dict

Bases:NadoBaseModel

Parameters for a cancel and place request.

**Attributes:**
  cancel_and_place (CancelAndPlaceParams): Request parameters for engine cancel_and_place execution

cancel_and_place (CancelAndPlaceParams): Request parameters for engine cancel_and_place execution

**cancel_and_place:CancelAndPlaceParams**

**classmethodserialize(v)[source]**
  Return type:dict

**Return type:**
  dict

dict

**classnado_protocol.engine_client.types.WithdrawCollateralRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a withdraw collateral request.Attributes:withdraw_collateral (WithdrawCollateralParams): The parameters of the collateral to be withdrawn.Methods:serialize: Validates and converts the ‘amount’ attribute of ‘withdraw_collateral’ to string.to_tx_request: Validates and converts ‘withdraw_collateral’ into a transaction request.withdraw_collateral:WithdrawCollateralParamsclassmethodserialize(v)[source]Return type:WithdrawCollateralParams

Bases:NadoBaseModel

Parameters for a withdraw collateral request.

**Attributes:**
  withdraw_collateral (WithdrawCollateralParams): The parameters of the collateral to be withdrawn.

withdraw_collateral (WithdrawCollateralParams): The parameters of the collateral to be withdrawn.

**Methods:**
  serialize: Validates and converts the ‘amount’ attribute of ‘withdraw_collateral’ to string.to_tx_request: Validates and converts ‘withdraw_collateral’ into a transaction request.

serialize: Validates and converts the ‘amount’ attribute of ‘withdraw_collateral’ to string.

to_tx_request: Validates and converts ‘withdraw_collateral’ into a transaction request.

**withdraw_collateral:WithdrawCollateralParams**

**classmethodserialize(v)[source]**
  Return type:WithdrawCollateralParams

**Return type:**
  WithdrawCollateralParams

WithdrawCollateralParams

**classnado_protocol.engine_client.types.LiquidateSubaccountRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a liquidate subaccount request.Attributes:liquidate_subaccount (LiquidateSubaccountParams): The parameters for the subaccount to be liquidated.Methods:serialize: Validates and converts the ‘amount’ attribute and the ‘liquidatee’ attribute
of ‘liquidate_subaccount’ to their proper serialized forms.to_tx_request: Validates and converts ‘liquidate_subaccount’ into a transaction request.liquidate_subaccount:LiquidateSubaccountParamsclassmethodserialize(v)[source]Return type:LiquidateSubaccountParams

Bases:NadoBaseModel

Parameters for a liquidate subaccount request.

**Attributes:**
  liquidate_subaccount (LiquidateSubaccountParams): The parameters for the subaccount to be liquidated.

liquidate_subaccount (LiquidateSubaccountParams): The parameters for the subaccount to be liquidated.

**Methods:**
  serialize: Validates and converts the ‘amount’ attribute and the ‘liquidatee’ attribute
of ‘liquidate_subaccount’ to their proper serialized forms.to_tx_request: Validates and converts ‘liquidate_subaccount’ into a transaction request.

serialize: Validates and converts the ‘amount’ attribute and the ‘liquidatee’ attribute
of ‘liquidate_subaccount’ to their proper serialized forms.

to_tx_request: Validates and converts ‘liquidate_subaccount’ into a transaction request.

**liquidate_subaccount:LiquidateSubaccountParams**

**classmethodserialize(v)[source]**
  Return type:LiquidateSubaccountParams

**Return type:**
  LiquidateSubaccountParams

LiquidateSubaccountParams

**classnado_protocol.engine_client.types.MintNlpRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a mint NLP request.Attributes:mint_nlp (MintNlpParams): The parameters for minting liquidity.Methods:serialize: Validates and converts the ‘quoteAmount’ attribute of ‘mint_nlp’ to their proper serialized forms.to_tx_request: Validates and converts ‘mint_nlp’ into a transaction request.mint_nlp:MintNlpParamsclassmethodserialize(v)[source]Return type:MintNlpParams

Bases:NadoBaseModel

Parameters for a mint NLP request.

**Attributes:**
  mint_nlp (MintNlpParams): The parameters for minting liquidity.

mint_nlp (MintNlpParams): The parameters for minting liquidity.

**Methods:**
  serialize: Validates and converts the ‘quoteAmount’ attribute of ‘mint_nlp’ to their proper serialized forms.to_tx_request: Validates and converts ‘mint_nlp’ into a transaction request.

serialize: Validates and converts the ‘quoteAmount’ attribute of ‘mint_nlp’ to their proper serialized forms.

to_tx_request: Validates and converts ‘mint_nlp’ into a transaction request.

**mint_nlp:MintNlpParams**

**classmethodserialize(v)[source]**
  Return type:MintNlpParams

**Return type:**
  MintNlpParams

MintNlpParams

**classnado_protocol.engine_client.types.BurnNlpRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a burn NLP request.Attributes:burn_nlp (BurnNlpParams): The parameters for burning liquidity.Methods:serialize: Validates and converts the ‘nlpAmount’ attribute of ‘burn_nlp’ to its proper serialized form.to_tx_request: Validates and converts ‘burn_nlp’ into a transaction request.burn_nlp:BurnNlpParamsclassmethodserialize(v)[source]Return type:BurnNlpParams

Bases:NadoBaseModel

Parameters for a burn NLP request.

**Attributes:**
  burn_nlp (BurnNlpParams): The parameters for burning liquidity.

burn_nlp (BurnNlpParams): The parameters for burning liquidity.

**Methods:**
  serialize: Validates and converts the ‘nlpAmount’ attribute of ‘burn_nlp’ to its proper serialized form.to_tx_request: Validates and converts ‘burn_nlp’ into a transaction request.

serialize: Validates and converts the ‘nlpAmount’ attribute of ‘burn_nlp’ to its proper serialized form.

to_tx_request: Validates and converts ‘burn_nlp’ into a transaction request.

**burn_nlp:BurnNlpParams**

**classmethodserialize(v)[source]**
  Return type:BurnNlpParams

**Return type:**
  BurnNlpParams

BurnNlpParams

**classnado_protocol.engine_client.types.LinkSignerRequest(**data)[source]**
  Bases:NadoBaseModelParameters for a request to link a signer to a subaccount.Attributes:link_signer (LinkSignerParams): Parameters including the subaccount to be linked.Methods:serialize: Validates and converts the ‘signer’ attribute of ‘link_signer’ into its hexadecimal representation.to_tx_request: Validates and converts ‘link_signer’ into a transaction request.link_signer:LinkSignerParamsclassmethodserialize(v)[source]Return type:LinkSignerParams

Bases:NadoBaseModel

Parameters for a request to link a signer to a subaccount.

**Attributes:**
  link_signer (LinkSignerParams): Parameters including the subaccount to be linked.

link_signer (LinkSignerParams): Parameters including the subaccount to be linked.

**Methods:**
  serialize: Validates and converts the ‘signer’ attribute of ‘link_signer’ into its hexadecimal representation.to_tx_request: Validates and converts ‘link_signer’ into a transaction request.

serialize: Validates and converts the ‘signer’ attribute of ‘link_signer’ into its hexadecimal representation.

to_tx_request: Validates and converts ‘link_signer’ into a transaction request.

**link_signer:LinkSignerParams**

**classmethodserialize(v)[source]**
  Return type:LinkSignerParams

**Return type:**
  LinkSignerParams

LinkSignerParams

**classnado_protocol.engine_client.types.ExecuteResponse(**data)[source]**
  Bases:NadoBaseModelRepresents the response returned from executing a request.Attributes:status (ResponseStatus): The status of the response.signature (Optional[str]): The signature of the response. Only present if the request was successfully executed.data (Optional[ExecuteResponseData]): Data returned from execute, not all executes currently return data.error_code (Optional[int]): The error code, if any error occurred during the execution of the request.error (Optional[str]): The error message, if any error occurred during the execution of the request.request_type (Optional[str]): Type of the request.req (Optional[dict]): The original request that was executed.id (Optional[id]): An optional client id provided when placing an orderstatus:ResponseStatussignature:Optional[str]data:Union[PlaceOrderResponse,PlaceOrdersResponse,CancelOrdersResponse,None]error_code:Optional[int]error:Optional[str]request_type:Optional[str]req:Optional[dict]id:Optional[int]

Bases:NadoBaseModel

Represents the response returned from executing a request.

**Attributes:**
  status (ResponseStatus): The status of the response.signature (Optional[str]): The signature of the response. Only present if the request was successfully executed.data (Optional[ExecuteResponseData]): Data returned from execute, not all executes currently return data.error_code (Optional[int]): The error code, if any error occurred during the execution of the request.error (Optional[str]): The error message, if any error occurred during the execution of the request.request_type (Optional[str]): Type of the request.req (Optional[dict]): The original request that was executed.id (Optional[id]): An optional client id provided when placing an order

status (ResponseStatus): The status of the response.

signature (Optional[str]): The signature of the response. Only present if the request was successfully executed.

data (Optional[ExecuteResponseData]): Data returned from execute, not all executes currently return data.

error_code (Optional[int]): The error code, if any error occurred during the execution of the request.

error (Optional[str]): The error message, if any error occurred during the execution of the request.

request_type (Optional[str]): Type of the request.

req (Optional[dict]): The original request that was executed.

id (Optional[id]): An optional client id provided when placing an order

**status:ResponseStatus**

**signature:Optional[str]**

**data:Union[PlaceOrderResponse,PlaceOrdersResponse,CancelOrdersResponse,None]**

**error_code:Optional[int]**

**error:Optional[str]**

**request_type:Optional[str]**

**req:Optional[dict]**

**id:Optional[int]**

**classnado_protocol.engine_client.types.EngineQueryType(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumEnumeration of the different types of engine queries.STATUS='status'CONTRACTS='contracts'NONCES='nonces'ORDER='order'SYMBOLS='symbols'ALL_PRODUCTS='all_products'FEE_RATES='fee_rates'HEALTH_GROUPS='health_groups'LINKED_SIGNER='linked_signer'MARKET_LIQUIDITY='market_liquidity'MARKET_PRICE='market_price'MAX_ORDER_SIZE='max_order_size'MAX_WITHDRAWABLE='max_withdrawable'MAX_NLP_MINTABLE='max_nlp_mintable'SUBACCOUNT_INFO='subaccount_info'SUBACCOUNT_ORDERS='subaccount_orders'ORDERS='orders'ISOLATED_POSITIONS='isolated_positions'

Bases:StrEnum

Enumeration of the different types of engine queries.

**STATUS='status'**

**CONTRACTS='contracts'**

**NONCES='nonces'**

**ORDER='order'**

**SYMBOLS='symbols'**

**ALL_PRODUCTS='all_products'**

**FEE_RATES='fee_rates'**

**HEALTH_GROUPS='health_groups'**

**LINKED_SIGNER='linked_signer'**

**MARKET_LIQUIDITY='market_liquidity'**

**MARKET_PRICE='market_price'**

**MAX_ORDER_SIZE='max_order_size'**

**MAX_WITHDRAWABLE='max_withdrawable'**

**MAX_NLP_MINTABLE='max_nlp_mintable'**

**SUBACCOUNT_INFO='subaccount_info'**

**SUBACCOUNT_ORDERS='subaccount_orders'**

**ORDERS='orders'**

**ISOLATED_POSITIONS='isolated_positions'**

**classnado_protocol.engine_client.types.QueryStatusParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the status of the engine.

Bases:NadoBaseModel

Parameters for querying the status of the engine.

**classnado_protocol.engine_client.types.QueryContractsParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the Nado contract addresses.

Bases:NadoBaseModel

Parameters for querying the Nado contract addresses.

**classnado_protocol.engine_client.types.QueryNoncesParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the nonces associated with a specific address.address:str

Bases:NadoBaseModel

Parameters for querying the nonces associated with a specific address.

**address:str**

**classnado_protocol.engine_client.types.QueryOrderParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying a specific order using its product_id and digest.product_id:intdigest:str

Bases:NadoBaseModel

Parameters for querying a specific order using its product_id and digest.

**product_id:int**

**digest:str**

**nado_protocol.engine_client.types.QuerySubaccountInfoTx**
  alias ofApplyDeltaTx

alias ofApplyDeltaTx

**classnado_protocol.engine_client.types.QuerySubaccountInfoParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the subaccount summary from engine, including balances.subaccount:strtxns:Optional[str]pre_state:Optional[str]

Bases:NadoBaseModel

Parameters for querying the subaccount summary from engine, including balances.

**subaccount:str**

**txns:Optional[str]**

**pre_state:Optional[str]**

**classnado_protocol.engine_client.types.QuerySubaccountOpenOrdersParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying open orders associated with a subaccount for a specific product.product_id:intsender:str

Bases:NadoBaseModel

Parameters for querying open orders associated with a subaccount for a specific product.

**product_id:int**

**sender:str**

**classnado_protocol.engine_client.types.QueryMarketLiquidityParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the market liquidity for a specific product up to a defined depth.product_id:intdepth:int

Bases:NadoBaseModel

Parameters for querying the market liquidity for a specific product up to a defined depth.

**product_id:int**

**depth:int**

**classnado_protocol.engine_client.types.QueryAllProductsParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying all products available in the engine.

Bases:NadoBaseModel

Parameters for querying all products available in the engine.

**classnado_protocol.engine_client.types.QueryMarketPriceParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the market price of a specific product.product_id:int

Bases:NadoBaseModel

Parameters for querying the market price of a specific product.

**product_id:int**

**classnado_protocol.engine_client.types.QueryMaxOrderSizeParams(**data)[source]**
  Bases:SpotLeverageSerializerMixinParameters for querying the maximum order size for a specific product and a given sender.sender:strproduct_id:intprice_x18:strdirection:MaxOrderSizeDirectionreduce_only:Optional[bool]isolated:Optional[bool]classmethoddirection_to_str(v)[source]Return type:strclassmethodreduce_only_to_str(v)[source]Return type:Optional[str]classmethodisolated_to_str(v)[source]Return type:Optional[str]

Bases:SpotLeverageSerializerMixin

Parameters for querying the maximum order size for a specific product and a given sender.

**sender:str**

**product_id:int**

**price_x18:str**

**direction:MaxOrderSizeDirection**

**reduce_only:Optional[bool]**

**isolated:Optional[bool]**

**classmethoddirection_to_str(v)[source]**
  Return type:str

**Return type:**
  str

str

**classmethodreduce_only_to_str(v)[source]**
  Return type:Optional[str]

**Return type:**
  Optional[str]

Optional[str]

**classmethodisolated_to_str(v)[source]**
  Return type:Optional[str]

**Return type:**
  Optional[str]

Optional[str]

**classnado_protocol.engine_client.types.QueryMaxWithdrawableParams(**data)[source]**
  Bases:SpotLeverageSerializerMixinParameters for querying the maximum withdrawable amount for a specific product and a given sender.sender:strproduct_id:int

Bases:SpotLeverageSerializerMixin

Parameters for querying the maximum withdrawable amount for a specific product and a given sender.

**sender:str**

**product_id:int**

**classnado_protocol.engine_client.types.QueryMaxLpMintableParams(**data)[source]**
  Bases:SpotLeverageSerializerMixinParameters for querying the maximum liquidity that can be minted by a specified sender for a specific product.sender:strproduct_id:int

Bases:SpotLeverageSerializerMixin

Parameters for querying the maximum liquidity that can be minted by a specified sender for a specific product.

**sender:str**

**product_id:int**

**classnado_protocol.engine_client.types.QueryFeeRatesParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the fee rates associated with a specified sender.sender:str

Bases:NadoBaseModel

Parameters for querying the fee rates associated with a specified sender.

**sender:str**

**classnado_protocol.engine_client.types.QueryHealthGroupsParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the health groups in the engine.

Bases:NadoBaseModel

Parameters for querying the health groups in the engine.

**classnado_protocol.engine_client.types.QueryLinkedSignerParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying the signer linked to a specified subaccount.subaccount:str

Bases:NadoBaseModel

Parameters for querying the signer linked to a specified subaccount.

**subaccount:str**

**nado_protocol.engine_client.types.StatusData**
  alias ofEngineStatus

alias ofEngineStatus

**classnado_protocol.engine_client.types.ContractsData(**data)[source]**
  Bases:NadoBaseModelData model for Nado’s contract addresses.chain_id:strendpoint_addr:str

Bases:NadoBaseModel

Data model for Nado’s contract addresses.

**chain_id:str**

**endpoint_addr:str**

**classnado_protocol.engine_client.types.NoncesData(**data)[source]**
  Bases:NadoBaseModelData model for nonce values for transactions and orders.tx_nonce:strorder_nonce:str

Bases:NadoBaseModel

Data model for nonce values for transactions and orders.

**tx_nonce:str**

**order_nonce:str**

**classnado_protocol.engine_client.types.OrderData(**data)[source]**
  Bases:NadoBaseModelData model for details of an order.product_id:intsender:strprice_x18:stramount:strexpiration:strnonce:strunfilled_amount:strdigest:strplaced_at:str

Bases:NadoBaseModel

Data model for details of an order.

**product_id:int**

**sender:str**

**price_x18:str**

**amount:str**

**expiration:str**

**nonce:str**

**unfilled_amount:str**

**digest:str**

**placed_at:str**

**classnado_protocol.engine_client.types.PreState(**data)[source]**
  Bases:NadoBaseModelModel for subaccount state before simulated transactions were applied.healths:list[SubaccountHealth]health_contributions:list[list[str]]spot_balances:list[SpotProductBalance]perp_balances:list[PerpProductBalance]

Bases:NadoBaseModel

Model for subaccount state before simulated transactions were applied.

**healths:list[SubaccountHealth]**

**health_contributions:list[list[str]]**

**spot_balances:list[SpotProductBalance]**

**perp_balances:list[PerpProductBalance]**

**classnado_protocol.engine_client.types.SubaccountInfoData(**data)[source]**
  Bases:NadoBaseModelModel for detailed info about a subaccount, including balances.subaccount:strexists:boolhealths:list[SubaccountHealth]health_contributions:list[list[str]]spot_count:intperp_count:intspot_balances:list[SpotProductBalance]perp_balances:list[PerpProductBalance]spot_products:list[SpotProduct]perp_products:list[PerpProduct]pre_state:Optional[PreState]parse_subaccount_balance(product_id)[source]Parses the balance of a subaccount for a given product.Return type:Union[SpotProductBalance,PerpProductBalance]Args:product_id (int): The ID of the product to lookup.Returns:Union[SpotProductBalance, PerpProductBalance]: The balance of the product in the subaccount.Raises:ValueError: If the product ID provided is not found.

Bases:NadoBaseModel

Model for detailed info about a subaccount, including balances.

**subaccount:str**

**exists:bool**

**healths:list[SubaccountHealth]**

**health_contributions:list[list[str]]**

**spot_count:int**

**perp_count:int**

**spot_balances:list[SpotProductBalance]**

**perp_balances:list[PerpProductBalance]**

**spot_products:list[SpotProduct]**

**perp_products:list[PerpProduct]**

**pre_state:Optional[PreState]**

**parse_subaccount_balance(product_id)[source]**
  Parses the balance of a subaccount for a given product.Return type:Union[SpotProductBalance,PerpProductBalance]Args:product_id (int): The ID of the product to lookup.Returns:Union[SpotProductBalance, PerpProductBalance]: The balance of the product in the subaccount.Raises:ValueError: If the product ID provided is not found.

Parses the balance of a subaccount for a given product.

**Return type:**
  Union[SpotProductBalance,PerpProductBalance]

Union[SpotProductBalance,PerpProductBalance]

**Args:**
  product_id (int): The ID of the product to lookup.

product_id (int): The ID of the product to lookup.

**Returns:**
  Union[SpotProductBalance, PerpProductBalance]: The balance of the product in the subaccount.

Union[SpotProductBalance, PerpProductBalance]: The balance of the product in the subaccount.

**Raises:**
  ValueError: If the product ID provided is not found.

ValueError: If the product ID provided is not found.

**classnado_protocol.engine_client.types.SubaccountOpenOrdersData(**data)[source]**
  Bases:NadoBaseModelData model encapsulating open orders of a subaccount for aspecific product.sender:strorders:list[OrderData]

Bases:NadoBaseModel

Data model encapsulating open orders of a subaccount for a

specific product.

**sender:str**

**orders:list[OrderData]**

**classnado_protocol.engine_client.types.MarketLiquidityData(**data)[source]**
  Bases:NadoBaseModelData model for market liquidity details.bids:list[list]asks:list[list]timestamp:str

Bases:NadoBaseModel

Data model for market liquidity details.

**bids:list[list]**

**asks:list[list]**

**timestamp:str**

**classnado_protocol.engine_client.types.AllProductsData(**data)[source]**
  Bases:NadoBaseModelData model for all the products available.spot_products:list[SpotProduct]perp_products:list[PerpProduct]

Bases:NadoBaseModel

Data model for all the products available.

**spot_products:list[SpotProduct]**

**perp_products:list[PerpProduct]**

**classnado_protocol.engine_client.types.MarketPriceData(**data)[source]**
  Bases:NadoBaseModelData model for the bid and ask prices of a specific product.product_id:intbid_x18:strask_x18:str

Bases:NadoBaseModel

Data model for the bid and ask prices of a specific product.

**product_id:int**

**bid_x18:str**

**ask_x18:str**

**classnado_protocol.engine_client.types.MaxOrderSizeData(**data)[source]**
  Bases:NadoBaseModelData model for the maximum order size.max_order_size:str

Bases:NadoBaseModel

Data model for the maximum order size.

**max_order_size:str**

**classnado_protocol.engine_client.types.MaxWithdrawableData(**data)[source]**
  Bases:NadoBaseModelData model for the maximum withdrawable amount.max_withdrawable:str

Bases:NadoBaseModel

Data model for the maximum withdrawable amount.

**max_withdrawable:str**

**classnado_protocol.engine_client.types.MaxLpMintableData(**data)[source]**
  Bases:NadoBaseModelData model for the maximum liquidity that can be minted.max_base_amount:strmax_quote_amount:str

Bases:NadoBaseModel

Data model for the maximum liquidity that can be minted.

**max_base_amount:str**

**max_quote_amount:str**

**classnado_protocol.engine_client.types.FeeRatesData(**data)[source]**
  Bases:NadoBaseModelData model for various fee rates associated with transactions.taker_fee_rates_x18:list[str]maker_fee_rates_x18:list[str]liquidation_sequencer_fee:strhealth_check_sequencer_fee:strtaker_sequencer_fee:strwithdraw_sequencer_fees:list[str]

Bases:NadoBaseModel

Data model for various fee rates associated with transactions.

**taker_fee_rates_x18:list[str]**

**maker_fee_rates_x18:list[str]**

**liquidation_sequencer_fee:str**

**health_check_sequencer_fee:str**

**taker_sequencer_fee:str**

**withdraw_sequencer_fees:list[str]**

**classnado_protocol.engine_client.types.HealthGroupsData(**data)[source]**
  Bases:NadoBaseModelData model for health group IDs.health_groups:list[list[int]]

Bases:NadoBaseModel

Data model for health group IDs.

**health_groups:list[list[int]]**

**classnado_protocol.engine_client.types.LinkedSignerData(**data)[source]**
  Bases:NadoBaseModelData model for the signer linked to a subaccount.linked_signer:str

Bases:NadoBaseModel

Data model for the signer linked to a subaccount.

**linked_signer:str**

**classnado_protocol.engine_client.types.QueryResponse(**data)[source]**
  Bases:NadoBaseModelRepresents a response to a query request.Attributes:status (ResponseStatus): The status of the query response.data (Optional[QueryResponseData]): The data returned from the query, or an error message if the query failed.error (Optional[str]): The error message, if any error occurred during the query.error_code (Optional[int]): The error code, if any error occurred during the query.request_type (Optional[str]): Type of the request.status:ResponseStatusdata:Union[EngineStatus,ContractsData,NoncesData,OrderData,SubaccountInfoData,SubaccountOpenOrdersData,SubaccountMultiProductsOpenOrdersData,MarketLiquidityData,SymbolsData,AllProductsData,MarketPriceData,MaxOrderSizeData,MaxWithdrawableData,MaxLpMintableData,FeeRatesData,HealthGroupsData,LinkedSignerData,list[ProductSymbol],IsolatedPositionsData,None]error:Optional[str]error_code:Optional[int]request_type:Optional[str]

Bases:NadoBaseModel

Represents a response to a query request.

**Attributes:**
  status (ResponseStatus): The status of the query response.data (Optional[QueryResponseData]): The data returned from the query, or an error message if the query failed.error (Optional[str]): The error message, if any error occurred during the query.error_code (Optional[int]): The error code, if any error occurred during the query.request_type (Optional[str]): Type of the request.

status (ResponseStatus): The status of the query response.

data (Optional[QueryResponseData]): The data returned from the query, or an error message if the query failed.

error (Optional[str]): The error message, if any error occurred during the query.

error_code (Optional[int]): The error code, if any error occurred during the query.

request_type (Optional[str]): Type of the request.

**status:ResponseStatus**

**data:Union[EngineStatus,ContractsData,NoncesData,OrderData,SubaccountInfoData,SubaccountOpenOrdersData,SubaccountMultiProductsOpenOrdersData,MarketLiquidityData,SymbolsData,AllProductsData,MarketPriceData,MaxOrderSizeData,MaxWithdrawableData,MaxLpMintableData,FeeRatesData,HealthGroupsData,LinkedSignerData,list[ProductSymbol],IsolatedPositionsData,None]**

**error:Optional[str]**

**error_code:Optional[int]**

**request_type:Optional[str]**

**classnado_protocol.engine_client.types.ResponseStatus(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumSUCCESS='success'FAILURE='failure'

Bases:StrEnum

**SUCCESS='success'**

**FAILURE='failure'**

**classnado_protocol.engine_client.types.EngineStatus(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumACTIVE='active'FAILED='failed'

Bases:StrEnum

**ACTIVE='active'**

**FAILED='failed'**

**classnado_protocol.engine_client.types.ApplyDelta(**data)[source]**
  Bases:NadoBaseModelproduct_id:intsubaccount:stramount_delta:strv_quote_delta:str

Bases:NadoBaseModel

**product_id:int**

**subaccount:str**

**amount_delta:str**

**v_quote_delta:str**

**classnado_protocol.engine_client.types.ApplyDeltaTx(**data)[source]**
  Bases:NadoBaseModelapply_delta:ApplyDelta

Bases:NadoBaseModel

**apply_delta:ApplyDelta**

**classnado_protocol.engine_client.types.SubaccountHealth(**data)[source]**
  Bases:NadoBaseModelassets:strliabilities:strhealth:str

Bases:NadoBaseModel

**assets:str**

**liabilities:str**

**health:str**

**classnado_protocol.engine_client.types.SpotBalance(**data)[source]**
  Bases:NadoBaseModelamount:str

Bases:NadoBaseModel

**amount:str**

**classnado_protocol.engine_client.types.SpotProductBalance(**data)[source]**
  Bases:NadoBaseModelproduct_id:intbalance:SpotBalance

Bases:NadoBaseModel

**product_id:int**

**balance:SpotBalance**

**classnado_protocol.engine_client.types.PerpBalance(**data)[source]**
  Bases:NadoBaseModelamount:strv_quote_balance:strlast_cumulative_funding_x18:str

Bases:NadoBaseModel

**amount:str**

**v_quote_balance:str**

**last_cumulative_funding_x18:str**

**classnado_protocol.engine_client.types.PerpProductBalance(**data)[source]**
  Bases:NadoBaseModelproduct_id:intbalance:PerpBalance

Bases:NadoBaseModel

**product_id:int**

**balance:PerpBalance**

**classnado_protocol.engine_client.types.ProductRisk(**data)[source]**
  Bases:NadoBaseModellong_weight_initial_x18:strshort_weight_initial_x18:strlong_weight_maintenance_x18:strshort_weight_maintenance_x18:strprice_x18:str

Bases:NadoBaseModel

**long_weight_initial_x18:str**

**short_weight_initial_x18:str**

**long_weight_maintenance_x18:str**

**short_weight_maintenance_x18:str**

**price_x18:str**

**classnado_protocol.engine_client.types.ProductBookInfo(**data)[source]**
  Bases:NadoBaseModelsize_increment:strprice_increment_x18:strmin_size:strcollected_fees:str

Bases:NadoBaseModel

**size_increment:str**

**price_increment_x18:str**

**min_size:str**

**collected_fees:str**

**classnado_protocol.engine_client.types.BaseProduct(**data)[source]**
  Bases:NadoBaseModelproduct_id:intoracle_price_x18:strrisk:ProductRiskbook_info:ProductBookInfo

Bases:NadoBaseModel

**product_id:int**

**oracle_price_x18:str**

**risk:ProductRisk**

**book_info:ProductBookInfo**

**classnado_protocol.engine_client.types.SpotProductConfig(**data)[source]**
  Bases:NadoBaseModeltoken:strinterest_inflection_util_x18:strinterest_floor_x18:strinterest_small_cap_x18:strinterest_large_cap_x18:strwithdraw_fee_x18:strmin_deposit_rate_x18:str

Bases:NadoBaseModel

**token:str**

**interest_inflection_util_x18:str**

**interest_floor_x18:str**

**interest_small_cap_x18:str**

**interest_large_cap_x18:str**

**withdraw_fee_x18:str**

**min_deposit_rate_x18:str**

**classnado_protocol.engine_client.types.SpotProductState(**data)[source]**
  Bases:NadoBaseModelcumulative_deposits_multiplier_x18:strcumulative_borrows_multiplier_x18:strtotal_deposits_normalized:strtotal_borrows_normalized:str

Bases:NadoBaseModel

**cumulative_deposits_multiplier_x18:str**

**cumulative_borrows_multiplier_x18:str**

**total_deposits_normalized:str**

**total_borrows_normalized:str**

**classnado_protocol.engine_client.types.SpotProduct(**data)[source]**
  Bases:BaseProductconfig:SpotProductConfigstate:SpotProductState

Bases:BaseProduct

**config:SpotProductConfig**

**state:SpotProductState**

**classnado_protocol.engine_client.types.PerpProductState(**data)[source]**
  Bases:NadoBaseModelcumulative_funding_long_x18:strcumulative_funding_short_x18:stravailable_settle:stropen_interest:str

Bases:NadoBaseModel

**cumulative_funding_long_x18:str**

**cumulative_funding_short_x18:str**

**available_settle:str**

**open_interest:str**

**classnado_protocol.engine_client.types.PerpProduct(**data)[source]**
  Bases:BaseProductstate:PerpProductState

Bases:BaseProduct

**state:PerpProductState**

**classnado_protocol.engine_client.types.MaxOrderSizeDirection(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumLONG='long'SHORT='short'

Bases:StrEnum

**LONG='long'**

**SHORT='short'**

**classnado_protocol.engine_client.types.StreamAuthenticationParams(**data)[source]**
  Bases:SignatureParamssender:strexpiration:int

Bases:SignatureParams

**sender:str**

**expiration:int**

**classnado_protocol.engine_client.types.Asset(**data)[source]**
  Bases:NadoBaseModelproduct_id:intticker_id:Optional[str]market_type:Optional[str]name:strsymbol:strmaker_fee:Optional[float]taker_fee:Optional[float]can_withdraw:boolcan_deposit:bool

Bases:NadoBaseModel

**product_id:int**

**ticker_id:Optional[str]**

**market_type:Optional[str]**

**name:str**

**symbol:str**

**maker_fee:Optional[float]**

**taker_fee:Optional[float]**

**can_withdraw:bool**

**can_deposit:bool**

**classnado_protocol.engine_client.types.MarketPair(**data)[source]**
  Bases:NadoBaseModelticker_id:strbase:strquote:str

Bases:NadoBaseModel

**ticker_id:str**

**base:str**

**quote:str**

**classnado_protocol.engine_client.types.SpotApr(**data)[source]**
  Bases:NadoBaseModelname:strsymbol:strproduct_id:intdeposit_apr:floatborrow_apr:floattvl:float

Bases:NadoBaseModel

**name:str**

**symbol:str**

**product_id:int**

**deposit_apr:float**

**borrow_apr:float**

**tvl:float**

**classnado_protocol.engine_client.types.Orderbook(**data)[source]**
  Bases:NadoBaseModelticker_id:strtimestamp:intbids:list[list]asks:list[list]

Bases:NadoBaseModel

**ticker_id:str**

**timestamp:int**

**bids:list[list]**

**asks:list[list]**

## nado-protocol.indexer_client

**classnado_protocol.indexer_client.IndexerClient(opts)[source]**
  Bases:IndexerQueryClientClient for interacting with the indexer service.It provides methods for querying data from the indexer service.Attributes:opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.Methods:__init__: Initializes theIndexerClientwith the provided options.__init__(opts)[source]Initializes the IndexerClient with the provided options.Args:opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

Bases:IndexerQueryClient

Client for interacting with the indexer service.

It provides methods for querying data from the indexer service.

**Attributes:**
  opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

**Methods:**
  __init__: Initializes theIndexerClientwith the provided options.

__init__: Initializes theIndexerClientwith the provided options.

**__init__(opts)[source]**
  Initializes the IndexerClient with the provided options.Args:opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

Initializes the IndexerClient with the provided options.

**Args:**
  opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

**classnado_protocol.indexer_client.IndexerClientOpts(**data)[source]**
  Bases:BaseModelModel representing the options for the Indexer Clienturl:AnyUrlclassmethodclean_url(v)[source]Return type:str

Bases:BaseModel

Model representing the options for the Indexer Client

**url:AnyUrl**

**classmethodclean_url(v)[source]**
  Return type:str

**Return type:**
  str

str

**classnado_protocol.indexer_client.IndexerQueryClient(opts)[source]**
  Bases:objectClient for querying data from the indexer service.Attributes:_opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.
url (str): URL of the indexer service.__init__(opts)[source]Initializes the IndexerQueryClient with the provided options.Args:opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.query(params)[source]Sends a query request to the indexer service and returns the response.Thequerymethod is overloaded to accept eitherIndexerParamsor a dictionary orIndexerRequestas the input parameters. Based on the type of the input, the appropriate internal method is invoked
to process the query request.Return type:IndexerResponseArgs:params (IndexerParams | dict | IndexerRequest): The parameters for the query request.Returns:IndexerResponse: The response from the indexer service.get_subaccount_historical_orders(params)[source]Retrieves the historical orders associated with a specific subaccount.Return type:IndexerHistoricalOrdersDataArgs:params (IndexerSubaccountHistoricalOrdersParams): The parameters specifying the subaccount for which to retrieve historical orders.Returns:IndexerHistoricalOrdersData: The historical orders associated with the specified subaccount.get_historical_orders_by_digest(digests)[source]Retrieves historical orders using their unique digests.Return type:IndexerHistoricalOrdersDataArgs:digests (list[str]): A list of order digests.Returns:IndexerHistoricalOrdersData: The historical orders corresponding to the provided digests.get_matches(params)[source]Retrieves match data based on provided parameters.Return type:IndexerMatchesDataArgs:params (IndexerMatchesParams): The parameters for the match data retrieval request.Returns:IndexerMatchesData: The match data corresponding to the provided parameters.get_events(params)[source]Retrieves event data based on provided parameters.Return type:IndexerEventsDataArgs:params (IndexerEventsParams): The parameters for the event data retrieval request.Returns:IndexerEventsData: The event data corresponding to the provided parameters.get_product_snapshots(params)[source]Retrieves snapshot data for specific products.Return type:IndexerProductSnapshotsDataArgs:params (IndexerProductSnapshotsParams): Parameters specifying the products for which to retrieve snapshot data.Returns:IndexerProductSnapshotsData: The product snapshot data corresponding to the provided parameters.get_market_snapshots(params)[source]Retrieves historical market snapshots.Return type:IndexerMarketSnapshotsDataArgs:params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.Returns:IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.get_candlesticks(params)[source]Retrieves candlestick data based on provided parameters.Return type:IndexerCandlesticksDataArgs:params (IndexerCandlesticksParams): The parameters for retrieving candlestick data.Returns:IndexerCandlesticksData: The candlestick data corresponding to the provided parameters.get_perp_funding_rate(product_id)[source]Retrieves the funding rate data for a specific perp product.Return type:IndexerFundingRateDataArgs:product_id (int): The identifier of the perp product.Returns:IndexerFundingRateData: The funding rate data for the specified perp product.get_perp_funding_rates(product_ids)[source]Fetches the latest funding rates for a list of perp products.Return type:Dict[str,IndexerFundingRateData]Args:product_ids (list): List of identifiers for the perp products.Returns:dict: A dictionary mapping each product_id to its latest funding rate and related details.get_perp_prices(product_id)[source]Retrieves the price data for a specific perp product.Return type:IndexerPerpPricesDataArgs:product_id (int): The identifier of the perp product.Returns:IndexerPerpPricesData: The price data for the specified perp product.get_oracle_prices(product_ids)[source]Retrieves the oracle price data for specific products.Return type:IndexerOraclePricesDataArgs:product_ids (list[int]): A list of product identifiers.Returns:IndexerOraclePricesData: The oracle price data for the specified products.get_liquidation_feed()[source]Retrieves the liquidation feed data.Return type:list[IndexerLiquidatableAccount]Returns:IndexerLiquidationFeedData: The latest liquidation feed data.get_linked_signer_rate_limits(subaccount)[source]Retrieves the rate limits for a linked signer of a specific subaccount.Return type:IndexerLinkedSignerRateLimitDataArgs:subaccount (str): The identifier of the subaccount.Returns:IndexerLinkedSignerRateLimitData: The rate limits for the linked signer of the specified subaccount.get_subaccounts(params)[source]Retrieves subaccounts via the indexer.Return type:IndexerSubaccountsDataArgs:params (IndexerSubaccountsParams): The filter parameters for retrieving subaccounts.Returns:IndexerSubaccountsData: List of subaccounts found.get_quote_price()[source]Return type:IndexerQuotePriceDataget_interest_and_funding_payments(params)[source]Return type:IndexerInterestAndFundingDataget_tickers(market_type=None)[source]Return type:Dict[str,IndexerTickerInfo]get_perp_contracts_info()[source]Return type:Dict[str,IndexerPerpContractInfo]get_historical_trades(ticker_id,limit,max_trade_id=None)[source]Return type:List[IndexerTradeInfo]get_multi_subaccount_snapshots(params)[source]Retrieves subaccount snapshots at specified timestamps.
Each snapshot is a view of the subaccount’s balances at that point in time,
with tracked variables for interest, funding, etc.Return type:IndexerAccountSnapshotsDataArgs:params (IndexerAccountSnapshotsParams): Parameters specifying subaccounts,timestamps, and whether to include isolated positions.Returns:IndexerAccountSnapshotsData: Dict mapping subaccount hex -> timestamp -> snapshot data.Each snapshot contains balances with trackedVars including netEntryUnrealized.

Bases:object

Client for querying data from the indexer service.

**Attributes:**
  _opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.
url (str): URL of the indexer service.

_opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.
url (str): URL of the indexer service.

**__init__(opts)[source]**
  Initializes the IndexerQueryClient with the provided options.Args:opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

Initializes the IndexerQueryClient with the provided options.

**Args:**
  opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

opts (IndexerClientOpts): Client configuration options for connecting and interacting with the indexer service.

**query(params)[source]**
  Sends a query request to the indexer service and returns the response.Thequerymethod is overloaded to accept eitherIndexerParamsor a dictionary orIndexerRequestas the input parameters. Based on the type of the input, the appropriate internal method is invoked
to process the query request.Return type:IndexerResponseArgs:params (IndexerParams | dict | IndexerRequest): The parameters for the query request.Returns:IndexerResponse: The response from the indexer service.

Sends a query request to the indexer service and returns the response.

Thequerymethod is overloaded to accept eitherIndexerParamsor a dictionary orIndexerRequestas the input parameters. Based on the type of the input, the appropriate internal method is invoked
to process the query request.

**Return type:**
  IndexerResponse

IndexerResponse

**Args:**
  params (IndexerParams | dict | IndexerRequest): The parameters for the query request.

params (IndexerParams | dict | IndexerRequest): The parameters for the query request.

**Returns:**
  IndexerResponse: The response from the indexer service.

IndexerResponse: The response from the indexer service.

**get_subaccount_historical_orders(params)[source]**
  Retrieves the historical orders associated with a specific subaccount.Return type:IndexerHistoricalOrdersDataArgs:params (IndexerSubaccountHistoricalOrdersParams): The parameters specifying the subaccount for which to retrieve historical orders.Returns:IndexerHistoricalOrdersData: The historical orders associated with the specified subaccount.

Retrieves the historical orders associated with a specific subaccount.

**Return type:**
  IndexerHistoricalOrdersData

IndexerHistoricalOrdersData

**Args:**
  params (IndexerSubaccountHistoricalOrdersParams): The parameters specifying the subaccount for which to retrieve historical orders.

params (IndexerSubaccountHistoricalOrdersParams): The parameters specifying the subaccount for which to retrieve historical orders.

**Returns:**
  IndexerHistoricalOrdersData: The historical orders associated with the specified subaccount.

IndexerHistoricalOrdersData: The historical orders associated with the specified subaccount.

**get_historical_orders_by_digest(digests)[source]**
  Retrieves historical orders using their unique digests.Return type:IndexerHistoricalOrdersDataArgs:digests (list[str]): A list of order digests.Returns:IndexerHistoricalOrdersData: The historical orders corresponding to the provided digests.

Retrieves historical orders using their unique digests.

**Return type:**
  IndexerHistoricalOrdersData

IndexerHistoricalOrdersData

**Args:**
  digests (list[str]): A list of order digests.

digests (list[str]): A list of order digests.

**Returns:**
  IndexerHistoricalOrdersData: The historical orders corresponding to the provided digests.

IndexerHistoricalOrdersData: The historical orders corresponding to the provided digests.

**get_matches(params)[source]**
  Retrieves match data based on provided parameters.Return type:IndexerMatchesDataArgs:params (IndexerMatchesParams): The parameters for the match data retrieval request.Returns:IndexerMatchesData: The match data corresponding to the provided parameters.

Retrieves match data based on provided parameters.

**Return type:**
  IndexerMatchesData

IndexerMatchesData

**Args:**
  params (IndexerMatchesParams): The parameters for the match data retrieval request.

params (IndexerMatchesParams): The parameters for the match data retrieval request.

**Returns:**
  IndexerMatchesData: The match data corresponding to the provided parameters.

IndexerMatchesData: The match data corresponding to the provided parameters.

**get_events(params)[source]**
  Retrieves event data based on provided parameters.Return type:IndexerEventsDataArgs:params (IndexerEventsParams): The parameters for the event data retrieval request.Returns:IndexerEventsData: The event data corresponding to the provided parameters.

Retrieves event data based on provided parameters.

**Return type:**
  IndexerEventsData

IndexerEventsData

**Args:**
  params (IndexerEventsParams): The parameters for the event data retrieval request.

params (IndexerEventsParams): The parameters for the event data retrieval request.

**Returns:**
  IndexerEventsData: The event data corresponding to the provided parameters.

IndexerEventsData: The event data corresponding to the provided parameters.

**get_product_snapshots(params)[source]**
  Retrieves snapshot data for specific products.Return type:IndexerProductSnapshotsDataArgs:params (IndexerProductSnapshotsParams): Parameters specifying the products for which to retrieve snapshot data.Returns:IndexerProductSnapshotsData: The product snapshot data corresponding to the provided parameters.

Retrieves snapshot data for specific products.

**Return type:**
  IndexerProductSnapshotsData

IndexerProductSnapshotsData

**Args:**
  params (IndexerProductSnapshotsParams): Parameters specifying the products for which to retrieve snapshot data.

params (IndexerProductSnapshotsParams): Parameters specifying the products for which to retrieve snapshot data.

**Returns:**
  IndexerProductSnapshotsData: The product snapshot data corresponding to the provided parameters.

IndexerProductSnapshotsData: The product snapshot data corresponding to the provided parameters.

**get_market_snapshots(params)[source]**
  Retrieves historical market snapshots.Return type:IndexerMarketSnapshotsDataArgs:params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.Returns:IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.

Retrieves historical market snapshots.

**Return type:**
  IndexerMarketSnapshotsData

IndexerMarketSnapshotsData

**Args:**
  params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.

params (IndexerMarketSnapshotsParams): Parameters specifying the historical market snapshot request.

**Returns:**
  IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.

IndexerMarketSnapshotsData: The market snapshot data corresponding to the provided parameters.

**get_candlesticks(params)[source]**
  Retrieves candlestick data based on provided parameters.Return type:IndexerCandlesticksDataArgs:params (IndexerCandlesticksParams): The parameters for retrieving candlestick data.Returns:IndexerCandlesticksData: The candlestick data corresponding to the provided parameters.

Retrieves candlestick data based on provided parameters.

**Return type:**
  IndexerCandlesticksData

IndexerCandlesticksData

**Args:**
  params (IndexerCandlesticksParams): The parameters for retrieving candlestick data.

params (IndexerCandlesticksParams): The parameters for retrieving candlestick data.

**Returns:**
  IndexerCandlesticksData: The candlestick data corresponding to the provided parameters.

IndexerCandlesticksData: The candlestick data corresponding to the provided parameters.

**get_perp_funding_rate(product_id)[source]**
  Retrieves the funding rate data for a specific perp product.Return type:IndexerFundingRateDataArgs:product_id (int): The identifier of the perp product.Returns:IndexerFundingRateData: The funding rate data for the specified perp product.

Retrieves the funding rate data for a specific perp product.

**Return type:**
  IndexerFundingRateData

IndexerFundingRateData

**Args:**
  product_id (int): The identifier of the perp product.

product_id (int): The identifier of the perp product.

**Returns:**
  IndexerFundingRateData: The funding rate data for the specified perp product.

IndexerFundingRateData: The funding rate data for the specified perp product.

**get_perp_funding_rates(product_ids)[source]**
  Fetches the latest funding rates for a list of perp products.Return type:Dict[str,IndexerFundingRateData]Args:product_ids (list): List of identifiers for the perp products.Returns:dict: A dictionary mapping each product_id to its latest funding rate and related details.

Fetches the latest funding rates for a list of perp products.

**Return type:**
  Dict[str,IndexerFundingRateData]

Dict[str,IndexerFundingRateData]

**Args:**
  product_ids (list): List of identifiers for the perp products.

product_ids (list): List of identifiers for the perp products.

**Returns:**
  dict: A dictionary mapping each product_id to its latest funding rate and related details.

dict: A dictionary mapping each product_id to its latest funding rate and related details.

**get_perp_prices(product_id)[source]**
  Retrieves the price data for a specific perp product.Return type:IndexerPerpPricesDataArgs:product_id (int): The identifier of the perp product.Returns:IndexerPerpPricesData: The price data for the specified perp product.

Retrieves the price data for a specific perp product.

**Return type:**
  IndexerPerpPricesData

IndexerPerpPricesData

**Args:**
  product_id (int): The identifier of the perp product.

product_id (int): The identifier of the perp product.

**Returns:**
  IndexerPerpPricesData: The price data for the specified perp product.

IndexerPerpPricesData: The price data for the specified perp product.

**get_oracle_prices(product_ids)[source]**
  Retrieves the oracle price data for specific products.Return type:IndexerOraclePricesDataArgs:product_ids (list[int]): A list of product identifiers.Returns:IndexerOraclePricesData: The oracle price data for the specified products.

Retrieves the oracle price data for specific products.

**Return type:**
  IndexerOraclePricesData

IndexerOraclePricesData

**Args:**
  product_ids (list[int]): A list of product identifiers.

product_ids (list[int]): A list of product identifiers.

**Returns:**
  IndexerOraclePricesData: The oracle price data for the specified products.

IndexerOraclePricesData: The oracle price data for the specified products.

**get_liquidation_feed()[source]**
  Retrieves the liquidation feed data.Return type:list[IndexerLiquidatableAccount]Returns:IndexerLiquidationFeedData: The latest liquidation feed data.

Retrieves the liquidation feed data.

**Return type:**
  list[IndexerLiquidatableAccount]

list[IndexerLiquidatableAccount]

**Returns:**
  IndexerLiquidationFeedData: The latest liquidation feed data.

IndexerLiquidationFeedData: The latest liquidation feed data.

**get_linked_signer_rate_limits(subaccount)[source]**
  Retrieves the rate limits for a linked signer of a specific subaccount.Return type:IndexerLinkedSignerRateLimitDataArgs:subaccount (str): The identifier of the subaccount.Returns:IndexerLinkedSignerRateLimitData: The rate limits for the linked signer of the specified subaccount.

Retrieves the rate limits for a linked signer of a specific subaccount.

**Return type:**
  IndexerLinkedSignerRateLimitData

IndexerLinkedSignerRateLimitData

**Args:**
  subaccount (str): The identifier of the subaccount.

subaccount (str): The identifier of the subaccount.

**Returns:**
  IndexerLinkedSignerRateLimitData: The rate limits for the linked signer of the specified subaccount.

IndexerLinkedSignerRateLimitData: The rate limits for the linked signer of the specified subaccount.

**get_subaccounts(params)[source]**
  Retrieves subaccounts via the indexer.Return type:IndexerSubaccountsDataArgs:params (IndexerSubaccountsParams): The filter parameters for retrieving subaccounts.Returns:IndexerSubaccountsData: List of subaccounts found.

Retrieves subaccounts via the indexer.

**Return type:**
  IndexerSubaccountsData

IndexerSubaccountsData

**Args:**
  params (IndexerSubaccountsParams): The filter parameters for retrieving subaccounts.

params (IndexerSubaccountsParams): The filter parameters for retrieving subaccounts.

**Returns:**
  IndexerSubaccountsData: List of subaccounts found.

IndexerSubaccountsData: List of subaccounts found.

**get_quote_price()[source]**
  Return type:IndexerQuotePriceData

**Return type:**
  IndexerQuotePriceData

IndexerQuotePriceData

**get_interest_and_funding_payments(params)[source]**
  Return type:IndexerInterestAndFundingData

**Return type:**
  IndexerInterestAndFundingData

IndexerInterestAndFundingData

**get_tickers(market_type=None)[source]**
  Return type:Dict[str,IndexerTickerInfo]

**Return type:**
  Dict[str,IndexerTickerInfo]

Dict[str,IndexerTickerInfo]

**get_perp_contracts_info()[source]**
  Return type:Dict[str,IndexerPerpContractInfo]

**Return type:**
  Dict[str,IndexerPerpContractInfo]

Dict[str,IndexerPerpContractInfo]

**get_historical_trades(ticker_id,limit,max_trade_id=None)[source]**
  Return type:List[IndexerTradeInfo]

**Return type:**
  List[IndexerTradeInfo]

List[IndexerTradeInfo]

**get_multi_subaccount_snapshots(params)[source]**
  Retrieves subaccount snapshots at specified timestamps.
Each snapshot is a view of the subaccount’s balances at that point in time,
with tracked variables for interest, funding, etc.Return type:IndexerAccountSnapshotsDataArgs:params (IndexerAccountSnapshotsParams): Parameters specifying subaccounts,timestamps, and whether to include isolated positions.Returns:IndexerAccountSnapshotsData: Dict mapping subaccount hex -> timestamp -> snapshot data.Each snapshot contains balances with trackedVars including netEntryUnrealized.

Retrieves subaccount snapshots at specified timestamps.
Each snapshot is a view of the subaccount’s balances at that point in time,
with tracked variables for interest, funding, etc.

**Return type:**
  IndexerAccountSnapshotsData

IndexerAccountSnapshotsData

**Args:**
  params (IndexerAccountSnapshotsParams): Parameters specifying subaccounts,timestamps, and whether to include isolated positions.

**params (IndexerAccountSnapshotsParams): Parameters specifying subaccounts,**
  timestamps, and whether to include isolated positions.

timestamps, and whether to include isolated positions.

**Returns:**
  IndexerAccountSnapshotsData: Dict mapping subaccount hex -> timestamp -> snapshot data.Each snapshot contains balances with trackedVars including netEntryUnrealized.

**IndexerAccountSnapshotsData: Dict mapping subaccount hex -> timestamp -> snapshot data.**
  Each snapshot contains balances with trackedVars including netEntryUnrealized.

Each snapshot contains balances with trackedVars including netEntryUnrealized.

## nado-protocol.indexer_client.types

**classnado_protocol.indexer_client.types.IndexerQueryType(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumEnumeration of query types available in the Indexer service.ORDERS='orders'MATCHES='matches'EVENTS='events'SUMMARY='summary'PRODUCTS='products'MARKET_SNAPSHOTS='market_snapshots'CANDLESTICKS='candlesticks'FUNDING_RATE='funding_rate'FUNDING_RATES='funding_rates'PERP_PRICES='price'ORACLE_PRICES='oracle_price'REWARDS='rewards'MAKER_STATISTICS='maker_statistics'LIQUIDATION_FEED='liquidation_feed'LINKED_SIGNER_RATE_LIMIT='linked_signer_rate_limit'REFERRAL_CODE='referral_code'SUBACCOUNTS='subaccounts'QUOTE_PRICE='quote_price'ACCOUNT_SNAPSHOTS='account_snapshots'INTEREST_AND_FUNDING='interest_and_funding'INK_AIRDROP='ink_airdrop'

Bases:StrEnum

Enumeration of query types available in the Indexer service.

**ORDERS='orders'**

**MATCHES='matches'**

**EVENTS='events'**

**SUMMARY='summary'**

**PRODUCTS='products'**

**MARKET_SNAPSHOTS='market_snapshots'**

**CANDLESTICKS='candlesticks'**

**FUNDING_RATE='funding_rate'**

**FUNDING_RATES='funding_rates'**

**PERP_PRICES='price'**

**ORACLE_PRICES='oracle_price'**

**REWARDS='rewards'**

**MAKER_STATISTICS='maker_statistics'**

**LIQUIDATION_FEED='liquidation_feed'**

**LINKED_SIGNER_RATE_LIMIT='linked_signer_rate_limit'**

**REFERRAL_CODE='referral_code'**

**SUBACCOUNTS='subaccounts'**

**QUOTE_PRICE='quote_price'**

**ACCOUNT_SNAPSHOTS='account_snapshots'**

**INTEREST_AND_FUNDING='interest_and_funding'**

**INK_AIRDROP='ink_airdrop'**

**classnado_protocol.indexer_client.types.IndexerBaseParams(**data)[source]**
  Bases:NadoBaseModelBase parameters for the indexer queries.idx:Optional[int]max_time:Optional[int]limit:Optional[int]classConfig[source]Bases:objectallow_population_by_field_name=True

Bases:NadoBaseModel

Base parameters for the indexer queries.

**idx:Optional[int]**

**max_time:Optional[int]**

**limit:Optional[int]**

**classConfig[source]**
  Bases:objectallow_population_by_field_name=True

Bases:object

**allow_population_by_field_name=True**

**classnado_protocol.indexer_client.types.IndexerSubaccountHistoricalOrdersParams(**data)[source]**
  Bases:IndexerBaseParamsParameters for querying historical orders by subaccounts.subaccounts:Optional[list[str]]product_ids:Optional[list[int]]trigger_types:Optional[list[str]]isolated:Optional[bool]classConfig[source]Bases:objectextra='forbid'

Bases:IndexerBaseParams

Parameters for querying historical orders by subaccounts.

**subaccounts:Optional[list[str]]**

**product_ids:Optional[list[int]]**

**trigger_types:Optional[list[str]]**

**isolated:Optional[bool]**

**classConfig[source]**
  Bases:objectextra='forbid'

Bases:object

**extra='forbid'**

**classnado_protocol.indexer_client.types.IndexerHistoricalOrdersByDigestParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying historical orders by digests.digests:list[str]classConfig[source]Bases:objectextra='forbid'

Bases:NadoBaseModel

Parameters for querying historical orders by digests.

**digests:list[str]**

**classConfig[source]**
  Bases:objectextra='forbid'

Bases:object

**extra='forbid'**

**classnado_protocol.indexer_client.types.IndexerMatchesParams(**data)[source]**
  Bases:IndexerBaseParamsParameters for querying matches.subaccounts:Optional[list[str]]product_ids:Optional[list[int]]isolated:Optional[bool]

Bases:IndexerBaseParams

Parameters for querying matches.

**subaccounts:Optional[list[str]]**

**product_ids:Optional[list[int]]**

**isolated:Optional[bool]**

**classnado_protocol.indexer_client.types.IndexerEventsRawLimit(**data)[source]**
  Bases:NadoBaseModelParameters for limiting by events count.raw:int

Bases:NadoBaseModel

Parameters for limiting by events count.

**raw:int**

**classnado_protocol.indexer_client.types.IndexerEventsTxsLimit(**data)[source]**
  Bases:NadoBaseModelParameters for limiting events by transaction count.txs:int

Bases:NadoBaseModel

Parameters for limiting events by transaction count.

**txs:int**

**classnado_protocol.indexer_client.types.IndexerEventsParams(**data)[source]**
  Bases:IndexerBaseParamsParameters for querying events.subaccounts:Optional[list[str]]product_ids:Optional[list[int]]event_types:Optional[list[IndexerEventType]]isolated:Optional[bool]limit:Union[IndexerEventsRawLimit,IndexerEventsTxsLimit,None]

Bases:IndexerBaseParams

Parameters for querying events.

**subaccounts:Optional[list[str]]**

**product_ids:Optional[list[int]]**

**event_types:Optional[list[IndexerEventType]]**

**isolated:Optional[bool]**

**limit:Union[IndexerEventsRawLimit,IndexerEventsTxsLimit,None]**

**classnado_protocol.indexer_client.types.IndexerProductSnapshotsParams(**data)[source]**
  Bases:IndexerBaseParamsParameters for querying product snapshots.product_id:int

Bases:IndexerBaseParams

Parameters for querying product snapshots.

**product_id:int**

**classnado_protocol.indexer_client.types.IndexerCandlesticksParams(**data)[source]**
  Bases:IndexerBaseParamsParameters for querying candlestick data.product_id:intgranularity:IndexerCandlesticksGranularityclassConfig[source]Bases:objectfields={'idx':{'exclude':True}}

Bases:IndexerBaseParams

Parameters for querying candlestick data.

**product_id:int**

**granularity:IndexerCandlesticksGranularity**

**classConfig[source]**
  Bases:objectfields={'idx':{'exclude':True}}

Bases:object

**fields={'idx':{'exclude':True}}**

**classnado_protocol.indexer_client.types.IndexerFundingRateParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying funding rates.product_id:int

Bases:NadoBaseModel

Parameters for querying funding rates.

**product_id:int**

**classnado_protocol.indexer_client.types.IndexerPerpPricesParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying perpetual prices.product_id:int

Bases:NadoBaseModel

Parameters for querying perpetual prices.

**product_id:int**

**classnado_protocol.indexer_client.types.IndexerOraclePricesParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying oracle prices.product_ids:list[int]

Bases:NadoBaseModel

Parameters for querying oracle prices.

**product_ids:list[int]**

**classnado_protocol.indexer_client.types.IndexerLiquidationFeedParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying liquidation feed.

Bases:NadoBaseModel

Parameters for querying liquidation feed.

**classnado_protocol.indexer_client.types.IndexerLinkedSignerRateLimitParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying linked signer rate limits.subaccount:str

Bases:NadoBaseModel

Parameters for querying linked signer rate limits.

**subaccount:str**

**classnado_protocol.indexer_client.types.IndexerSubaccountsParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying subaccounts.address:Optional[str]limit:Optional[int]start:Optional[int]

Bases:NadoBaseModel

Parameters for querying subaccounts.

**address:Optional[str]**

**limit:Optional[int]**

**start:Optional[int]**

**classnado_protocol.indexer_client.types.IndexerHistoricalOrdersRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying historical orders.orders:Union[IndexerSubaccountHistoricalOrdersParams,IndexerHistoricalOrdersByDigestParams]classConfig[source]Bases:objectsmart_union=True

Bases:NadoBaseModel

Request object for querying historical orders.

**orders:Union[IndexerSubaccountHistoricalOrdersParams,IndexerHistoricalOrdersByDigestParams]**

**classConfig[source]**
  Bases:objectsmart_union=True

Bases:object

**smart_union=True**

**classnado_protocol.indexer_client.types.IndexerMatchesRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying matches.matches:IndexerMatchesParams

Bases:NadoBaseModel

Request object for querying matches.

**matches:IndexerMatchesParams**

**classnado_protocol.indexer_client.types.IndexerEventsRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying events.events:IndexerEventsParams

Bases:NadoBaseModel

Request object for querying events.

**events:IndexerEventsParams**

**classnado_protocol.indexer_client.types.IndexerProductSnapshotsRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying product snapshots.products:IndexerProductSnapshotsParams

Bases:NadoBaseModel

Request object for querying product snapshots.

**products:IndexerProductSnapshotsParams**

**classnado_protocol.indexer_client.types.IndexerCandlesticksRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying candlestick data.candlesticks:IndexerCandlesticksParams

Bases:NadoBaseModel

Request object for querying candlestick data.

**candlesticks:IndexerCandlesticksParams**

**classnado_protocol.indexer_client.types.IndexerFundingRateRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying funding rates.funding_rate:IndexerFundingRateParams

Bases:NadoBaseModel

Request object for querying funding rates.

**funding_rate:IndexerFundingRateParams**

**classnado_protocol.indexer_client.types.IndexerFundingRatesRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying funding rates.funding_rates:IndexerFundingRatesParams

Bases:NadoBaseModel

Request object for querying funding rates.

**funding_rates:IndexerFundingRatesParams**

**classnado_protocol.indexer_client.types.IndexerPerpPricesRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying perpetual prices.price:IndexerPerpPricesParams

Bases:NadoBaseModel

Request object for querying perpetual prices.

**price:IndexerPerpPricesParams**

**classnado_protocol.indexer_client.types.IndexerOraclePricesRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying oracle prices.oracle_price:IndexerOraclePricesParams

Bases:NadoBaseModel

Request object for querying oracle prices.

**oracle_price:IndexerOraclePricesParams**

**classnado_protocol.indexer_client.types.IndexerLiquidationFeedRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying liquidation feed.liquidation_feed:IndexerLiquidationFeedParams

Bases:NadoBaseModel

Request object for querying liquidation feed.

**liquidation_feed:IndexerLiquidationFeedParams**

**classnado_protocol.indexer_client.types.IndexerLinkedSignerRateLimitRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying linked signer rate limits.linked_signer_rate_limit:IndexerLinkedSignerRateLimitParams

Bases:NadoBaseModel

Request object for querying linked signer rate limits.

**linked_signer_rate_limit:IndexerLinkedSignerRateLimitParams**

**classnado_protocol.indexer_client.types.IndexerSubaccountsRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying subaccounts.subaccounts:IndexerSubaccountsParams

Bases:NadoBaseModel

Request object for querying subaccounts.

**subaccounts:IndexerSubaccountsParams**

**classnado_protocol.indexer_client.types.IndexerHistoricalOrdersData(**data)[source]**
  Bases:NadoBaseModelData object for historical orders.orders:list[IndexerHistoricalOrder]

Bases:NadoBaseModel

Data object for historical orders.

**orders:list[IndexerHistoricalOrder]**

**classnado_protocol.indexer_client.types.IndexerMatchesData(**data)[source]**
  Bases:NadoBaseModelData object for matches.matches:list[IndexerMatch]txs:list[IndexerTx]

Bases:NadoBaseModel

Data object for matches.

**matches:list[IndexerMatch]**

**txs:list[IndexerTx]**

**classnado_protocol.indexer_client.types.IndexerEventsData(**data)[source]**
  Bases:NadoBaseModelData object for events.events:list[IndexerEvent]txs:list[IndexerTx]

Bases:NadoBaseModel

Data object for events.

**events:list[IndexerEvent]**

**txs:list[IndexerTx]**

**classnado_protocol.indexer_client.types.IndexerProductSnapshotsData(**data)[source]**
  Bases:NadoBaseModelData object for product snapshots.products:list[IndexerProduct]txs:list[IndexerTx]

Bases:NadoBaseModel

Data object for product snapshots.

**products:list[IndexerProduct]**

**txs:list[IndexerTx]**

**classnado_protocol.indexer_client.types.IndexerCandlesticksData(**data)[source]**
  Bases:NadoBaseModelData object for candlestick data.candlesticks:list[IndexerCandlestick]

Bases:NadoBaseModel

Data object for candlestick data.

**candlesticks:list[IndexerCandlestick]**

**classnado_protocol.indexer_client.types.IndexerFundingRateData(**data)[source]**
  Bases:NadoBaseModelData object for funding rates.product_id:intfunding_rate_x18:strupdate_time:str

Bases:NadoBaseModel

Data object for funding rates.

**product_id:int**

**funding_rate_x18:str**

**update_time:str**

**classnado_protocol.indexer_client.types.IndexerPerpPricesData(**data)[source]**
  Bases:NadoBaseModelData object for perpetual prices.product_id:intindex_price_x18:strmark_price_x18:strupdate_time:str

Bases:NadoBaseModel

Data object for perpetual prices.

**product_id:int**

**index_price_x18:str**

**mark_price_x18:str**

**update_time:str**

**classnado_protocol.indexer_client.types.IndexerOraclePricesData(**data)[source]**
  Bases:NadoBaseModelData object for oracle prices.prices:list[IndexerOraclePrice]

Bases:NadoBaseModel

Data object for oracle prices.

**prices:list[IndexerOraclePrice]**

**classnado_protocol.indexer_client.types.IndexerLinkedSignerRateLimitData(**data)[source]**
  Bases:NadoBaseModelData object for linked signer rate limits.remaining_tx:strtotal_tx_limit:strwait_time:intsigner:str

Bases:NadoBaseModel

Data object for linked signer rate limits.

**remaining_tx:str**

**total_tx_limit:str**

**wait_time:int**

**signer:str**

**classnado_protocol.indexer_client.types.IndexerSubaccountsData(**data)[source]**
  Bases:NadoBaseModelData object for subaccounts response from the indexer.subaccounts:list[IndexerSubaccount]

Bases:NadoBaseModel

Data object for subaccounts response from the indexer.

**subaccounts:list[IndexerSubaccount]**

**classnado_protocol.indexer_client.types.IndexerQuotePriceData(**data)[source]**
  Bases:NadoBaseModelData object for the quote price response from the indexer.price_x18:str

Bases:NadoBaseModel

Data object for the quote price response from the indexer.

**price_x18:str**

**classnado_protocol.indexer_client.types.IndexerResponse(**data)[source]**
  Bases:NadoBaseModelRepresents the response returned by the indexer.Attributes:data (IndexerResponseData): The data contained in the response.data:Union[IndexerHistoricalOrdersData,IndexerMatchesData,IndexerEventsData,IndexerProductSnapshotsData,IndexerCandlesticksData,IndexerFundingRateData,IndexerPerpPricesData,IndexerOraclePricesData,IndexerLinkedSignerRateLimitData,IndexerSubaccountsData,IndexerQuotePriceData,IndexerMarketSnapshotsData,IndexerInterestAndFundingData,list[IndexerLiquidatableAccount],Dict[str,IndexerFundingRateData],IndexerAccountSnapshotsData,IndexerInkAirdropData]

Bases:NadoBaseModel

Represents the response returned by the indexer.

**Attributes:**
  data (IndexerResponseData): The data contained in the response.

data (IndexerResponseData): The data contained in the response.

**data:Union[IndexerHistoricalOrdersData,IndexerMatchesData,IndexerEventsData,IndexerProductSnapshotsData,IndexerCandlesticksData,IndexerFundingRateData,IndexerPerpPricesData,IndexerOraclePricesData,IndexerLinkedSignerRateLimitData,IndexerSubaccountsData,IndexerQuotePriceData,IndexerMarketSnapshotsData,IndexerInterestAndFundingData,list[IndexerLiquidatableAccount],Dict[str,IndexerFundingRateData],IndexerAccountSnapshotsData,IndexerInkAirdropData]**

**classnado_protocol.indexer_client.types.IndexerEventType(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumLIQUIDATE_SUBACCOUNT='liquidate_subaccount'DEPOSIT_COLLATERAL='deposit_collateral'WITHDRAW_COLLATERAL='withdraw_collateral'SETTLE_PNL='settle_pnl'MATCH_ORDERS='match_orders'MATCH_ORDER_A_M_M='match_order_a_m_m'SWAP_AMM='swap_a_m_m'MINT_NLP='mint_nlp'BURN_NLP='burn_nlp'MANUAL_ASSERT='manual_assert'LINK_SIGNER='link_signer'TRANSFER_QUOTE='transfer_quote'CREATE_ISOLATED_SUBACCOUNT='create_isolated_subaccount'

Bases:StrEnum

**LIQUIDATE_SUBACCOUNT='liquidate_subaccount'**

**DEPOSIT_COLLATERAL='deposit_collateral'**

**WITHDRAW_COLLATERAL='withdraw_collateral'**

**SETTLE_PNL='settle_pnl'**

**MATCH_ORDERS='match_orders'**

**MATCH_ORDER_A_M_M='match_order_a_m_m'**

**SWAP_AMM='swap_a_m_m'**

**MINT_NLP='mint_nlp'**

**BURN_NLP='burn_nlp'**

**MANUAL_ASSERT='manual_assert'**

**LINK_SIGNER='link_signer'**

**TRANSFER_QUOTE='transfer_quote'**

**CREATE_ISOLATED_SUBACCOUNT='create_isolated_subaccount'**

**classnado_protocol.indexer_client.types.IndexerCandlesticksGranularity(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:IntEnumONE_MINUTE=60FIVE_MINUTES=300FIFTEEN_MINUTES=900ONE_HOUR=3600TWO_HOURS=7200FOUR_HOURS=14400ONE_DAY=86400ONE_WEEK=604800FOUR_WEEKS=2419200

Bases:IntEnum

**ONE_MINUTE=60**

**FIVE_MINUTES=300**

**FIFTEEN_MINUTES=900**

**ONE_HOUR=3600**

**TWO_HOURS=7200**

**FOUR_HOURS=14400**

**ONE_DAY=86400**

**ONE_WEEK=604800**

**FOUR_WEEKS=2419200**

**classnado_protocol.indexer_client.types.IndexerBaseModel(**data)[source]**
  Bases:NadoBaseModelsubmission_idx:strtimestamp:Optional[str]

Bases:NadoBaseModel

**submission_idx:str**

**timestamp:Optional[str]**

**classnado_protocol.indexer_client.types.IndexerBaseOrder(**data)[source]**
  Bases:NadoBaseModelsender:strpriceX18:stramount:strexpiration:Union[str,int]nonce:Union[str,int]

Bases:NadoBaseModel

**sender:str**

**priceX18:str**

**amount:str**

**expiration:Union[str,int]**

**nonce:Union[str,int]**

**classnado_protocol.indexer_client.types.IndexerOrderFill(**data)[source]**
  Bases:IndexerBaseModeldigest:strbase_filled:strquote_filled:strfee:str

Bases:IndexerBaseModel

**digest:str**

**base_filled:str**

**quote_filled:str**

**fee:str**

**classnado_protocol.indexer_client.types.IndexerHistoricalOrder(**data)[source]**
  Bases:IndexerOrderFillsubaccount:strproduct_id:intamount:strprice_x18:strexpiration:strnonce:strisolated:bool

Bases:IndexerOrderFill

**subaccount:str**

**product_id:int**

**amount:str**

**price_x18:str**

**expiration:str**

**nonce:str**

**isolated:bool**

**classnado_protocol.indexer_client.types.IndexerSignedOrder(**data)[source]**
  Bases:NadoBaseModelorder:IndexerBaseOrdersignature:str

Bases:NadoBaseModel

**order:IndexerBaseOrder**

**signature:str**

**classnado_protocol.indexer_client.types.IndexerMatch(**data)[source]**
  Bases:IndexerOrderFillorder:IndexerBaseOrdercumulative_fee:strcumulative_base_filled:strcumulative_quote_filled:strisolated:bool

Bases:IndexerOrderFill

**order:IndexerBaseOrder**

**cumulative_fee:str**

**cumulative_base_filled:str**

**cumulative_quote_filled:str**

**isolated:bool**

**classnado_protocol.indexer_client.types.IndexerMatchOrdersTxData(**data)[source]**
  Bases:NadoBaseModelproduct_id:intamm:booltaker:IndexerSignedOrdermaker:IndexerSignedOrder

Bases:NadoBaseModel

**product_id:int**

**amm:bool**

**taker:IndexerSignedOrder**

**maker:IndexerSignedOrder**

**classnado_protocol.indexer_client.types.IndexerMatchOrdersTx(**data)[source]**
  Bases:NadoBaseModelmatch_orders:IndexerMatchOrdersTxData

Bases:NadoBaseModel

**match_orders:IndexerMatchOrdersTxData**

**classnado_protocol.indexer_client.types.IndexerWithdrawCollateralTxData(**data)[source]**
  Bases:NadoBaseModelsender:strproduct_id:intamount:strnonce:int

Bases:NadoBaseModel

**sender:str**

**product_id:int**

**amount:str**

**nonce:int**

**classnado_protocol.indexer_client.types.IndexerWithdrawCollateralTx(**data)[source]**
  Bases:NadoBaseModelwithdraw_collateral:IndexerWithdrawCollateralTxData

Bases:NadoBaseModel

**withdraw_collateral:IndexerWithdrawCollateralTxData**

**classnado_protocol.indexer_client.types.IndexerLiquidateSubaccountTxData(**data)[source]**
  Bases:NadoBaseModelsender:strliquidatee:strmode:inthealth_group:intamount:strnonce:int

Bases:NadoBaseModel

**sender:str**

**liquidatee:str**

**mode:int**

**health_group:int**

**amount:str**

**nonce:int**

**classnado_protocol.indexer_client.types.IndexerLiquidateSubaccountTx(**data)[source]**
  Bases:NadoBaseModelliquidate_subaccount:IndexerLiquidateSubaccountTxData

Bases:NadoBaseModel

**liquidate_subaccount:IndexerLiquidateSubaccountTxData**

**classnado_protocol.indexer_client.types.IndexerMintNlpTxData(**data)[source]**
  Bases:NadoBaseModelsender:strquote_amount:strnonce:int

Bases:NadoBaseModel

**sender:str**

**quote_amount:str**

**nonce:int**

**classnado_protocol.indexer_client.types.IndexerMintNlpTx(**data)[source]**
  Bases:NadoBaseModelmint_nlp:IndexerMintNlpTxData

Bases:NadoBaseModel

**mint_nlp:IndexerMintNlpTxData**

**classnado_protocol.indexer_client.types.IndexerBurnNlpTxData(**data)[source]**
  Bases:NadoBaseModelsender:strnlp_amount:strnonce:int

Bases:NadoBaseModel

**sender:str**

**nlp_amount:str**

**nonce:int**

**classnado_protocol.indexer_client.types.IndexerBurnNlpTx(**data)[source]**
  Bases:NadoBaseModelburn_nlp:IndexerBurnNlpTxData

Bases:NadoBaseModel

**burn_nlp:IndexerBurnNlpTxData**

**classnado_protocol.indexer_client.types.IndexerTx(**data)[source]**
  Bases:IndexerBaseModeltx:Union[IndexerMatchOrdersTx,IndexerWithdrawCollateralTx,IndexerLiquidateSubaccountTx,IndexerMintNlpTx,IndexerBurnNlpTx,Any]

Bases:IndexerBaseModel

**tx:Union[IndexerMatchOrdersTx,IndexerWithdrawCollateralTx,IndexerLiquidateSubaccountTx,IndexerMintNlpTx,IndexerBurnNlpTx,Any]**

**classnado_protocol.indexer_client.types.IndexerSpotProductBalanceData(**data)[source]**
  Bases:NadoBaseModelspot:SpotProductBalance

Bases:NadoBaseModel

**spot:SpotProductBalance**

**classnado_protocol.indexer_client.types.IndexerSpotProductData(**data)[source]**
  Bases:NadoBaseModelspot:SpotProduct

Bases:NadoBaseModel

**spot:SpotProduct**

**classnado_protocol.indexer_client.types.IndexerPerpProductData(**data)[source]**
  Bases:NadoBaseModelperp:PerpProduct

Bases:NadoBaseModel

**perp:PerpProduct**

**classnado_protocol.indexer_client.types.IndexerEventTrackedData(**data)[source]**
  Bases:NadoBaseModelnet_interest_unrealized:strnet_interest_cumulative:strnet_funding_unrealized:strnet_funding_cumulative:strnet_entry_unrealized:strnet_entry_cumulative:strquote_volume_cumulative:str

Bases:NadoBaseModel

**net_interest_unrealized:str**

**net_interest_cumulative:str**

**net_funding_unrealized:str**

**net_funding_cumulative:str**

**net_entry_unrealized:str**

**net_entry_cumulative:str**

**quote_volume_cumulative:str**

**classnado_protocol.indexer_client.types.IndexerEvent(**data)[source]**
  Bases:IndexerBaseModel,IndexerEventTrackedDatasubaccount:strproduct_id:intevent_type:IndexerEventTypeproduct:Union[IndexerSpotProductData,IndexerPerpProductData]pre_balance:Union[IndexerSpotProductBalanceData,IndexerPerpProductBalanceData]post_balance:Union[IndexerSpotProductBalanceData,IndexerPerpProductBalanceData]isolated:boolisolated_product_id:Optional[int]

Bases:IndexerBaseModel,IndexerEventTrackedData

**subaccount:str**

**product_id:int**

**event_type:IndexerEventType**

**product:Union[IndexerSpotProductData,IndexerPerpProductData]**

**pre_balance:Union[IndexerSpotProductBalanceData,IndexerPerpProductBalanceData]**

**post_balance:Union[IndexerSpotProductBalanceData,IndexerPerpProductBalanceData]**

**isolated:bool**

**isolated_product_id:Optional[int]**

**classnado_protocol.indexer_client.types.IndexerProduct(**data)[source]**
  Bases:IndexerBaseModelproduct_id:intproduct:Union[IndexerSpotProductData,IndexerPerpProductData]

Bases:IndexerBaseModel

**product_id:int**

**product:Union[IndexerSpotProductData,IndexerPerpProductData]**

**classnado_protocol.indexer_client.types.IndexerCandlestick(**data)[source]**
  Bases:IndexerBaseModelproduct_id:intgranularity:intopen_x18:strhigh_x18:strlow_x18:strclose_x18:strvolume:str

Bases:IndexerBaseModel

**product_id:int**

**granularity:int**

**open_x18:str**

**high_x18:str**

**low_x18:str**

**close_x18:str**

**volume:str**

**classnado_protocol.indexer_client.types.IndexerOraclePrice(**data)[source]**
  Bases:NadoBaseModelproduct_id:intoracle_price_x18:strupdate_time:str

Bases:NadoBaseModel

**product_id:int**

**oracle_price_x18:str**

**update_time:str**

**classnado_protocol.indexer_client.types.IndexerAddressReward(**data)[source]**
  Bases:NadoBaseModelproduct_id:intq_score:strsum_q_min:struptime:intmaker_volume:strtaker_volume:strmaker_fee:strtaker_fee:strmaker_tokens:strtaker_tokens:strtaker_referral_tokens:strrebates:str

Bases:NadoBaseModel

**product_id:int**

**q_score:str**

**sum_q_min:str**

**uptime:int**

**maker_volume:str**

**taker_volume:str**

**maker_fee:str**

**taker_fee:str**

**maker_tokens:str**

**taker_tokens:str**

**taker_referral_tokens:str**

**rebates:str**

**classnado_protocol.indexer_client.types.IndexerGlobalRewards(**data)[source]**
  Bases:NadoBaseModelproduct_id:intreward_coefficient:strq_scores:strmaker_volumes:strtaker_volumes:strmaker_fees:strtaker_fees:strmaker_tokens:strtaker_tokens:str

Bases:NadoBaseModel

**product_id:int**

**reward_coefficient:str**

**q_scores:str**

**maker_volumes:str**

**taker_volumes:str**

**maker_fees:str**

**taker_fees:str**

**maker_tokens:str**

**taker_tokens:str**

**classnado_protocol.indexer_client.types.IndexerTokenReward(**data)[source]**
  Bases:NadoBaseModelepoch:intstart_time:strperiod:straddress_rewards:list[IndexerAddressReward]global_rewards:list[IndexerGlobalRewards]

Bases:NadoBaseModel

**epoch:int**

**start_time:str**

**period:str**

**address_rewards:list[IndexerAddressReward]**

**global_rewards:list[IndexerGlobalRewards]**

**classnado_protocol.indexer_client.types.IndexerMarketMakerData(**data)[source]**
  Bases:NadoBaseModeltimestamp:strmaker_fee:struptime:strsum_q_min:strq_score:strmaker_share:strexpected_maker_reward:str

Bases:NadoBaseModel

**timestamp:str**

**maker_fee:str**

**uptime:str**

**sum_q_min:str**

**q_score:str**

**maker_share:str**

**expected_maker_reward:str**

**classnado_protocol.indexer_client.types.IndexerMarketMaker(**data)[source]**
  Bases:NadoBaseModeladdress:strdata:list[IndexerMarketMakerData]

Bases:NadoBaseModel

**address:str**

**data:list[IndexerMarketMakerData]**

**classnado_protocol.indexer_client.types.IndexerLiquidatableAccount(**data)[source]**
  Bases:NadoBaseModelsubaccount:strupdate_time:int

Bases:NadoBaseModel

**subaccount:str**

**update_time:int**

**classnado_protocol.indexer_client.types.IndexerSubaccount(**data)[source]**
  Bases:NadoBaseModelid:strsubaccount:straddress:strsubaccount_name:strcreated_at:strisolated:bool

Bases:NadoBaseModel

**id:str**

**subaccount:str**

**address:str**

**subaccount_name:str**

**created_at:str**

**isolated:bool**

**classnado_protocol.indexer_client.types.IndexerInterestAndFundingParams(**data)[source]**
  Bases:NadoBaseModelParameters for querying interest and funding payments.subaccount:strproduct_ids:list[int]max_idx:Union[str,int,None]limit:int

Bases:NadoBaseModel

Parameters for querying interest and funding payments.

**subaccount:str**

**product_ids:list[int]**

**max_idx:Union[str,int,None]**

**limit:int**

**classnado_protocol.indexer_client.types.IndexerInterestAndFundingRequest(**data)[source]**
  Bases:NadoBaseModelRequest object for querying Interest and funding payments.interest_and_funding:IndexerInterestAndFundingParams

Bases:NadoBaseModel

Request object for querying Interest and funding payments.

**interest_and_funding:IndexerInterestAndFundingParams**

**classnado_protocol.indexer_client.types.IndexerInterestAndFundingData(**data)[source]**
  Bases:NadoBaseModelData object for the interest and funding payments response from the indexer.interest_payments:list[IndexerPayment]funding_payments:list[IndexerPayment]next_idx:str

Bases:NadoBaseModel

Data object for the interest and funding payments response from the indexer.

**interest_payments:list[IndexerPayment]**

**funding_payments:list[IndexerPayment]**

**next_idx:str**

**classnado_protocol.indexer_client.types.IndexerTickerInfo(**data)[source]**
  Bases:NadoBaseModelticker_id:strbase_currency:strquote_currency:strlast_price:floatbase_volume:floatquote_volume:floatprice_change_percent_24h:float

Bases:NadoBaseModel

**ticker_id:str**

**base_currency:str**

**quote_currency:str**

**last_price:float**

**base_volume:float**

**quote_volume:float**

**price_change_percent_24h:float**

**classnado_protocol.indexer_client.types.IndexerPerpContractInfo(**data)[source]**
  Bases:IndexerTickerInfoproduct_type:strcontract_price:floatcontract_price_currency:stropen_interest:floatopen_interest_usd:floatindex_price:floatmark_price:floatfunding_rate:floatnext_funding_rate_timestamp:int

Bases:IndexerTickerInfo

**product_type:str**

**contract_price:float**

**contract_price_currency:str**

**open_interest:float**

**open_interest_usd:float**

**index_price:float**

**mark_price:float**

**funding_rate:float**

**next_funding_rate_timestamp:int**

**classnado_protocol.indexer_client.types.IndexerTradeInfo(**data)[source]**
  Bases:NadoBaseModelticker_id:strtrade_id:intprice:floatbase_filled:floatquote_filled:floattimestamp:inttrade_type:str

Bases:NadoBaseModel

**ticker_id:str**

**trade_id:int**

**price:float**

**base_filled:float**

**quote_filled:float**

**timestamp:int**

**trade_type:str**

## nado-protocol.contracts

**classnado_protocol.contracts.NadoContractsContext(**data)[source]**
  Bases:BaseModelHolds the context for various Nado contracts.Attributes:endpoint_addr (str): The endpoint address.querier_addr (str): The querier address.spot_engine_addr (Optional[str]): The spot engine address. This may be None.perp_engine_addr (Optional[str]): The perp engine address. This may be None.clearinghouse_addr (Optional[str]): The clearinghouse address. This may be None.airdrop_addr (Optional[str]): The airdrop address. This may be None.staking_addr (Optional[str]): The staking address. This may be None.foundation_rewards_airdrop_addr (Optional[str]): The Foundation Rewards airdrop address of the corresponding chain (e.g: Ink airdrop for Ink). This may be None.network:Optional[NadoNetwork]endpoint_addr:strquerier_addr:strspot_engine_addr:Optional[str]perp_engine_addr:Optional[str]clearinghouse_addr:Optional[str]airdrop_addr:Optional[str]staking_addr:Optional[str]foundation_rewards_airdrop_addr:Optional[str]

Bases:BaseModel

Holds the context for various Nado contracts.

**Attributes:**
  endpoint_addr (str): The endpoint address.querier_addr (str): The querier address.spot_engine_addr (Optional[str]): The spot engine address. This may be None.perp_engine_addr (Optional[str]): The perp engine address. This may be None.clearinghouse_addr (Optional[str]): The clearinghouse address. This may be None.airdrop_addr (Optional[str]): The airdrop address. This may be None.staking_addr (Optional[str]): The staking address. This may be None.foundation_rewards_airdrop_addr (Optional[str]): The Foundation Rewards airdrop address of the corresponding chain (e.g: Ink airdrop for Ink). This may be None.

endpoint_addr (str): The endpoint address.

querier_addr (str): The querier address.

spot_engine_addr (Optional[str]): The spot engine address. This may be None.

perp_engine_addr (Optional[str]): The perp engine address. This may be None.

clearinghouse_addr (Optional[str]): The clearinghouse address. This may be None.

airdrop_addr (Optional[str]): The airdrop address. This may be None.

staking_addr (Optional[str]): The staking address. This may be None.

foundation_rewards_airdrop_addr (Optional[str]): The Foundation Rewards airdrop address of the corresponding chain (e.g: Ink airdrop for Ink). This may be None.

**network:Optional[NadoNetwork]**

**endpoint_addr:str**

**querier_addr:str**

**spot_engine_addr:Optional[str]**

**perp_engine_addr:Optional[str]**

**clearinghouse_addr:Optional[str]**

**airdrop_addr:Optional[str]**

**staking_addr:Optional[str]**

**foundation_rewards_airdrop_addr:Optional[str]**

**classnado_protocol.contracts.NadoContracts(node_url,contracts_context)[source]**
  Bases:objectEncapsulates the set of Nado contracts required for querying and executing.__init__(node_url,contracts_context)[source]Initialize a NadoContracts instance.This will set up the Web3 instance and contract addresses for querying and executing the Nado contracts.
It will also load and parse the ABI for the given contracts.Args:node_url (str): The Ethereum node URL.contracts_context (NadoContractsContext): The Nado contracts context, holding the relevant addresses.network:Optional[NadoNetwork]w3:Web3contracts_context:NadoContractsContextquerier:Contractendpoint:Contractclearinghouse:Optional[Contract]spot_engine:Optional[Contract]perp_engine:Optional[Contract]staking:Optional[Contract]airdrop:Optional[Contract]foundation_rewards_airdrop:Optional[Contract]deposit_collateral(params,signer)[source]Deposits a specified amount of collateral into a spot product.Return type:strArgs:params (DepositCollateralParams): The parameters for depositing collateral.signer (LocalAccount): The account that will sign the deposit transaction.Returns:str: The transaction hash of the deposit operation.approve_allowance(erc20,amount,signer,to=None)[source]Approves a specified amount of allowance for the ERC20 token contract.Args:erc20 (Contract): The ERC20 token contract.amount (int): The amount of the ERC20 token to be approved.signer (LocalAccount): The account that will sign the approval transaction.to (Optional[str]): When specified, approves allowance to the provided contract address, otherwise it approves it to Nado’s Endpoint.Returns:str: The transaction hash of the approval operation.claim(epoch,amount_to_claim,total_claimable_amount,merkle_proof,signer)[source]Return type:strclaim_and_stake(epoch,amount_to_claim,total_claimable_amount,merkle_proof,signer)[source]Return type:strstake(amount,signer)[source]Return type:strunstake(amount,signer)[source]Return type:strwithdraw_unstaked(signer)[source]Return type:strclaim_usdc_rewards(signer)[source]Return type:strclaim_and_stake_usdc_rewards(signer)[source]Return type:strclaim_foundation_rewards(claim_proofs,signer)[source]Return type:strget_token_contract_for_product(product_id)[source]Returns the ERC20 token contract for a given product.Return type:ContractArgs:product_id (int): The ID of the product for which to get the ERC20 token contract.Returns:Contract: The ERC20 token contract for the specified product.Raises:InvalidProductId: If the provided product ID is not valid.execute(func,signer)[source]Executes a smart contract function.This method builds a transaction for a given contract function, signs the transaction with the provided signer’s private key,
sends the raw signed transaction to the network, and waits for the transaction to be mined.Return type:strArgs:func (ContractFunction): The contract function to be executed.signer (LocalAccount): The local account object that will sign the transaction. It should contain the private key.Returns:str: The hexadecimal representation of the transaction hash.Raises:ValueError: If the transaction is invalid, the method will not catch the error.
TimeExhausted: If the transaction receipt isn’t available within the timeout limit set by the Web3 provider.

Bases:object

Encapsulates the set of Nado contracts required for querying and executing.

**__init__(node_url,contracts_context)[source]**
  Initialize a NadoContracts instance.This will set up the Web3 instance and contract addresses for querying and executing the Nado contracts.
It will also load and parse the ABI for the given contracts.Args:node_url (str): The Ethereum node URL.contracts_context (NadoContractsContext): The Nado contracts context, holding the relevant addresses.

Initialize a NadoContracts instance.

This will set up the Web3 instance and contract addresses for querying and executing the Nado contracts.
It will also load and parse the ABI for the given contracts.

**Args:**
  node_url (str): The Ethereum node URL.contracts_context (NadoContractsContext): The Nado contracts context, holding the relevant addresses.

node_url (str): The Ethereum node URL.

contracts_context (NadoContractsContext): The Nado contracts context, holding the relevant addresses.

**network:Optional[NadoNetwork]**

**w3:Web3**

**contracts_context:NadoContractsContext**

**querier:Contract**

**endpoint:Contract**

**clearinghouse:Optional[Contract]**

**spot_engine:Optional[Contract]**

**perp_engine:Optional[Contract]**

**staking:Optional[Contract]**

**airdrop:Optional[Contract]**

**foundation_rewards_airdrop:Optional[Contract]**

**deposit_collateral(params,signer)[source]**
  Deposits a specified amount of collateral into a spot product.Return type:strArgs:params (DepositCollateralParams): The parameters for depositing collateral.signer (LocalAccount): The account that will sign the deposit transaction.Returns:str: The transaction hash of the deposit operation.

Deposits a specified amount of collateral into a spot product.

**Return type:**
  str

str

**Args:**
  params (DepositCollateralParams): The parameters for depositing collateral.signer (LocalAccount): The account that will sign the deposit transaction.

params (DepositCollateralParams): The parameters for depositing collateral.

signer (LocalAccount): The account that will sign the deposit transaction.

**Returns:**
  str: The transaction hash of the deposit operation.

str: The transaction hash of the deposit operation.

**approve_allowance(erc20,amount,signer,to=None)[source]**
  Approves a specified amount of allowance for the ERC20 token contract.Args:erc20 (Contract): The ERC20 token contract.amount (int): The amount of the ERC20 token to be approved.signer (LocalAccount): The account that will sign the approval transaction.to (Optional[str]): When specified, approves allowance to the provided contract address, otherwise it approves it to Nado’s Endpoint.Returns:str: The transaction hash of the approval operation.

Approves a specified amount of allowance for the ERC20 token contract.

**Args:**
  erc20 (Contract): The ERC20 token contract.amount (int): The amount of the ERC20 token to be approved.signer (LocalAccount): The account that will sign the approval transaction.to (Optional[str]): When specified, approves allowance to the provided contract address, otherwise it approves it to Nado’s Endpoint.

erc20 (Contract): The ERC20 token contract.

amount (int): The amount of the ERC20 token to be approved.

signer (LocalAccount): The account that will sign the approval transaction.

to (Optional[str]): When specified, approves allowance to the provided contract address, otherwise it approves it to Nado’s Endpoint.

**Returns:**
  str: The transaction hash of the approval operation.

str: The transaction hash of the approval operation.

**claim(epoch,amount_to_claim,total_claimable_amount,merkle_proof,signer)[source]**
  Return type:str

**Return type:**
  str

str

**claim_and_stake(epoch,amount_to_claim,total_claimable_amount,merkle_proof,signer)[source]**
  Return type:str

**Return type:**
  str

str

**stake(amount,signer)[source]**
  Return type:str

**Return type:**
  str

str

**unstake(amount,signer)[source]**
  Return type:str

**Return type:**
  str

str

**withdraw_unstaked(signer)[source]**
  Return type:str

**Return type:**
  str

str

**claim_usdc_rewards(signer)[source]**
  Return type:str

**Return type:**
  str

str

**claim_and_stake_usdc_rewards(signer)[source]**
  Return type:str

**Return type:**
  str

str

**claim_foundation_rewards(claim_proofs,signer)[source]**
  Return type:str

**Return type:**
  str

str

**get_token_contract_for_product(product_id)[source]**
  Returns the ERC20 token contract for a given product.Return type:ContractArgs:product_id (int): The ID of the product for which to get the ERC20 token contract.Returns:Contract: The ERC20 token contract for the specified product.Raises:InvalidProductId: If the provided product ID is not valid.

Returns the ERC20 token contract for a given product.

**Return type:**
  Contract

Contract

**Args:**
  product_id (int): The ID of the product for which to get the ERC20 token contract.

product_id (int): The ID of the product for which to get the ERC20 token contract.

**Returns:**
  Contract: The ERC20 token contract for the specified product.

Contract: The ERC20 token contract for the specified product.

**Raises:**
  InvalidProductId: If the provided product ID is not valid.

InvalidProductId: If the provided product ID is not valid.

**execute(func,signer)[source]**
  Executes a smart contract function.This method builds a transaction for a given contract function, signs the transaction with the provided signer’s private key,
sends the raw signed transaction to the network, and waits for the transaction to be mined.Return type:strArgs:func (ContractFunction): The contract function to be executed.signer (LocalAccount): The local account object that will sign the transaction. It should contain the private key.Returns:str: The hexadecimal representation of the transaction hash.Raises:ValueError: If the transaction is invalid, the method will not catch the error.
TimeExhausted: If the transaction receipt isn’t available within the timeout limit set by the Web3 provider.

Executes a smart contract function.

This method builds a transaction for a given contract function, signs the transaction with the provided signer’s private key,
sends the raw signed transaction to the network, and waits for the transaction to be mined.

**Return type:**
  str

str

**Args:**
  func (ContractFunction): The contract function to be executed.signer (LocalAccount): The local account object that will sign the transaction. It should contain the private key.

func (ContractFunction): The contract function to be executed.

signer (LocalAccount): The local account object that will sign the transaction. It should contain the private key.

**Returns:**
  str: The hexadecimal representation of the transaction hash.

str: The hexadecimal representation of the transaction hash.

**Raises:**
  ValueError: If the transaction is invalid, the method will not catch the error.
TimeExhausted: If the transaction receipt isn’t available within the timeout limit set by the Web3 provider.

ValueError: If the transaction is invalid, the method will not catch the error.
TimeExhausted: If the transaction receipt isn’t available within the timeout limit set by the Web3 provider.

**classnado_protocol.contracts.DepositCollateralParams(**data)[source]**
  Bases:NadoBaseModelClass representing parameters for depositing collateral in the Nado protocol.Attributes:subaccount_name (str): The name of the subaccount.product_id (int): The ID of the spot product to deposit collateral for.amount (int): The amount of collateral to be deposited.referral_code (Optional[str]): Use this to indicate you were referred by existing member.subaccount_name:strproduct_id:intamount:intreferral_code:Optional[str]

Bases:NadoBaseModel

Class representing parameters for depositing collateral in the Nado protocol.

**Attributes:**
  subaccount_name (str): The name of the subaccount.product_id (int): The ID of the spot product to deposit collateral for.amount (int): The amount of collateral to be deposited.referral_code (Optional[str]): Use this to indicate you were referred by existing member.

subaccount_name (str): The name of the subaccount.

product_id (int): The ID of the spot product to deposit collateral for.

amount (int): The amount of collateral to be deposited.

referral_code (Optional[str]): Use this to indicate you were referred by existing member.

**subaccount_name:str**

**product_id:int**

**amount:int**

**referral_code:Optional[str]**

**classnado_protocol.contracts.NadoExecuteType(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumEnumeration of possible actions to execute in Nado.PLACE_ORDER='place_order'PLACE_ORDERS='place_orders'CANCEL_ORDERS='cancel_orders'CANCEL_PRODUCT_ORDERS='cancel_product_orders'CANCEL_AND_PLACE='cancel_and_place'WITHDRAW_COLLATERAL='withdraw_collateral'LIQUIDATE_SUBACCOUNT='liquidate_subaccount'MINT_NLP='mint_nlp'BURN_NLP='burn_nlp'LINK_SIGNER='link_signer'TRANSFER_QUOTE='transfer_quote'

Bases:StrEnum

Enumeration of possible actions to execute in Nado.

**PLACE_ORDER='place_order'**

**PLACE_ORDERS='place_orders'**

**CANCEL_ORDERS='cancel_orders'**

**CANCEL_PRODUCT_ORDERS='cancel_product_orders'**

**CANCEL_AND_PLACE='cancel_and_place'**

**WITHDRAW_COLLATERAL='withdraw_collateral'**

**LIQUIDATE_SUBACCOUNT='liquidate_subaccount'**

**MINT_NLP='mint_nlp'**

**BURN_NLP='burn_nlp'**

**LINK_SIGNER='link_signer'**

**TRANSFER_QUOTE='transfer_quote'**

**classnado_protocol.contracts.NadoNetwork(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumEnumeration representing various network environments for the Nado protocol.HARDHAT='localhost'TESTING='testing'TESTNET='testnet'MAINNET='mainnet'

Bases:StrEnum

Enumeration representing various network environments for the Nado protocol.

**HARDHAT='localhost'**

**TESTING='testing'**

**TESTNET='testnet'**

**MAINNET='mainnet'**

**classnado_protocol.contracts.NadoAbiName(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumEnumeration representing various contract names for which the ABI can be loaded in the Nado protocol.ENDPOINT='Endpoint'FQUERIER='FQuerier'ICLEARINGHOUSE='IClearinghouse'IENDPOINT='IEndpoint'IPERP_ENGINE='IPerpEngine'ISPOT_ENGINE='ISpotEngine'MOCK_ERC20='MockERC20'ISTAKING='IStaking'IAIRDROP='IAirdrop'IFOUNDATION_REWARDS_AIRDROP='IFoundationRewardsAirdrop'

Bases:StrEnum

Enumeration representing various contract names for which the ABI can be loaded in the Nado protocol.

**ENDPOINT='Endpoint'**

**FQUERIER='FQuerier'**

**ICLEARINGHOUSE='IClearinghouse'**

**IENDPOINT='IEndpoint'**

**IPERP_ENGINE='IPerpEngine'**

**ISPOT_ENGINE='ISpotEngine'**

**MOCK_ERC20='MockERC20'**

**ISTAKING='IStaking'**

**IAIRDROP='IAirdrop'**

**IFOUNDATION_REWARDS_AIRDROP='IFoundationRewardsAirdrop'**

**classnado_protocol.contracts.NadoDeployment(**data)[source]**
  Bases:NadoBaseModelClass representing deployment data for Nado protocol contracts.Attributes:node_url (AnyUrl): The URL of the node.quote_addr (str): The address of the quote contract.querier_addr (str): The address of the querier contract.clearinghouse_addr (str): The address of the clearinghouse contract.endpoint_addr (str): The address of the endpoint contract.spot_engine_addr (str): The address of the spot engine contract.perp_engine_addr (str): The address of the perpetual engine contract.airdrop_addr (str): The address of the airdrop contract.staking_addr (str): The address of the staking contract.foundation_rewards_airdrop_addr (str): The address of Foundation Rewards airdrop contract for the corresponding chain (e.g: Arb airdrop for Arbitrum).node_url:AnyUrlquote_addr:strquerier_addr:strclearinghouse_addr:strendpoint_addr:strspot_engine_addr:strperp_engine_addr:strairdrop_addr:strstaking_addr:strfoundation_rewards_airdrop_addr:str

Bases:NadoBaseModel

Class representing deployment data for Nado protocol contracts.

**Attributes:**
  node_url (AnyUrl): The URL of the node.quote_addr (str): The address of the quote contract.querier_addr (str): The address of the querier contract.clearinghouse_addr (str): The address of the clearinghouse contract.endpoint_addr (str): The address of the endpoint contract.spot_engine_addr (str): The address of the spot engine contract.perp_engine_addr (str): The address of the perpetual engine contract.airdrop_addr (str): The address of the airdrop contract.staking_addr (str): The address of the staking contract.foundation_rewards_airdrop_addr (str): The address of Foundation Rewards airdrop contract for the corresponding chain (e.g: Arb airdrop for Arbitrum).

node_url (AnyUrl): The URL of the node.

quote_addr (str): The address of the quote contract.

querier_addr (str): The address of the querier contract.

clearinghouse_addr (str): The address of the clearinghouse contract.

endpoint_addr (str): The address of the endpoint contract.

spot_engine_addr (str): The address of the spot engine contract.

perp_engine_addr (str): The address of the perpetual engine contract.

airdrop_addr (str): The address of the airdrop contract.

staking_addr (str): The address of the staking contract.

foundation_rewards_airdrop_addr (str): The address of Foundation Rewards airdrop contract for the corresponding chain (e.g: Arb airdrop for Arbitrum).

**node_url:AnyUrl**

**quote_addr:str**

**querier_addr:str**

**clearinghouse_addr:str**

**endpoint_addr:str**

**spot_engine_addr:str**

**perp_engine_addr:str**

**airdrop_addr:str**

**staking_addr:str**

**foundation_rewards_airdrop_addr:str**

## nado-protocol.contracts.eip712

**nado_protocol.contracts.eip712.get_nado_eip712_domain(verifying_contract,chain_id)[source]**
  Util to create an EIP712Domain instance specific to Nado.Return type:EIP712DomainArgs:verifying_contract (str): The address of the contract that will verify the EIP-712 signature.chain_id (int): The chain ID of the originating network.Returns:EIP712Domain: An instance of EIP712Domain with name set to “Nado”, version “0.0.1”, and the provided verifying contract and chain ID.

Util to create an EIP712Domain instance specific to Nado.

**Return type:**
  EIP712Domain

EIP712Domain

**Args:**
  verifying_contract (str): The address of the contract that will verify the EIP-712 signature.chain_id (int): The chain ID of the originating network.

verifying_contract (str): The address of the contract that will verify the EIP-712 signature.

chain_id (int): The chain ID of the originating network.

**Returns:**
  EIP712Domain: An instance of EIP712Domain with name set to “Nado”, version “0.0.1”, and the provided verifying contract and chain ID.

EIP712Domain: An instance of EIP712Domain with name set to “Nado”, version “0.0.1”, and the provided verifying contract and chain ID.

**nado_protocol.contracts.eip712.get_eip712_domain_type()[source]**
  Util to return the structure of an EIP712Domain as per EIP-712.Return type:list[dict[str,str]]Returns:dict: A list of dictionaries each containing the name and type of a field in EIP712Domain.

Util to return the structure of an EIP712Domain as per EIP-712.

**Return type:**
  list[dict[str,str]]

list[dict[str,str]]

**Returns:**
  dict: A list of dictionaries each containing the name and type of a field in EIP712Domain.

dict: A list of dictionaries each containing the name and type of a field in EIP712Domain.

**nado_protocol.contracts.eip712.build_eip712_typed_data(tx,msg,verifying_contract,chain_id)[source]**
  Util to build EIP712 typed data for Nado execution.Return type:EIP712TypedDataArgs:tx (NadoTxType): The Nado tx type being signed.msg (dict): The message being signed.verifying_contract (str): The contract that will verify the signature.chain_id (int): The chain ID of the originating network.Returns:EIP712TypedData: A structured data object that adheres to the EIP-712 standard.

Util to build EIP712 typed data for Nado execution.

**Return type:**
  EIP712TypedData

EIP712TypedData

**Args:**
  tx (NadoTxType): The Nado tx type being signed.msg (dict): The message being signed.verifying_contract (str): The contract that will verify the signature.chain_id (int): The chain ID of the originating network.

tx (NadoTxType): The Nado tx type being signed.

msg (dict): The message being signed.

verifying_contract (str): The contract that will verify the signature.

chain_id (int): The chain ID of the originating network.

**Returns:**
  EIP712TypedData: A structured data object that adheres to the EIP-712 standard.

EIP712TypedData: A structured data object that adheres to the EIP-712 standard.

**nado_protocol.contracts.eip712.get_eip712_typed_data_digest(typed_data)[source]**
  Util to get the EIP-712 typed data hash.Return type:strArgs:typed_data (EIP712TypedData): The EIP-712 typed data to hash.Returns:str: The hexadecimal representation of the hash.

Util to get the EIP-712 typed data hash.

**Return type:**
  str

str

**Args:**
  typed_data (EIP712TypedData): The EIP-712 typed data to hash.

typed_data (EIP712TypedData): The EIP-712 typed data to hash.

**Returns:**
  str: The hexadecimal representation of the hash.

str: The hexadecimal representation of the hash.

**nado_protocol.contracts.eip712.sign_eip712_typed_data(typed_data,signer)[source]**
  Util to sign EIP-712 typed data using a local Ethereum account.Return type:strArgs:typed_data (EIP712TypedData): The EIP-712 typed data to sign.signer (LocalAccount): The local Ethereum account to sign the data.Returns:str: The hexadecimal representation of the signature.

Util to sign EIP-712 typed data using a local Ethereum account.

**Return type:**
  str

str

**Args:**
  typed_data (EIP712TypedData): The EIP-712 typed data to sign.signer (LocalAccount): The local Ethereum account to sign the data.

typed_data (EIP712TypedData): The EIP-712 typed data to sign.

signer (LocalAccount): The local Ethereum account to sign the data.

**Returns:**
  str: The hexadecimal representation of the signature.

str: The hexadecimal representation of the signature.

**nado_protocol.contracts.eip712.get_nado_eip712_type(tx)[source]**
  Util that provides the EIP712 type information for Nado execute types.Return type:dictArgs:tx (NadoTxType): The Nado transaction type for which to retrieve EIP712 type information.Returns:dict: A dictionary containing the EIP712 type information for the given execute type.

Util that provides the EIP712 type information for Nado execute types.

**Return type:**
  dict

dict

**Args:**
  tx (NadoTxType): The Nado transaction type for which to retrieve EIP712 type information.

tx (NadoTxType): The Nado transaction type for which to retrieve EIP712 type information.

**Returns:**
  dict: A dictionary containing the EIP712 type information for the given execute type.

dict: A dictionary containing the EIP712 type information for the given execute type.

**classnado_protocol.contracts.eip712.EIP712Domain(**data)[source]**
  Bases:BaseModelModel that represents the EIP-712 Domain data structure.Attributes:name (str): The user-readable name of the signing domain, i.e., the name of the DApp or the protocol.
version (str): The current major version of the signing domain. Signatures from different versions are not compatible.
chainId (int): The chain ID of the originating network.
verifyingContract (str): The address of the contract that will verify the signature.name:strversion:strchainId:intverifyingContract:str

Bases:BaseModel

Model that represents the EIP-712 Domain data structure.

**Attributes:**
  name (str): The user-readable name of the signing domain, i.e., the name of the DApp or the protocol.
version (str): The current major version of the signing domain. Signatures from different versions are not compatible.
chainId (int): The chain ID of the originating network.
verifyingContract (str): The address of the contract that will verify the signature.

name (str): The user-readable name of the signing domain, i.e., the name of the DApp or the protocol.
version (str): The current major version of the signing domain. Signatures from different versions are not compatible.
chainId (int): The chain ID of the originating network.
verifyingContract (str): The address of the contract that will verify the signature.

**name:str**

**version:str**

**chainId:int**

**verifyingContract:str**

**classnado_protocol.contracts.eip712.EIP712Types(**data)[source]**
  Bases:BaseModelUtil to encapsulate the EIP-712 type data structure.Attributes:EIP712Domain (list[dict]): A list of dictionaries representing EIP-712 Domain data.EIP712Domain:list[dict]classConfig[source]Bases:objectarbitrary_types_allowed=Trueextra='allow'

Bases:BaseModel

Util to encapsulate the EIP-712 type data structure.

**Attributes:**
  EIP712Domain (list[dict]): A list of dictionaries representing EIP-712 Domain data.

EIP712Domain (list[dict]): A list of dictionaries representing EIP-712 Domain data.

**EIP712Domain:list[dict]**

**classConfig[source]**
  Bases:objectarbitrary_types_allowed=Trueextra='allow'

Bases:object

**arbitrary_types_allowed=True**

**extra='allow'**

**classnado_protocol.contracts.eip712.EIP712TypedData(**data)[source]**
  Bases:BaseModelUtil to represent the EIP-712 Typed Data structure.Attributes:types (EIP712Types): EIP-712 type data.
primaryType (str): The primary type for EIP-712 message signing.
domain (EIP712Domain): The domain data of the EIP-712 typed message.
message (dict): The actual data to sign.types:EIP712TypesprimaryType:strdomain:EIP712Domainmessage:dict

Bases:BaseModel

Util to represent the EIP-712 Typed Data structure.

**Attributes:**
  types (EIP712Types): EIP-712 type data.
primaryType (str): The primary type for EIP-712 message signing.
domain (EIP712Domain): The domain data of the EIP-712 typed message.
message (dict): The actual data to sign.

types (EIP712Types): EIP-712 type data.
primaryType (str): The primary type for EIP-712 message signing.
domain (EIP712Domain): The domain data of the EIP-712 typed message.
message (dict): The actual data to sign.

**types:EIP712Types**

**primaryType:str**

**domain:EIP712Domain**

**message:dict**

## nado-protocol.utils

**classnado_protocol.utils.NadoBackendURL(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:StrEnumEnum representing different Nado backend URLs.DEVNET_GATEWAY='http://localhost:80'DEVNET_INDEXER='http://localhost:8000'DEVNET_TRIGGER='http://localhost:8080'TESTNET_GATEWAY='https://gateway.test.nado.xyz/v1'TESTNET_INDEXER='https://archive.test.nado.xyz/v1'TESTNET_TRIGGER='https://trigger.test.nado.xyz/v1'MAINNET_GATEWAY='https://gateway.prod.nado.xyz/v1'MAINNET_INDEXER='https://archive.prod.nado.xyz/v1'MAINNET_TRIGGER='https://trigger.prod.nado.xyz/v1'

Bases:StrEnum

Enum representing different Nado backend URLs.

**DEVNET_GATEWAY='http://localhost:80'**

**DEVNET_INDEXER='http://localhost:8000'**

**DEVNET_TRIGGER='http://localhost:8080'**

**TESTNET_GATEWAY='https://gateway.test.nado.xyz/v1'**

**TESTNET_INDEXER='https://archive.test.nado.xyz/v1'**

**TESTNET_TRIGGER='https://trigger.test.nado.xyz/v1'**

**MAINNET_GATEWAY='https://gateway.prod.nado.xyz/v1'**

**MAINNET_INDEXER='https://archive.prod.nado.xyz/v1'**

**MAINNET_TRIGGER='https://trigger.prod.nado.xyz/v1'**

**classnado_protocol.utils.NadoClientOpts(**data)[source]**
  Bases:BaseModelModel defining the configuration options for execute Nado Clients (e.g: Engine, Trigger). It includes various parameters such as the URL,
the signer, the linked signer, the chain ID, and others.Attributes:url (AnyUrl): The URL of the server.
signer (Optional[Signer]): The signer for the client, if any. It can either be aLocalAccountor a private key.
linked_signer (Optional[Signer]): An optional signer linked the main subaccount to perform executes on it’s behalf.
chain_id (Optional[int]): An optional network chain ID.
endpoint_addr (Optional[str]): Nado’s endpoint address used for verifying executes.Notes:The class also includes several methods for validating and sanitizing the input values.“linked_signer” cannot be set if “signer” is not set.url:AnyUrlsigner:Union[LocalAccount,str,None]linked_signer:Union[LocalAccount,str,None]chain_id:Optional[int]endpoint_addr:Optional[str]classConfig[source]Bases:objectarbitrary_types_allowed=Trueclassmethodcheck_linked_signer(values)[source]Validates that if a linked_signer is set, a signer must also be set.Args:values (dict): The input values to be validated.Raises:ValueError: If linked_signer is set but signer is not.Returns:dict: The validated values.classmethodclean_url(v)[source]Cleans the URL input by removing trailing slashes.Return type:strArgs:v (AnyUrl): The input URL.Returns:str: The cleaned URL.classmethodsigner_to_local_account(v)[source]Validates and converts the signer to a LocalAccount instance.Return type:Optional[LocalAccount]Args:v (Optional[Signer]): The signer instance or None.Returns:Optional[LocalAccount]: The LocalAccount instance or None.classmethodlinked_signer_to_local_account(v)[source]Validates and converts the linked_signer to a LocalAccount instance.Return type:Optional[LocalAccount]Args:v (Optional[Signer]): The linked_signer instance or None.Returns:Optional[LocalAccount]: The LocalAccount instance or None.

Bases:BaseModel

Model defining the configuration options for execute Nado Clients (e.g: Engine, Trigger). It includes various parameters such as the URL,
the signer, the linked signer, the chain ID, and others.

**Attributes:**
  url (AnyUrl): The URL of the server.
signer (Optional[Signer]): The signer for the client, if any. It can either be aLocalAccountor a private key.
linked_signer (Optional[Signer]): An optional signer linked the main subaccount to perform executes on it’s behalf.
chain_id (Optional[int]): An optional network chain ID.
endpoint_addr (Optional[str]): Nado’s endpoint address used for verifying executes.

url (AnyUrl): The URL of the server.
signer (Optional[Signer]): The signer for the client, if any. It can either be aLocalAccountor a private key.
linked_signer (Optional[Signer]): An optional signer linked the main subaccount to perform executes on it’s behalf.
chain_id (Optional[int]): An optional network chain ID.
endpoint_addr (Optional[str]): Nado’s endpoint address used for verifying executes.

**Notes:**
  The class also includes several methods for validating and sanitizing the input values.“linked_signer” cannot be set if “signer” is not set.
- The class also includes several methods for validating and sanitizing the input values.

The class also includes several methods for validating and sanitizing the input values.

- “linked_signer” cannot be set if “signer” is not set.

“linked_signer” cannot be set if “signer” is not set.

**url:AnyUrl**

**signer:Union[LocalAccount,str,None]**

**linked_signer:Union[LocalAccount,str,None]**

**chain_id:Optional[int]**

**endpoint_addr:Optional[str]**

**classConfig[source]**
  Bases:objectarbitrary_types_allowed=True

Bases:object

**arbitrary_types_allowed=True**

**classmethodcheck_linked_signer(values)[source]**
  Validates that if a linked_signer is set, a signer must also be set.Args:values (dict): The input values to be validated.Raises:ValueError: If linked_signer is set but signer is not.Returns:dict: The validated values.

Validates that if a linked_signer is set, a signer must also be set.

**Args:**
  values (dict): The input values to be validated.

values (dict): The input values to be validated.

**Raises:**
  ValueError: If linked_signer is set but signer is not.

ValueError: If linked_signer is set but signer is not.

**Returns:**
  dict: The validated values.

dict: The validated values.

**classmethodclean_url(v)[source]**
  Cleans the URL input by removing trailing slashes.Return type:strArgs:v (AnyUrl): The input URL.Returns:str: The cleaned URL.

Cleans the URL input by removing trailing slashes.

**Return type:**
  str

str

**Args:**
  v (AnyUrl): The input URL.

v (AnyUrl): The input URL.

**Returns:**
  str: The cleaned URL.

str: The cleaned URL.

**classmethodsigner_to_local_account(v)[source]**
  Validates and converts the signer to a LocalAccount instance.Return type:Optional[LocalAccount]Args:v (Optional[Signer]): The signer instance or None.Returns:Optional[LocalAccount]: The LocalAccount instance or None.

Validates and converts the signer to a LocalAccount instance.

**Return type:**
  Optional[LocalAccount]

Optional[LocalAccount]

**Args:**
  v (Optional[Signer]): The signer instance or None.

v (Optional[Signer]): The signer instance or None.

**Returns:**
  Optional[LocalAccount]: The LocalAccount instance or None.

Optional[LocalAccount]: The LocalAccount instance or None.

**classmethodlinked_signer_to_local_account(v)[source]**
  Validates and converts the linked_signer to a LocalAccount instance.Return type:Optional[LocalAccount]Args:v (Optional[Signer]): The linked_signer instance or None.Returns:Optional[LocalAccount]: The LocalAccount instance or None.

Validates and converts the linked_signer to a LocalAccount instance.

**Return type:**
  Optional[LocalAccount]

Optional[LocalAccount]

**Args:**
  v (Optional[Signer]): The linked_signer instance or None.

v (Optional[Signer]): The linked_signer instance or None.

**Returns:**
  Optional[LocalAccount]: The LocalAccount instance or None.

Optional[LocalAccount]: The LocalAccount instance or None.

**classnado_protocol.utils.SubaccountParams(**data)[source]**
  Bases:NadoBaseModelA class used to represent parameters for a Subaccount in the Nado system.Attributes:subaccount_owner (Optional[str]): The wallet address of the subaccount.
subaccount_name (str): The subaccount name identifier.subaccount_owner:Optional[str]subaccount_name:str

Bases:NadoBaseModel

A class used to represent parameters for a Subaccount in the Nado system.

**Attributes:**
  subaccount_owner (Optional[str]): The wallet address of the subaccount.
subaccount_name (str): The subaccount name identifier.

subaccount_owner (Optional[str]): The wallet address of the subaccount.
subaccount_name (str): The subaccount name identifier.

**subaccount_owner:Optional[str]**

**subaccount_name:str**

**nado_protocol.utils.subaccount_to_bytes32(subaccount,name=None)[source]**
  Converts a subaccount representation to a bytes object of length 32.Return type:bytesArgs:subaccount (Subaccount): The subaccount, which can be a string, bytes, or SubaccountParams instance.name (str|bytes, optional): The subaccount name, when providedsubaccountis expected to be the owner address.Returns:(bytes|SubaccountParams): The bytes object of length 32 representing the subaccount.Raises:ValueError: If thesubaccountis aSubaccountParamsinstance and is missing eithersubaccount_ownerorsubaccount_nameNote:Ifnameis provided,subaccountmust be the owner address, otherwisesubaccountcan be the bytes32 or hex representation of the subaccount or a SubaccountParams object.

Converts a subaccount representation to a bytes object of length 32.

**Return type:**
  bytes

bytes

**Args:**
  subaccount (Subaccount): The subaccount, which can be a string, bytes, or SubaccountParams instance.name (str|bytes, optional): The subaccount name, when providedsubaccountis expected to be the owner address.

subaccount (Subaccount): The subaccount, which can be a string, bytes, or SubaccountParams instance.

name (str|bytes, optional): The subaccount name, when providedsubaccountis expected to be the owner address.

**Returns:**
  (bytes|SubaccountParams): The bytes object of length 32 representing the subaccount.

(bytes|SubaccountParams): The bytes object of length 32 representing the subaccount.

**Raises:**
  ValueError: If thesubaccountis aSubaccountParamsinstance and is missing eithersubaccount_ownerorsubaccount_name

ValueError: If thesubaccountis aSubaccountParamsinstance and is missing eithersubaccount_ownerorsubaccount_name

**Note:**
  Ifnameis provided,subaccountmust be the owner address, otherwisesubaccountcan be the bytes32 or hex representation of the subaccount or a SubaccountParams object.

Ifnameis provided,subaccountmust be the owner address, otherwisesubaccountcan be the bytes32 or hex representation of the subaccount or a SubaccountParams object.

**nado_protocol.utils.subaccount_to_hex(subaccount,name=None)[source]**
  Converts a subaccount representation to its hexadecimal representation.Return type:strArgs:subaccount (Subaccount): The subaccount, which can be a string, bytes, or SubaccountParams instance.name (str|bytes, optional): Additional string, if any, to be appended to the subaccount string before conversion. Defaults to None.Returns:(str|SubaccountParams): The hexadecimal representation of the subaccount.

Converts a subaccount representation to its hexadecimal representation.

**Return type:**
  str

str

**Args:**
  subaccount (Subaccount): The subaccount, which can be a string, bytes, or SubaccountParams instance.name (str|bytes, optional): Additional string, if any, to be appended to the subaccount string before conversion. Defaults to None.

subaccount (Subaccount): The subaccount, which can be a string, bytes, or SubaccountParams instance.

name (str|bytes, optional): Additional string, if any, to be appended to the subaccount string before conversion. Defaults to None.

**Returns:**
  (str|SubaccountParams): The hexadecimal representation of the subaccount.

(str|SubaccountParams): The hexadecimal representation of the subaccount.

**nado_protocol.utils.subaccount_name_to_bytes12(subaccount_name)[source]**
  Converts a subaccount name to a bytes object of length 12.Return type:bytesArgs:subaccount_name (str): The subaccount name to be converted.Returns:bytes: A bytes object of length 12 representing the subaccount name.

Converts a subaccount name to a bytes object of length 12.

**Return type:**
  bytes

bytes

**Args:**
  subaccount_name (str): The subaccount name to be converted.

subaccount_name (str): The subaccount name to be converted.

**Returns:**
  bytes: A bytes object of length 12 representing the subaccount name.

bytes: A bytes object of length 12 representing the subaccount name.

**nado_protocol.utils.hex_to_bytes32(input)[source]**
  Converts a hexadecimal string or bytes to a bytes object of length 32.Return type:bytesArgs:input (str | bytes): The hexadecimal string or bytes to be converted.Returns:bytes: The converted bytes object of length 32.

Converts a hexadecimal string or bytes to a bytes object of length 32.

**Return type:**
  bytes

bytes

**Args:**
  input (str | bytes): The hexadecimal string or bytes to be converted.

input (str | bytes): The hexadecimal string or bytes to be converted.

**Returns:**
  bytes: The converted bytes object of length 32.

bytes: The converted bytes object of length 32.

**nado_protocol.utils.hex_to_bytes12(input)[source]**
  Converts a hexadecimal string or bytes to a bytes object of length 12.Return type:bytesArgs:input (str | bytes): The hexadecimal string or bytes to be converted.Returns:bytes: The converted bytes object of length 12.

Converts a hexadecimal string or bytes to a bytes object of length 12.

**Return type:**
  bytes

bytes

**Args:**
  input (str | bytes): The hexadecimal string or bytes to be converted.

input (str | bytes): The hexadecimal string or bytes to be converted.

**Returns:**
  bytes: The converted bytes object of length 12.

bytes: The converted bytes object of length 12.

**nado_protocol.utils.hex_to_bytes(input,size)[source]**
  Converts a hexadecimal string or bytes to a bytes object of specified size.Return type:bytesArgs:input (str | bytes): The hexadecimal string or bytes to be converted.size (int): The specified size for the output bytes object.Returns:bytes: The converted bytes object of the specified size.

Converts a hexadecimal string or bytes to a bytes object of specified size.

**Return type:**
  bytes

bytes

**Args:**
  input (str | bytes): The hexadecimal string or bytes to be converted.size (int): The specified size for the output bytes object.

input (str | bytes): The hexadecimal string or bytes to be converted.

size (int): The specified size for the output bytes object.

**Returns:**
  bytes: The converted bytes object of the specified size.

bytes: The converted bytes object of the specified size.

**nado_protocol.utils.str_to_hex(input)[source]**
  Converts a string to its hexadecimal representation.Return type:strArgs:input (str): The string to be converted.Returns:str: The hexadecimal representation of the input string.

Converts a string to its hexadecimal representation.

**Return type:**
  str

str

**Args:**
  input (str): The string to be converted.

input (str): The string to be converted.

**Returns:**
  str: The hexadecimal representation of the input string.

str: The hexadecimal representation of the input string.

**nado_protocol.utils.bytes32_to_hex(bytes32)[source]**
  Converts a bytes object of length 32 to its hexadecimal representation.Return type:strArgs:bytes32 (bytes): The bytes object of length 32 to be converted.Returns:str: The hexadecimal representation of the input bytes object. If the input is not a bytes object, the function returns the input itself.

Converts a bytes object of length 32 to its hexadecimal representation.

**Return type:**
  str

str

**Args:**
  bytes32 (bytes): The bytes object of length 32 to be converted.

bytes32 (bytes): The bytes object of length 32 to be converted.

**Returns:**
  str: The hexadecimal representation of the input bytes object. If the input is not a bytes object, the function returns the input itself.

str: The hexadecimal representation of the input bytes object. If the input is not a bytes object, the function returns the input itself.

**nado_protocol.utils.zero_subaccount()[source]**
  Generates a bytes object of length 32 filled with zero bytes.Return type:bytesReturns:bytes: A bytes object of length 32 filled with zero bytes.

Generates a bytes object of length 32 filled with zero bytes.

**Return type:**
  bytes

bytes

**Returns:**
  bytes: A bytes object of length 32 filled with zero bytes.

bytes: A bytes object of length 32 filled with zero bytes.

**nado_protocol.utils.zero_address()[source]**
  Generates a bytes object of length 20 filled with zero bytes.Return type:bytesReturns:bytes: A bytes object of length 20 filled with zero bytes.

Generates a bytes object of length 20 filled with zero bytes.

**Return type:**
  bytes

bytes

**Returns:**
  bytes: A bytes object of length 20 filled with zero bytes.

bytes: A bytes object of length 20 filled with zero bytes.

**classnado_protocol.utils.OrderType(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:IntEnumDEFAULT=0IOC=1FOK=2POST_ONLY=3

Bases:IntEnum

**DEFAULT=0**

**IOC=1**

**FOK=2**

**POST_ONLY=3**

**nado_protocol.utils.get_expiration_timestamp(seconds_from_now)[source]**
  Returns a timestamp that is seconds_from_now in the future.Order types and reduce-only flags should now be set using build_appendix().Return type:intArgs:seconds_from_now (int): Number of seconds from now for expiration.Returns:int: The expiration timestamp.

Returns a timestamp that is seconds_from_now in the future.

Order types and reduce-only flags should now be set using build_appendix().

**Return type:**
  int

int

**Args:**
  seconds_from_now (int): Number of seconds from now for expiration.

seconds_from_now (int): Number of seconds from now for expiration.

**Returns:**
  int: The expiration timestamp.

int: The expiration timestamp.

**nado_protocol.utils.gen_order_nonce(recv_time_ms=None,random_int=None)[source]**
  Generates an order nonce based on a received timestamp and a random integer.Return type:intArgs:recv_time_ms (int, optional): Received timestamp in milliseconds. Defaults to the current time plus 90 seconds.random_int (int, optional): An integer for the nonce. Defaults to a random integer between 0 and 999.Returns:int: The generated order nonce.

Generates an order nonce based on a received timestamp and a random integer.

**Return type:**
  int

int

**Args:**
  recv_time_ms (int, optional): Received timestamp in milliseconds. Defaults to the current time plus 90 seconds.random_int (int, optional): An integer for the nonce. Defaults to a random integer between 0 and 999.

recv_time_ms (int, optional): Received timestamp in milliseconds. Defaults to the current time plus 90 seconds.

random_int (int, optional): An integer for the nonce. Defaults to a random integer between 0 and 999.

**Returns:**
  int: The generated order nonce.

int: The generated order nonce.

**nado_protocol.utils.to_pow_10(x,pow)[source]**
  Converts integer to power of 10 format.Return type:intArgs:x (int): Integer value.pow (int): Power of 10.Returns:int: Converted value.

Converts integer to power of 10 format.

**Return type:**
  int

int

**Args:**
  x (int): Integer value.pow (int): Power of 10.

x (int): Integer value.

pow (int): Power of 10.

**Returns:**
  int: Converted value.

int: Converted value.

**nado_protocol.utils.to_x6(x)[source]**
  Converts a float to a fixed point of 1e6.Return type:intArgs:x (float): Float value to convert.Returns:int: Fixed point value represented as an integer.

Converts a float to a fixed point of 1e6.

**Return type:**
  int

int

**Args:**
  x (float): Float value to convert.

x (float): Float value to convert.

**Returns:**
  int: Fixed point value represented as an integer.

int: Fixed point value represented as an integer.

**nado_protocol.utils.to_x18(x)[source]**
  Converts a float to a fixed point of 1e18.Return type:intArgs:x (float): Float value to convert.Returns:int: Fixed point value represented as an integer.

Converts a float to a fixed point of 1e18.

**Return type:**
  int

int

**Args:**
  x (float): Float value to convert.

x (float): Float value to convert.

**Returns:**
  int: Fixed point value represented as an integer.

int: Fixed point value represented as an integer.

**nado_protocol.utils.from_pow_10(x,pow)[source]**
  Reverts integer from power of 10 format.Return type:floatArgs:x (int): Converted value.pow (int): Power of 10.Returns:float: Original value.

Reverts integer from power of 10 format.

**Return type:**
  float

float

**Args:**
  x (int): Converted value.pow (int): Power of 10.

x (int): Converted value.

pow (int): Power of 10.

**Returns:**
  float: Original value.

float: Original value.

**nado_protocol.utils.from_x6(x)[source]**
  Reverts integer from power of 10^6 format.Return type:floatArgs:x (int): Converted value.Returns:float: Original value.

Reverts integer from power of 10^6 format.

**Return type:**
  float

float

**Args:**
  x (int): Converted value.

x (int): Converted value.

**Returns:**
  float: Original value.

float: Original value.

**nado_protocol.utils.from_x18(x)[source]**
  Reverts integer from power of 10^18 format.Return type:floatArgs:x (int): Converted value.Returns:float: Original value.

Reverts integer from power of 10^18 format.

**Return type:**
  float

float

**Args:**
  x (int): Converted value.

x (int): Converted value.

**Returns:**
  float: Original value.

float: Original value.

**exceptionnado_protocol.utils.ExecuteFailedException(message='Executefailed')[source]**
  Bases:ExceptionRaised when the execute status is not ‘success’__init__(message='Executefailed')[source]

Bases:Exception

Raised when the execute status is not ‘success’

**__init__(message='Executefailed')[source]**

**exceptionnado_protocol.utils.QueryFailedException(message='Queryfailed')[source]**
  Bases:ExceptionRaised when the query status is not ‘success’__init__(message='Queryfailed')[source]

Bases:Exception

Raised when the query status is not ‘success’

**__init__(message='Queryfailed')[source]**

**exceptionnado_protocol.utils.BadStatusCodeException(message='Badstatuscode')[source]**
  Bases:ExceptionRaised when the response status code is not 200__init__(message='Badstatuscode')[source]

Bases:Exception

Raised when the response status code is not 200

**__init__(message='Badstatuscode')[source]**

**exceptionnado_protocol.utils.MissingSignerException(message='Signernotprovided')[source]**
  Bases:ExceptionRaised when the Signer is required to perform an operation but it’s not provided.__init__(message='Signernotprovided')[source]

Bases:Exception

Raised when the Signer is required to perform an operation but it’s not provided.

**__init__(message='Signernotprovided')[source]**

**exceptionnado_protocol.utils.InvalidProductId(message='Invalidproductidprovided')[source]**
  Bases:ExceptionRaised when product id is invalid.__init__(message='Invalidproductidprovided')[source]

Bases:Exception

Raised when product id is invalid.

**__init__(message='Invalidproductidprovided')[source]**

**classnado_protocol.utils.OrderAppendixTriggerType(value,names=None,*,module=None,qualname=None,type=None,start=1,boundary=None)[source]**
  Bases:IntEnumEnumeration for trigger order types encoded in the appendix.PRICE=1TWAP=2TWAP_CUSTOM_AMOUNTS=3

Bases:IntEnum

Enumeration for trigger order types encoded in the appendix.

**PRICE=1**

**TWAP=2**

**TWAP_CUSTOM_AMOUNTS=3**

**classnado_protocol.utils.AppendixBitFields[source]**
  Bases:objectVERSION_BITS=8ISOLATED_BITS=1ORDER_TYPE_BITS=2REDUCE_ONLY_BITS=1TRIGGER_TYPE_BITS=2RESERVED_BITS=50VALUE_BITS=64VERSION_MASK=255ISOLATED_MASK=1ORDER_TYPE_MASK=3REDUCE_ONLY_MASK=1TRIGGER_TYPE_MASK=3RESERVED_MASK=1125899906842623VALUE_MASK=18446744073709551615VERSION_SHIFT=0ISOLATED_SHIFT=8ORDER_TYPE_SHIFT=9REDUCE_ONLY_SHIFT=11TRIGGER_TYPE_SHIFT=12RESERVED_SHIFT=14VALUE_SHIFT=64

Bases:object

**VERSION_BITS=8**

**ISOLATED_BITS=1**

**ORDER_TYPE_BITS=2**

**REDUCE_ONLY_BITS=1**

**TRIGGER_TYPE_BITS=2**

**RESERVED_BITS=50**

**VALUE_BITS=64**

**VERSION_MASK=255**

**ISOLATED_MASK=1**

**ORDER_TYPE_MASK=3**

**REDUCE_ONLY_MASK=1**

**TRIGGER_TYPE_MASK=3**

**RESERVED_MASK=1125899906842623**

**VALUE_MASK=18446744073709551615**

**VERSION_SHIFT=0**

**ISOLATED_SHIFT=8**

**ORDER_TYPE_SHIFT=9**

**REDUCE_ONLY_SHIFT=11**

**TRIGGER_TYPE_SHIFT=12**

**RESERVED_SHIFT=14**

**VALUE_SHIFT=64**

**classnado_protocol.utils.TWAPBitFields[source]**
  Bases:objectBit field definitions for TWAP value packing within the 64-bit value field.TIMES_BITS=32SLIPPAGE_BITS=32TIMES_MASK=4294967295SLIPPAGE_MASK=4294967295SLIPPAGE_SHIFT=0TIMES_SHIFT=32SLIPPAGE_SCALE=1000000

Bases:object

Bit field definitions for TWAP value packing within the 64-bit value field.

**TIMES_BITS=32**

**SLIPPAGE_BITS=32**

**TIMES_MASK=4294967295**

**SLIPPAGE_MASK=4294967295**

**SLIPPAGE_SHIFT=0**

**TIMES_SHIFT=32**

**SLIPPAGE_SCALE=1000000**

**nado_protocol.utils.gen_order_verifying_contract(product_id)[source]**
  Generates the order verifying contract address based on the product ID.Return type:strArgs:product_id (int): The product ID for which to generate the verifying contract address.Returns:str: The generated order verifying contract address in hexadecimal format.

Generates the order verifying contract address based on the product ID.

**Return type:**
  str

str

**Args:**
  product_id (int): The product ID for which to generate the verifying contract address.

product_id (int): The product ID for which to generate the verifying contract address.

**Returns:**
  str: The generated order verifying contract address in hexadecimal format.

str: The generated order verifying contract address in hexadecimal format.

**nado_protocol.utils.pack_twap_appendix_value(times,slippage_frac)[source]**
  Packs TWAP order fields into a 64-bit integer for the appendix.Bit layout (MSB → LSB):
|   times   | slippage_x6 ||-----------|————-|
| 63..32    | 31..0       |
| 32 bits   | 32 bits     |Return type:int

Packs TWAP order fields into a 64-bit integer for the appendix.

Bit layout (MSB → LSB):
|   times   | slippage_x6 ||-----------|————-|
| 63..32    | 31..0       |
| 32 bits   | 32 bits     |

**Return type:**
  int

int

**nado_protocol.utils.unpack_twap_appendix_value(value)[source]**
  Unpacks a 64-bit integer into TWAP order fields.Return type:tuple[int,float]Args:value (int): The 64-bit value to unpack.Returns:tuple[int, float]: Number of TWAP executions and slippage fraction.

Unpacks a 64-bit integer into TWAP order fields.

**Return type:**
  tuple[int,float]

tuple[int,float]

**Args:**
  value (int): The 64-bit value to unpack.

value (int): The 64-bit value to unpack.

**Returns:**
  tuple[int, float]: Number of TWAP executions and slippage fraction.

tuple[int, float]: Number of TWAP executions and slippage fraction.

**nado_protocol.utils.build_appendix(order_type,isolated=False,reduce_only=False,trigger_type=None,isolated_margin=None,twap_times=None,twap_slippage_frac=None,_version=1)[source]**
  Builds an appendix value with the specified parameters.Return type:intArgs:order_type (OrderType): The order execution type. Required.
isolated (bool): Whether this order is for an isolated position. Defaults to False.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
trigger_type (Optional[OrderAppendixTriggerType]): Trigger type. Defaults to None (no trigger).
isolated_margin (Optional[int]): Margin amount for isolated position if isolated is True.
twap_times (Optional[int]): Number of TWAP executions (required for TWAP trigger type).
twap_slippage_frac (Optional[float]): TWAP slippage fraction (required for TWAP trigger type).Returns:int: The built appendix value with version set to APPENDIX_VERSION.Raises:ValueError: If parameters are invalid or incompatible.

Builds an appendix value with the specified parameters.

**Return type:**
  int

int

**Args:**
  order_type (OrderType): The order execution type. Required.
isolated (bool): Whether this order is for an isolated position. Defaults to False.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
trigger_type (Optional[OrderAppendixTriggerType]): Trigger type. Defaults to None (no trigger).
isolated_margin (Optional[int]): Margin amount for isolated position if isolated is True.
twap_times (Optional[int]): Number of TWAP executions (required for TWAP trigger type).
twap_slippage_frac (Optional[float]): TWAP slippage fraction (required for TWAP trigger type).

order_type (OrderType): The order execution type. Required.
isolated (bool): Whether this order is for an isolated position. Defaults to False.
reduce_only (bool): Whether this is a reduce-only order. Defaults to False.
trigger_type (Optional[OrderAppendixTriggerType]): Trigger type. Defaults to None (no trigger).
isolated_margin (Optional[int]): Margin amount for isolated position if isolated is True.
twap_times (Optional[int]): Number of TWAP executions (required for TWAP trigger type).
twap_slippage_frac (Optional[float]): TWAP slippage fraction (required for TWAP trigger type).

**Returns:**
  int: The built appendix value with version set to APPENDIX_VERSION.

int: The built appendix value with version set to APPENDIX_VERSION.

**Raises:**
  ValueError: If parameters are invalid or incompatible.

ValueError: If parameters are invalid or incompatible.

**nado_protocol.utils.order_reduce_only(appendix)[source]**
  Checks if the order is reduce-only based on the appendix value.Return type:boolArgs:appendix (int): The order appendix value.Returns:bool: True if the order is reduce-only, False otherwise.

Checks if the order is reduce-only based on the appendix value.

**Return type:**
  bool

bool

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  bool: True if the order is reduce-only, False otherwise.

bool: True if the order is reduce-only, False otherwise.

**nado_protocol.utils.order_is_trigger_order(appendix)[source]**
  Checks if the order is a trigger order based on the appendix value.Return type:boolArgs:appendix (int): The order appendix value.Returns:bool: True if the order is a trigger order, False otherwise.

Checks if the order is a trigger order based on the appendix value.

**Return type:**
  bool

bool

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  bool: True if the order is a trigger order, False otherwise.

bool: True if the order is a trigger order, False otherwise.

**nado_protocol.utils.order_is_isolated(appendix)[source]**
  Checks if the order is for an isolated position based on the appendix value.Return type:boolArgs:appendix (int): The order appendix value.Returns:bool: True if the order is for an isolated position, False otherwise.

Checks if the order is for an isolated position based on the appendix value.

**Return type:**
  bool

bool

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  bool: True if the order is for an isolated position, False otherwise.

bool: True if the order is for an isolated position, False otherwise.

**nado_protocol.utils.order_isolated_margin(appendix)[source]**
  Extracts the isolated margin amount from the appendix value.Return type:Optional[int]Args:appendix (int): The order appendix value.Returns:Optional[int]: The isolated margin amount if the order is isolated, None otherwise.

Extracts the isolated margin amount from the appendix value.

**Return type:**
  Optional[int]

Optional[int]

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  Optional[int]: The isolated margin amount if the order is isolated, None otherwise.

Optional[int]: The isolated margin amount if the order is isolated, None otherwise.

**nado_protocol.utils.order_version(appendix)[source]**
  Extracts the version from the appendix value.Return type:intArgs:appendix (int): The order appendix value.Returns:int: The version number (bits 7..0).

Extracts the version from the appendix value.

**Return type:**
  int

int

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  int: The version number (bits 7..0).

int: The version number (bits 7..0).

**nado_protocol.utils.order_trigger_type(appendix)[source]**
  Extracts the trigger type from the appendix value.Return type:Optional[OrderAppendixTriggerType]Args:appendix (int): The order appendix value.Returns:Optional[OrderAppendixTriggerType]: The trigger type, or None if no trigger is set.

Extracts the trigger type from the appendix value.

**Return type:**
  Optional[OrderAppendixTriggerType]

Optional[OrderAppendixTriggerType]

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  Optional[OrderAppendixTriggerType]: The trigger type, or None if no trigger is set.

Optional[OrderAppendixTriggerType]: The trigger type, or None if no trigger is set.

**nado_protocol.utils.order_twap_data(appendix)[source]**
  Extracts TWAP data from the appendix value if it’s a TWAP order.Return type:Optional[tuple[int,float]]Args:appendix (int): The order appendix value.Returns:Optional[tuple[int, float]]: Tuple of (times, slippage_frac) if TWAP, None otherwise.

Extracts TWAP data from the appendix value if it’s a TWAP order.

**Return type:**
  Optional[tuple[int,float]]

Optional[tuple[int,float]]

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  Optional[tuple[int, float]]: Tuple of (times, slippage_frac) if TWAP, None otherwise.

Optional[tuple[int, float]]: Tuple of (times, slippage_frac) if TWAP, None otherwise.

**nado_protocol.utils.order_execution_type(appendix)[source]**
  Extracts the order execution type from the appendix value.Return type:OrderTypeArgs:appendix (int): The order appendix value.Returns:OrderType: The order execution type.

Extracts the order execution type from the appendix value.

**Return type:**
  OrderType

OrderType

**Args:**
  appendix (int): The order appendix value.

appendix (int): The order appendix value.

**Returns:**
  OrderType: The order execution type.

OrderType: The order execution type.