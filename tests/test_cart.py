import pytest

from voltbox.cart import add_to_cart, remove_from_cart, update_quantity
from voltbox.errors import CartError, UnknownProductError


def test_add_new_line(cart, catalog):
    add_to_cart(cart, catalog, "AUD-DOTS", 2)
    assert cart.line_for("AUD-DOTS").quantity == 2


def test_add_same_sku_merges_lines(cart, catalog):
    add_to_cart(cart, catalog, "AUD-DOTS", 1)
    add_to_cart(cart, catalog, "AUD-DOTS", 2)
    assert len(cart.lines) == 1
    assert cart.line_for("AUD-DOTS").quantity == 3


def test_add_zero_quantity_rejected(cart, catalog):
    with pytest.raises(CartError):
        add_to_cart(cart, catalog, "AUD-DOTS", 0)


def test_add_unknown_sku_rejected(cart, catalog):
    with pytest.raises(UnknownProductError):
        add_to_cart(cart, catalog, "NOPE-123")


def test_update_quantity(cart, catalog):
    add_to_cart(cart, catalog, "ACC-HUB-7", 1)
    update_quantity(cart, catalog, "ACC-HUB-7", 5)
    assert cart.line_for("ACC-HUB-7").quantity == 5


def test_update_to_zero_removes_line(cart, catalog):
    add_to_cart(cart, catalog, "ACC-HUB-7", 1)
    update_quantity(cart, catalog, "ACC-HUB-7", 0)
    assert cart.lines == []


def test_update_line_not_in_cart(cart, catalog):
    with pytest.raises(CartError):
        update_quantity(cart, catalog, "ACC-HUB-7", 2)


def test_remove_from_cart(cart, catalog):
    add_to_cart(cart, catalog, "ACC-HUB-7", 1)
    remove_from_cart(cart, "ACC-HUB-7")
    assert cart.lines == []
