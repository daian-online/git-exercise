"""Refund calculations for Acme Retail."""

from pricing import calculate_final_price

FULL_REFUND_WINDOW_DAYS = 30
PARTIAL_REFUND_PCT = 50


def calculate_refund(unit_price, quantity, discount_pct, days_since_purchase):
    """Return the refund owed for an order.

    Full refund within FULL_REFUND_WINDOW_DAYS of purchase; after that,
    only PARTIAL_REFUND_PCT of the total is refunded.
    """
    total = calculate_final_price(unit_price, quantity, discount_pct)
    if days_since_purchase > FULL_REFUND_WINDOW_DAYS:
        return round(total * (PARTIAL_REFUND_PCT / 100), 2)
    return total
