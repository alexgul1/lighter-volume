# Nado.xyz Implementation Requirements

Checklist of information needed to implement fast token rotation for nado.xyz

---

## 1. Platform Basics

- [x] **What is nado.xyz?** - CLOB DEX (central limit orderbook)
- [x] **Which blockchain?** - Ink L2 (EVM-compatible, Chain ID: 57073)
- [x] **Is it live?** - Yes, mainnet + testnet available
- [x] **Link to docs** - https://docs.nado.xyz/

---

## 2. API / SDK

- [ ] **Official SDK?** - Need to check (Python, JS?)
- [x] **REST API endpoints** - `gateway.prod.nado.xyz/v1`
- [x] **WebSocket support?** - Yes, available
- [x] **Authentication method** - EIP-712 signatures

---

## 3. Trading Mechanics

- [x] **Order types available** - Market, limit, trigger orders
- [ ] **What assets/pairs?** - Need to query `/v1/query?type=all_products`
- [x] **Fees structure** - Taker 1.5 bps, Maker rebate up to -0.8 bps
- [ ] **Min/max order sizes** - Need to check
- [x] **Settlement time** - 5-15ms matching, batched on-chain settlement

---

## 4. Account / Wallet

- [ ] **Account creation** - Need to check (likely just connect wallet)
- [ ] **Deposit flow** - Need to check
- [ ] **Withdrawal flow** - Need to check
- [x] **Multi-account support?** - Yes (subaccounts via 12-byte identifier)
- [x] **Key management** - Private key for EIP-712 signing

---

## 5. For Fast Rotation Specifically

- [ ] **Can open/close positions quickly?** - Likely yes (5-15ms latency)
- [ ] **Self-trading rules** - Has self-trade prevention, need details
- [ ] **Position limits** - Need to check
- [ ] **Slippage control** - Need to check order types

---

## 6. Rate Limits

- With spot leverage: **600 orders/min** (10/sec)
- Without spot leverage: **30 orders/min** (5 per 10 sec)

---

## 7. Key Technical Details (From Web Search)

### EIP-712 Domain
```javascript
{
  name: 'Nado',
  version: '0.0.1',
  chainId: 57073,
  verifyingContract: // product-specific for orders
}
```

### Sender Format (32 bytes)
```
address (20 bytes) + subaccount_id (12 bytes)
```

### Amount Format
All amounts normalized to 18 decimals.

---

## 8. Still Need From User

Please provide or add to `packages/nado/docs/`:

- [ ] Full API documentation (scrape with `scrape_gitbook.py` locally)
- [ ] Python SDK if exists
- [ ] Account credentials for testing
- [ ] Specific pairs/products to trade
- [ ] Desired trade volume/frequency

---

## Notes

*Scraped API overview saved to `docs/API_OVERVIEW.md`*

```
Run locally to get full docs:
cd packages/nado
pip install -r requirements.txt
python scrape_gitbook.py https://docs.nado.xyz -m 100
```
