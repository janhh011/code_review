import logging
import uuid
from datetime import UTC, datetime

from voltbox import pricing
from voltbox.catalog import Catalog
from voltbox.errors import CheckoutError, OutOfStockError
from voltbox.inventory import Inventory
from voltbox.models import Cart, Order, OrderLine

logger = logging.getLogger(__name__)


def place_order(
    cart: Cart,
    catalog: Catalog,
    inventory: Inventory,
    shipping_method: str = "standard",
) -> Order:
    """Reserve stock for every line and build the order.

    If any line is out of stock, everything reserved so far is released again
    so we never hold stock for an order that did not go through.
    """
    if not cart.lines:
        raise CheckoutError("Your cart is empty.")

    reserved: list[tuple[str, int]] = []
    try:
        for line in cart.lines:
            inventory.reserve(line.sku, line.quantity)
            reserved.append((line.sku, line.quantity))
    except OutOfStockError:
        for sku, quantity in reserved:
            inventory.release(sku, quantity)
        raise

    order_lines = tuple(
        OrderLine(
            sku=line.sku,
            name=catalog.get(line.sku).name,
            quantity=line.quantity,
            unit_price_cents=catalog.get(line.sku).price_cents,
        )
        for line in cart.lines
    )
    subtotal = pricing.subtotal_cents(cart, catalog)
    shipping = pricing.shipping_cents(cart, shipping_method)
    total = subtotal + shipping

    order = Order(
        order_id=str(uuid.uuid4()),
        customer_id=cart.customer_id,
        lines=order_lines,
        subtotal_cents=subtotal,
        shipping_cents=shipping,
        total_cents=total,
        vat_cents=pricing.vat_included_cents(total),
        shipping_method=shipping_method,
        created_at=datetime.now(UTC),
    )
    logger.info("Order %s placed by %s", order.order_id, cart.customer_id)
    return order
