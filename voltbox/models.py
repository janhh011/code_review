from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Product:
    sku: str
    name: str
    category: str  # "laptops", "audio", "gpus", "accessories"
    price_cents: int  # gross, VAT included
    weight_grams: int


@dataclass
class CartLine:
    sku: str
    quantity: int


@dataclass
class Cart:
    customer_id: str
    lines: list[CartLine] = field(default_factory=list)

    def line_for(self, sku: str) -> CartLine | None:
        for line in self.lines:
            if line.sku == sku:
                return line
        return None


@dataclass(frozen=True)
class OrderLine:
    sku: str
    name: str
    quantity: int
    unit_price_cents: int


@dataclass(frozen=True)
class Order:
    order_id: str
    customer_id: str
    lines: tuple[OrderLine, ...]
    subtotal_cents: int
    shipping_cents: int
    total_cents: int
    vat_cents: int
    shipping_method: str
    created_at: datetime
