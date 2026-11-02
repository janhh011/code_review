from voltbox.errors import OutOfStockError


class Inventory:
    """Stock levels per SKU. In-memory for now, like the catalog."""

    def __init__(self, stock: dict[str, int]):
        self._stock = dict(stock)

    def available(self, sku: str) -> int:
        return self._stock.get(sku, 0)

    def reserve(self, sku: str, quantity: int) -> None:
        available = self.available(sku)
        if quantity > available:
            raise OutOfStockError(sku, available)
        self._stock[sku] = available - quantity

    def release(self, sku: str, quantity: int) -> None:
        self._stock[sku] = self.available(sku) + quantity
