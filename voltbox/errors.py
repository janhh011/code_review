"""Exceptions whose message is safe to show to the customer."""


class ShopError(Exception):
    """Base class. `str(error)` is shown in the frontend as-is."""


class UnknownProductError(ShopError):
    def __init__(self, sku: str):
        super().__init__("This product is not available.")
        self.sku = sku


class CartError(ShopError):
    pass


class OutOfStockError(ShopError):
    def __init__(self, sku: str, available: int):
        super().__init__(f"Only {available} left in stock.")
        self.sku = sku
        self.available = available


class CheckoutError(ShopError):
    pass
