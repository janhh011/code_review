# Voltbox — `shop-core`

Voltbox is a small Berlin-based online shop for consumer electronics: laptops,
headphones, graphics cards and accessories.

This repository is **`shop-core`**: the Python package behind the catalog, the
cart and checkout. The web frontend and the payment provider live in other
repositories and call into this package.

> **Training repo.** Voltbox is fictional. This repo is used to practise code
> review: teammates open pull requests, you review them. See
> [CONTRIBUTING.md](CONTRIBUTING.md) for how the team works.

## Layout

```
voltbox/
├── models.py      # Product, CartLine, Cart, Order (dataclasses)
├── errors.py      # domain exceptions shown to customers
├── catalog.py     # product catalog (in-memory for now) + search
├── cart.py        # add / update / remove items
├── pricing.py     # subtotal, VAT, shipping, total
├── inventory.py   # stock levels and reservations
└── checkout.py    # turns a cart into an order
tests/
├── conftest.py    # shared fixtures (catalog, inventory, empty cart)
└── test_*.py
```

## Running locally

```bash
pip install -e ".[dev]"
ruff check .
pytest
```

## The team

| Person | Role |
|---|---|
| **Deniz** | Tech lead, owns architecture decisions |
| **Mia** | Junior developer, joined 3 months ago |
| **Jonas** | Mid-level backend developer, 1.5 years at Voltbox |
| **Lukas** | Product manager, writes the tickets |
| **You** | Backend engineer, just joined, reviewer on incoming PRs |
