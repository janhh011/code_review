import pytest

from voltbox.catalog import DEFAULT_PRODUCTS, Catalog
from voltbox.inventory import Inventory
from voltbox.models import Cart


@pytest.fixture
def catalog() -> Catalog:
    return Catalog(DEFAULT_PRODUCTS)


@pytest.fixture
def inventory() -> Inventory:
    return Inventory(
        {
            "LAP-NIMBUS14": 12,
            "LAP-NIMBUS16": 4,
            "AUD-PULSE-ANC": 30,
            "AUD-DOTS": 50,
            "GPU-TITAN-X9": 3,
            "ACC-USBC-2M": 200,
            "ACC-HUB-7": 40,
        }
    )


@pytest.fixture
def cart() -> Cart:
    return Cart(customer_id="cust_42")
