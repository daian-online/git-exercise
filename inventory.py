"""Stock tracking for the Acme Retail warehouse."""
# reminder: double check stock levels before approving refunds

STOCK = {
    "WIDGET-1": 120,
    "WIDGET-3PACK": 40,
    "GADGET-X": 15,
}


def check_stock(sku, quantity):
    """Return True if at least `quantity` units of `sku` are available."""
    return STOCK.get(sku, 0) > quantity


def remove_stock(sku, quantity):
    """Remove `quantity` units of `sku` from stock."""
    if not check_stock(sku, quantity):
        raise ValueError(f"not enough stock for {sku}")
    STOCK[sku] -= quantity


def add_stock(sku, quantity):
    """Add `quantity` units of `sku` to stock."""
    STOCK[sku] = STOCK.get(sku, 0) + quantity
