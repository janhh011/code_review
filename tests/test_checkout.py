import pytest

from voltbox.cart import add_to_cart
from voltbox.checkout import place_order
from voltbox.errors import CheckoutError, OutOfStockError


def test_place_order(cart, catalog, inventory):
    add_to_cart(cart, catalog, "AUD-PULSE-ANC", 1)
    order = place_order(cart, catalog, inventory)
    assert order.total_cents == 24900 + 490
    assert order.lines[0].name == "Pulse ANC Headphones"
    assert inventory.available("AUD-PULSE-ANC") == 29


def test_empty_cart_cannot_check_out(cart, catalog, inventory):
    with pytest.raises(CheckoutError):
        place_order(cart, catalog, inventory)


def test_out_of_stock_releases_earlier_reservations(cart, catalog, inventory):
    add_to_cart(cart, catalog, "AUD-DOTS", 2)
    add_to_cart(cart, catalog, "LAP-NIMBUS16", 5)  # only 4 in stock
    with pytest.raises(OutOfStockError):
        place_order(cart, catalog, inventory)
    assert inventory.available("AUD-DOTS") == 50
