---
url: https://docs.nado.xyz/faqs
title: FAQs
---

# FAQs

Discover answers to common user questions on Nado.

Welcome to the Nado Frequently Asked Questions (FAQs). This section provides detailed, practical answers for newcomers to Nado. Whether you're new to perpetual trading or refining your strategy, these responses aim to clarify key concepts and processes.

If you're depositing into Nado or withdrawing for the first time, we recommend reviewing the relevant responses and associated tutorial sections for a smooth onboarding experience.

Trade smarter, move faster.

### Deposits

#### Why can't I deposit my ETH?

Nado exclusively accepts ERC-20 tokens as deposits to ensure seamless integration with our smart contract infrastructure on the INK network.

Native ETH is not directly supported for deposits into trading positions, as it serves primarily as the gas token for transactions on INK. To use ETH-based value for trading, first bridge or wrap it into a compatible ERC-20 asset (e.g., Wrapped ETH or stablecoins like USDT0) on the Ink network. This process can be initiated through trusted bridges accessible via the Nado interface or external tools, allowing you to convert and deposit in an efficient workflow.

Users can also send ETH to Nado via the direct-deposit flow available on the app, simplifying the deposit process.

#### How do I deposit from other chains onto Ink and deposit on Nado?

Nado operates on the high-performance Ink L2 network, so deposits from other chains require first bridging assets to Ink before depositing them into Nado. This two-step process ensures compatibility and leverages Ink’s low-cost, EVM-compatible environment.

- Bridge Assets to INK: Use a reliable cross-chain bridge to transfer supported assets (e.g., ETH, USDT0, USDC) from your source chain (such as Ethereum, Arbitrum, Polygon, etc) to your Ink wallet address.Recommended Bridges:USDT0 Native Bridge,Superbridge,Bungee, orRelay.Steps:Connect your wallet and select the source chain.Choose Ink as the destination network.Select the asset and amount, then sign the bridging transaction.Wait for confirmation (typically 5 - 15 minutes); track via theInk Explorer.

Bridge Assets to INK: Use a reliable cross-chain bridge to transfer supported assets (e.g., ETH, USDT0, USDC) from your source chain (such as Ethereum, Arbitrum, Polygon, etc) to your Ink wallet address.

- Recommended Bridges:USDT0 Native Bridge,Superbridge,Bungee, orRelay.

Recommended Bridges:USDT0 Native Bridge,Superbridge,Bungee, orRelay.

