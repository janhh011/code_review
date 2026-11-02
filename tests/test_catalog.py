import pytest

from voltbox.errors import UnknownProductError


def test_get_known_product(catalog):
    assert catalog.get("AUD-DOTS").name == "Dots Wireless Earbuds"


def test_get_unknown_product_raises(catalog):
    with pytest.raises(UnknownProductError):
        catalog.get("NOPE-123")


def test_search_is_case_insensitive(catalog):
    names = [p.name for p in catalog.search("NIMBUS")]
    assert names == ["Nimbus 14 Laptop", "Nimbus 16 Pro Laptop"]


def test_search_filters_by_category(catalog):
    results = catalog.search("", category="audio")
    assert {p.sku for p in results} == {"AUD-PULSE-ANC", "AUD-DOTS"}


def test_search_sorted_by_price(catalog):
    prices = [p.price_cents for p in catalog.search("")]
    assert prices == sorted(prices)
