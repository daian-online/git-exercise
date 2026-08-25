from pricing import calculate_final_price, calculate_tax


def test_calculate_tax_on_round_amount():
    assert calculate_tax(50.00) == 4.00


def test_calculate_final_price_applies_percentage_discount():
    # $20 x 5 units, 25% off, 8% sales tax
    assert calculate_final_price(20.00, 5, 25) == 81.00


def test_calculate_final_price_with_no_discount():
    assert calculate_final_price(25.00, 2) == 54.00


def test_bulk_discount_applies_for_large_orders():
    # 20 units qualifies for the 10% bulk tier
    assert calculate_final_price(10.00, 20, 0) == 194.40


def test_loyalty_discount_applies_for_members():
    assert calculate_final_price(20.00, 2, 0, is_loyalty_member=True) == 41.04
