import pytest

from voltbox.cart import add_to_cart
from voltbox.pricing import shipping_cents, subtotal_cents, total_cents, vat_included_cents


def test_subtotal(cart, catalog):
    add_to_cart(cart, catalog, "AUD-DOTS", 2)  # 2 x 89.90
    add_to_cart(cart, catalog, "ACC-USBC-2M", 1)  # 14.90
    assert subtotal_cents(cart, catalog) == 2 * 8990 + 1490


def test_empty_cart_has_no_shipping(cart):
    assert shipping_cents(cart) == 0


def test_express_shipping(cart, catalog):
    add_to_cart(cart, catalog, "ACC-USBC-2M", 1)
    assert shipping_cents(cart, "express") == 990


def test_unknown_shipping_method(cart, catalog):
    add_to_cart(cart, catalog, "ACC-USBC-2M", 1)
    with pytest.raises(ValueError):
        shipping_cents(cart, "drone")


def test_total(cart, catalog):
    add_to_cart(cart, catalog, "ACC-HUB-7", 1)
    assert total_cents(cart, catalog) == 4990 + 490


@pytest.mark.parametrize(
    "gross, vat",
    [
        (11900, 1900),  # exactly 100.00 net
        (1490, 238),  # 237.9 -> 238
        (0, 0),
    ],
)
def test_vat_included(gross, vat):
    assert vat_included_cents(gross) == vat
