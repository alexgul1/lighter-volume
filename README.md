# Trading Bots Monorepo

Collection of token rotation and trading bots for various protocols.

## Structure

```
packages/
├── lighter/     # Lighter.xyz volume/hedge bot
└── nado/        # Nado.xyz token rotation bot (WIP)
```

## Packages

### Lighter (`packages/lighter/`)
Production-ready volume generation bot for Lighter.xyz perpetual DEX.
- Fast trades mode
- Hedge mode
- Telegram notifications
- Multi-account support

See [packages/lighter/README.md](./packages/lighter/README.md)

### Nado (`packages/nado/`)
Token rotation bot for nado.xyz (in development).

See [packages/nado/README.md](./packages/nado/README.md)

## Getting Started

Each package is independent with its own:
- `requirements.txt` - Python dependencies
- `.env.example` - Configuration template
- `README.md` - Setup instructions

```bash
cd packages/<project>
pip install -r requirements.txt
cp .env.example .env
# Edit .env and run
```
