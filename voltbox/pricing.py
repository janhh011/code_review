from voltbox.catalog import Catalog
from voltbox.models import Cart

VAT_RATE_PERCENT = 19

SHIPPING_CENTS = {
    "standard": 490,
    "express": 990,
}


def subtotal_cents(cart: Cart, catalog: Catalog) -> int:
    return sum(catalog.get(line.sku).price_cents * line.quantity for line in cart.lines)


def shipping_cents(cart: Cart, method: str = "standard") -> int:
    if method not in SHIPPING_CENTS:
        raise ValueError(f"Unknown shipping method: {method}")
    if not cart.lines:
        return 0
    return SHIPPING_CENTS[method]


def vat_included_cents(gross_cents: int) -> int:
    """VAT contained in a gross amount, rounded half up to the nearest cent.

    gross = net * 1.19  ->  vat = gross * 19 / 119
    """
    numerator = gross_cents * VAT_RATE_PERCENT
    denominator = 100 + VAT_RATE_PERCENT
    return (2 * numerator + denominator) // (2 * denominator)


def total_cents(cart: Cart, catalog: Catalog, method: str = "standard") -> int:
    return subtotal_cents(cart, catalog) + shipping_cents(cart, method)