[USDT0 Native Bridge](https://usdt0.to/transfer)
[Superbridge](https://superbridge.app/)
[Bungee](https://bungee.exchange/)
[Relay](https://relay.link/)
- Steps:Connect your wallet and select the source chain.Choose Ink as the destination network.Select the asset and amount, then sign the bridging transaction.Wait for confirmation (typically 5 - 15 minutes); track via theInk Explorer.

Steps:

- Connect your wallet and select the source chain.

Connect your wallet and select the source chain.

- Choose Ink as the destination network.

Choose Ink as the destination network.

- Select the asset and amount, then sign the bridging transaction.

Select the asset and amount, then sign the bridging transaction.

- Wait for confirmation (typically 5 - 15 minutes); track via theInk Explorer.

Wait for confirmation (typically 5 - 15 minutes); track via theInk Explorer.

[Ink Explorer](https://explorer.inkonchain.com)

Ensure your wallet is configured for INK.

- Deposit into Nado: Once assets are on Ink and visible in your wallet:Visit theNado app.Connect your Ink-configured wallet.Navigate to the Deposit section on the Portfolio page.Select the asset, enter the amount, and confirm the on-chain transaction – deposits settle near-instantly on Nado, making collateral available for trading almost immediately.

Deposit into Nado: Once assets are on Ink and visible in your wallet:

- Visit theNado app.

Visit theNado app.

[Nado app](https://app.nado.xyz)
- Connect your Ink-configured wallet.

Connect your Ink-configured wallet.

- Navigate to the Deposit section on the Portfolio page.

Navigate to the Deposit section on the Portfolio page.

- Select the asset, enter the amount, and confirm the on-chain transaction – deposits settle near-instantly on Nado, making collateral available for trading almost immediately.

Select the asset, enter the amount, and confirm the on-chain transaction – deposits settle near-instantly on Nado, making collateral available for trading almost immediately.

This method supports assets like ETH (for gas), USDT0, USDC, wETH, and wBTC. Always verify token contract addresses on the Ink Explorer to avoid errors.

#### How do I deposit funds from a CEX wallet?

Depositing from a centralized exchange (CEX) to Nado involves withdrawing assets to your Ink-configured wallet first, then depositing into Nado This ensures funds land on the correct network for seamless trading.

1. Withdraw from CEX to Ink Wallet:

- Log in to your CEX account (e.g., Kraken) and initiate a withdrawal of supported assets (e.g., ETH, USDT0, etc).

Log in to your CEX account (e.g., Kraken) and initiate a withdrawal of supported assets (e.g., ETH, USDT0, etc).

- Enter your Ink wallet address as the recipient – double-check it's on the Ink network to prevent loss of funds. You can also use the 'Direct Deposit' feature on Nado to simplify this process.

Enter your Ink wallet address as the recipient – double-check it's on the Ink network to prevent loss of funds. You can also use the 'Direct Deposit' feature on Nado to simplify this process.

- Specify the Ink network in the withdrawal options (Kraken supports zero-fee Ink withdrawals for ETH).

Specify the Ink network in the withdrawal options (Kraken supports zero-fee Ink withdrawals for ETH).

- Confirm and complete the withdrawal; funds typically arrive in 10–30 minutes.

Confirm and complete the withdrawal; funds typically arrive in 10–30 minutes.

2. Import and Verify Assets in Wallet:

- If the token doesn't auto-appear, manually import it using the INK-specific contract address (e.g., via MetaMask's "Import Token" feature—verify addresses on the Ink Explorer).

If the token doesn't auto-appear, manually import it using the INK-specific contract address (e.g., via MetaMask's "Import Token" feature—verify addresses on the Ink Explorer).

3. Deposit into Nado:

- Connect your wallet to theNado appon the Ink network.

Connect your wallet to theNado appon the Ink network.

[Nado app](https://app.nado.xyz)
- Go to the Deposit section in the Portfolio.

Go to the Deposit section in the Portfolio.

- Select the asset, input the amount, and approve the transaction – your collateral will be available almost immediately for trading.

Select the asset, input the amount, and approve the transaction – your collateral will be available almost immediately for trading.

Pro Tip: Start with a small test withdrawal to confirm the process. For gas fees on Ink, ensure you have at least 0.01 ETH in your wallet.

### Withdrawals

Withdrawals from Nado are designed for simplicity and efficiency, operating without the need for any bridging mechanisms. This means your funds move directly from the protocol to your connected wallet in a straightforward, on-chain process, preserving the integrity and speed of your assets' transfer.

To enhance your withdrawal flexibility, you have the option to enable the borrowing toggle. This feature allows you to borrow additional assets against your existing margin, providing greater liquidity while you initiate the withdrawal.

Once your withdrawal request is submitted, it joins a batch of other pending withdrawals for optimized processing. You can easily monitor the real-time status of your withdrawal – including confirmation, pending settlement, and completion – directly in theWithdrawals Historytab, accessible via the Portfolio page in the Nado interface.

Nado employs a gas-optimization strategy to minimize user fees, batching and submitting withdrawal transactions to the Ink L2 network only when gas prices are at their lowest.

While all user actions within Nado execute instantaneously, the actual on-chain settlement of withdrawals may take up to 30 minutes during periods of elevated network congestion. This 30-minute window serves as the targeted maximum pending time: Nado's automated system will proactively submit the transaction to Nado after this interval, even in high-gas environments, to ensure timely resolution.

In rare cases where processing exceeds this timeframe, it is typically attributable to sustained spikes in network gas costs beyond Nado's control. Rest assured, if your withdrawal appears as "pending" in the Nado app, it has been successfully queued and validated internally. Settlement will occur automatically once gas fees decrease or fall below the predefined optimization threshold at the time of submission.

Please be aware that exact withdrawal times can vary due to real-time fluctuations in network conditions and gas pricing. For comprehensive tracking, we also recommend reviewing the Account History section within the Portfolio page, which provides a detailed log of all deposit and withdrawal activities.

### General FAQs

#### Why do I need to deposit?

Depositing collateral into Nado's smart contracts is essential for enabling leveraged trading on the exchange. These contracts operate in a non-custodial manner, meaning your funds remain under your control and are stored on-chain. You can withdraw your available balance whenever you choose, providing full flexibility while powering your positions.

#### Do I control my assets?

Yes, you maintain complete control over your assets in Nado. Only you can initiate trades, access funds, or execute withdrawals. The protocol's non-custodial smart contracts ensure that no third party holds custody, giving you sovereign authority over your portfolio.

#### What is unified margin trading and how is it unique?

Unified margin consolidates all your account balances and open positions into one margin pool, enabling real-time margin offsets that reduce overall margin requirements and enhance capital efficiency.

How it Works

- Shared Collateral Pool: Every asset in your Nado account (e.g., USDT0 deposits, kBTC holdings, etc) and all open positions contribute to a unified health score, calculated by Nado's on-chain risk engine. This score reflects your total available collateral and maintenance margin levels before hitting margin limits and liquidation thresholds.

Shared Collateral Pool: Every asset in your Nado account (e.g., USDT0 deposits, kBTC holdings, etc) and all open positions contribute to a unified health score, calculated by Nado's on-chain risk engine. This score reflects your total available collateral and maintenance margin levels before hitting margin limits and liquidation thresholds.

- Automatic Netting & Rebalancing: Positive PnL from one position can offset losses in another, dynamically adjusting margin needs. Maintenance margin (the buffer against liquidation) and initial margin (required to open positions) are computed holistically, often resulting in lower margin requirements than isolated margin trades.

Automatic Netting & Rebalancing: Positive PnL from one position can offset losses in another, dynamically adjusting margin needs. Maintenance margin (the buffer against liquidation) and initial margin (required to open positions) are computed holistically, often resulting in lower margin requirements than isolated margin trades.

- Risk Tiers for Visibility: Monitor your portfolio through intuitive risk levels, updated in real-time for proactive management.

Risk Tiers for Visibility: Monitor your portfolio through intuitive risk levels, updated in real-time for proactive management.

The core advantage of unified margin is maximizing capital efficiency.

Your portfolio operates as an interconnected system, where balanced exposures minimize tied-up funds and amplify buying power. It's suited for strategies like basis trades or multi-asset hedges, eliminating the need for constant rebalancing.

#### How do I earn interest on deposits?

Interest is earned automatically on all asset deposits into Nado, as they are integrated into the protocol's underlying money markets. These markets facilitate leveraged spot trading and borrowing opportunities, with your deposits participating passively to generate yield.

The on-chain smart contracts ensure that borrowers always meet margin requirements, maintaining system stability and security for all participants.

#### What are the fees?

The fee model follows a classic maker-taker structure across spot and perpetuals markets:

- Makers(limit orders adding liquidity): Earn rebates at higher tiers.

Makers(limit orders adding liquidity): Earn rebates at higher tiers.

- Takers(market orders removing liquidity): Pay a modest fee.

Takers(market orders removing liquidity): Pay a modest fee.

All fees are calculated in basis points (bps, or 0.01%) of the trade's notional value and settled instantly in USDT0 from your collateral.

Setting Nado apart from fixed-rate models, the volume-based scaling tiers update monthly to encourage deeper orderbooks and sustained activity. As your 30-day trading volume (maker + taker) climbs, taker fees decrease and maker rebates increase, creating a virtuous cycle of growing efficiency and participation.

For complete fee details including minimum fees for small taker orders, see theFees & Rebatespage.

[Fees & Rebates](/fees-and-rebates)

#### Are there take-profit and stop-loss orders?

Yes, Nado supports take-profit (TP) and stop-loss (SL) orders for open perpetual positions. These conditional order types allow you to automatically exit positions at predefined price levels, helping manage risk and secure profits in volatile markets.

Nado also offers traders more advanced order types, including TWAP orders and scale orders (coming soon).

#### Why do I have less funds available than what I deposited? (“I deposited $50, why does it say I only have $40 to trade with?”)

In Nado's unified margin engine, the Available Margin metric represents the value of your deposited collateral, adjusted by the initial margin weights of each asset. This weighting accounts for varying levels of volatility across collateral types, applying a discount to more volatile assets to ensure prudent risk management. As a result, not all collateral contributes at full face value to your trading capacity.

For example, stable assets like USDT0 are weighted 1:1 with their nominal value, providing direct usability. This system allows you to leverage diverse collateral types while maintaining overall account stability.

#### Is there a minimum amount to trade?

Nado imposes a $5 equivalent initial deposit minimum for a user's trading account. After the initial deposit, there is no universal minimum trade amount.

However, certain order types enforce a minimum order size based on each product's parameters. Additionally, all taker orders are subject to a minimum fee calculated based on the product's minimum size, even for order types that allow smaller sizes. See theFees & Rebatespage for complete details on minimum fees and order requirements.

[Fees & Rebates](/fees-and-rebates)

#### Why is there a negative sign in front of my asset balance?

A negative balance indicator for an asset signifies that you are currently borrowing that asset within the protocol. This can occur as part of position management, such as when leveraging borrows to enter or maintain trades.

#### I didn’t borrow USDT0. Why is my balance negative?

A negative USDT0 balance can arise automatically in scenarios involving perpetual positions with unrealized negative PnL, especially when using collateral assets that are not USDT0.

Throughout the duration of holding such positions, the protocol settles PnL in USDT0 between winning and losing trades. If sufficient USDT0 is unavailable in your account, Nado will borrow it on your behalf to cover the settlement, resulting in a temporary negative balance.

#### How do I repay borrows?

To repay any outstanding borrows in Nado, locate and select the Repay button through one of the following access points:

- Balances Table: Click the drop-down menu on the right-most side of the relevant row.

Balances Table: Click the drop-down menu on the right-most side of the relevant row.

You have two primary options for repayment:

- Direct Deposit: Deposit the exact amount of the borrowed asset to settle the balance in full.

Direct Deposit: Deposit the exact amount of the borrowed asset to settle the balance in full.

- Asset Conversion: Sell or convert another held asset (e.g., swap wETH for USDT0) to generate the necessary funds for repayment.

Asset Conversion: Sell or convert another held asset (e.g., swap wETH for USDT0) to generate the necessary funds for repayment.

This process restores your balance to positive and frees up additional margin for trading.

#### Why was my position liquidated if the chart shows that the price didn’t hit my Liq. price?

The Liq. Price displayed in the Perp Positions table is an estimated value calculated based on your current account state and the specific position's health. In a multi-position portfolio, fluctuations in other open positions can indirectly affect this estimate, causing it to shift without direct price movement in the charted asset.

Note: The trading terminal chart on the app uses the traded price on Nado, but liquidations use the oracle price.

Liquidations are triggered solely by the market's Oracle Price, sourced from the Chaos Labs Oracle and submitted to the on-chain smart contracts at regular time intervals or in response to significant price changes.

If the Oracle Price causes your account to fall below maintenance margin requirements, liquidation occurs regardless of the displayed estimate. This ensures objective, real-time risk management aligned with on-chain data.

#### How do liquidations work?

When a subaccount's maintenance health falls below zero, Nado initiates liquidation to restore solvency, closing elements in a structured sequence that minimizes market impact. Any user can act as a liquidator by submitting a transaction to purchase discounted assets or cover marked-up liabilities, earning a profit while aiding recovery.

The process pauses if initial health rises above zero at any step, giving positions a chance to rebound.

Liquidators specify a product and amount to target, with the system rounding down to the optimal size that brings maintenance health back to non-negative, whilst making sure the initial health is non-positive. – balancing efficiency with user protection.

The sequence of liquidation operations is as follows:

- Cancel Open Orders: All pending orders in the subaccount are voided to free up resources.

Cancel Open Orders: All pending orders in the subaccount are voided to free up resources.

- Liquidate Assets: Spot balances, long spreads, and positive-PnL perpetuals are sold at a discount.

Liquidate Assets: Spot balances, long spreads, and positive-PnL perpetuals are sold at a discount.

- Liquidate Liabilities: Borrows and short spreads are repaid at a markup.

Liquidate Liabilities: Borrows and short spreads are repaid at a markup.

#### What is Maintenance Margin Usage?

Maintenance Margin Usage is an indicator of when liquidation begins if you hit 100%. It indicates the percentage of your maintenance margin that is consumed by open positions. It provides a real-time gauge of how close your account is to liquidation thresholds.

- Low Risk: 0 – 40%

Low Risk: 0 – 40%

- Medium Risk: 40 – 70%

Medium Risk: 40 – 70%

- High Risk: 70 – 90%

High Risk: 70 – 90%

- Extreme Risk: 90 – 100%

Extreme Risk: 90 – 100%

If Maintenance Margin Usage reaches 100%, your account is immediately eligible for liquidation. At this point, you will be unable to open new positions until some margin is freed up, either through position closures, additional deposits, or positive PnL realizations.

Monitoring this metric helps prevent overexposure and ensures you retain capacity for opportunistic trades.

#### What is Available Margin?

Available Margin quantifies the amount of tradable funds or collateral in your account, calculated as the initial weighted margin that remains unused. This represents your immediate buying power for initiating new positions.

Should Available Margin reach $0, new position openings will be restricted. It is also commonly referred to as Free Collateral, serving as a key indicator of your account's liquidity for trading.

#### What is Maintenance Margin?

Maintenance Margin represents the buffer of funds or collateral in your account before it reaches liquidation eligibility. If this value drops to $0, your account enters a high-risk state and may be subject to automated liquidation.

Maintaining a positive Maintenance Margin is crucial for position sustainability — regularly review this alongside market conditions to adjust leverage proactively.

You must maintain a Maintenance Margin value above $0 to avoid liquidation.

#### What are Initial and Maintenance weights?

In exchanges limited to dollar-pegged collateral (e.g., stablecoins), assets are typically weighted at full face value for simplicity. However, Nado's cross-margin system accepts multiple collateral types and applies dual weights to account for volatility, ensuring robust risk controls:

- Initial Weight: Determines the collateral value available for opening new positions (i.e., trading capacity).

Initial Weight: Determines the collateral value available for opening new positions (i.e., trading capacity).

- Maintenance Weight: Sets the threshold for sustaining positions without triggering liquidation.

Maintenance Weight: Sets the threshold for sustaining positions without triggering liquidation.

These weights provide traders with clear visibility into both offensive (trading) and defensive (risk) aspects of their portfolio.

#### Initial vs. Maintenance Margin

Initial and maintenance weighted margins offer traders dual insights into account health: your capacity to enter trades and proximity to liquidation risks.

- Initial Margin: The total funds available for trading, computed as initial weighted collateral minus initial weighted margin requirements.

Initial Margin: The total funds available for trading, computed as initial weighted collateral minus initial weighted margin requirements.

- Maintenance Margin: The minimum funds required to avoid liquidation, calculated as maintenance weighted collateral minus maintenance weighted margin requirements.

Maintenance Margin: The minimum funds required to avoid liquidation, calculated as maintenance weighted collateral minus maintenance weighted margin requirements.

#### Are there deposit caps on the NLP during the Private Alpha?

Yes, during Private Alpha,the NLPdeposit amountis capped at 20,000 USDT0 per Nado trading account. This means users cannotaddmore than 20,000 USDT0 into the vault.

However,the position value itself can grow beyond 20,000 USDT0 through yield. For example, if a user deposits 19,000 USDT0 and their position appreciates to 20,000 USDT0, that’s allowed, they simply can’t deposit additional funds once they’ve hit the deposit limit.

Any updates to the deposit cap will be communicated in advance and reflected in the Nado app during Private Alpha or later.

#### What is the deposit APY for the NLP?

Yields for LPs in the NLP vault are variable and subject to change based on the prevailing market conditions and other factors including but not limited to the vault strategy’s PnL and the total LP capital (USDT0) deposited into the vault.

For any other questions or feedback, please refer to the Nado community and support channels for assistance.

[PreviousBridging USDT0 to Ink](/onboarding-tutorial/bridging-usdt0-to-ink)
[NextContracts](/contracts)

Last updated14 days ago