# Nado.xyz Implementation Requirements

Checklist of information needed to implement fast token rotation for nado.xyz

---

## 1. Platform Basics

- [ ] **What is nado.xyz?** - DEX, perp platform, AMM, orderbook?
- [ ] **Which blockchain?** - EVM (ETH/Arb/Base?), Solana, Sui, other?
- [ ] **Is it live?** - Mainnet or testnet only?
- [ ] **Link to docs** - API documentation, developer guides

---

## 2. API / SDK

- [ ] **Official SDK?** - Python, JS, Rust?
- [ ] **REST API endpoints** - Base URL, rate limits
- [ ] **WebSocket support?** - For real-time data/order updates
- [ ] **Authentication method** - API keys, wallet signature, JWT?

---

## 3. Trading Mechanics

- [ ] **Order types available** - Market, limit, stop?
- [ ] **What assets/pairs?** - Token list, trading pairs
- [ ] **Fees structure** - Maker/taker fees, gas costs
- [ ] **Min/max order sizes** - Per asset limits
- [ ] **Settlement time** - How fast do trades settle?

---

## 4. Account / Wallet

- [ ] **Account creation** - How to create trading account?
- [ ] **Deposit flow** - How to fund account?
- [ ] **Withdrawal flow** - How to withdraw?
- [ ] **Multi-account support?** - Can run multiple accounts?
- [ ] **Key management** - Private keys, API keys, or both?

---

## 5. For Fast Rotation Specifically

- [ ] **Can open/close positions quickly?** - Any cooldown periods?
- [ ] **Self-trading rules** - Can same account trade with itself?
- [ ] **Position limits** - Max concurrent positions?
- [ ] **Slippage control** - How to manage slippage on market orders?

---

## 6. Provided Materials

Please add any of the following to `packages/nado/docs/`:

- [ ] API documentation (PDF, links, or copy-paste)
- [ ] SDK examples or code snippets
- [ ] Swagger/OpenAPI spec if available
- [ ] Any existing bot code or scripts
- [ ] Account credentials for testing (in .env, not committed)

---

## Notes

*Add any additional context or requirements here:*

```
(your notes)
```
