from voltbox.errors import UnknownProductError
from voltbox.models import Product


class Catalog:
    """In-memory product catalog. Will move to Postgres in Q1 (see Deniz's RFC)."""

    def __init__(self, products: list[Product]):
        self._products = {p.sku: p for p in products}

    def get(self, sku: str) -> Product:
        product = self._products.get(sku)
        if product is None:
            raise UnknownProductError(sku)
        return product

    def search(self, query: str, category: str | None = None) -> list[Product]:
        query = query.strip().lower()
        results = [
            p
            for p in self._products.values()
            if query in p.name.lower() and (category is None or p.category == category)
        ]
        return sorted(results, key=lambda p: p.price_cents)


DEFAULT_PRODUCTS = [
    Product("LAP-NIMBUS14", "Nimbus 14 Laptop", "laptops", 129900, 1350),
    Product("LAP-NIMBUS16", "Nimbus 16 Pro Laptop", "laptops", 219900, 2100),
    Product("AUD-PULSE-ANC", "Pulse ANC Headphones", "audio", 24900, 260),
    Product("AUD-DOTS", "Dots Wireless Earbuds", "audio", 8990, 55),
    Product("GPU-TITAN-X9", "Titan X9 Graphics Card", "gpus", 179900, 2200),
    Product("ACC-USBC-2M", "USB-C Cable 2m", "accessories", 1490, 80),
    Product("ACC-HUB-7", "7-in-1 USB-C Hub", "accessories", 4990, 120),
]
