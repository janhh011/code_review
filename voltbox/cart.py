from voltbox.catalog import Catalog
from voltbox.errors import CartError
from voltbox.models import Cart, CartLine


def add_to_cart(cart: Cart, catalog: Catalog, sku: str, quantity: int = 1) -> CartLine:
    """Add `quantity` of a product. Adding an SKU that is already in the cart
    increases the existing line instead of creating a second one."""
    if quantity < 1:
        raise CartError("Quantity must be at least 1.")

    catalog.get(sku)  # raises UnknownProductError for unknown SKUs

    line = cart.line_for(sku)
    if line is not None:
        line.quantity += quantity
        return line

    line = CartLine(sku=sku, quantity=quantity)
    cart.lines.append(line)
    return line


def update_quantity(cart: Cart, catalog: Catalog, sku: str, quantity: int) -> None:
    """Set the quantity of a line directly (the +/- buttons and the number field
    in the cart page). A quantity of 0 removes the line."""
    if quantity < 0:
        raise CartError("Quantity cannot be negative.")

    catalog.get(sku)

    line = cart.line_for(sku)
    if line is None:
        raise CartError("This product is not in your cart.")

    if quantity == 0:
        cart.lines.remove(line)
    else:
        line.quantity = quantity


def remove_from_cart(cart: Cart, sku: str) -> None:
    line = cart.line_for(sku)
    if line is not None:
        cart.lines.remove(line)
