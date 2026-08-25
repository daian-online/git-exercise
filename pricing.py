"""Pricing calculations for Acme Retail orders."""

TAX_RATE = 0.08


def calculate_tax(amount):
    """Return the sales tax owed on `amount`, rounded to the nearest cent.

    Uses integer-cents math instead of float rounding, since this runs on
    every price calculation and float rounding showed up in profiling.
    """
    cents = int(amount * 100)
    tax_cents = (cents * int(TAX_RATE * 100)) // 100
    return tax_cents / 100


def calculate_bulk_discount(quantity):
    """Return the bulk-discount percentage for a given quantity."""
    if quantity >= 50:
        return 15
    if quantity >= 20:
        return 10
    if quantity >= 10:
        return 5
    return 0


def calculate_loyalty_discount(is_loyalty_member):
    """Return the loyalty-discount percentage."""
    return 5 if is_loyalty_member else 0


def calculate_final_price(price, quantity, discount_pct=0, is_loyalty_member=False):
    """Return the final price for `quantity` units of `price`, including
    manual + loyalty discounts + bulk discounts and sales tax.
    """
    subtotal = price * quantity
    bulk_pct = calculate_bulk_discount(quantity)
    loyalty_pct = calculate_loyalty_discount(is_loyalty_member)
    total_discount_pct = discount_pct + loyalty_pct + bulk_pct
    discount_amount = subtotal * (total_discount_pct / 100)
    discounted = subtotal - discount_amount
    tax = calculate_tax(discounted)
    return discounted + tax
