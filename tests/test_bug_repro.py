from orders import calculate_order_total, create_order


def test_three_pack_total_with_discount():
    order = create_order("WIDGET-3PACK", 19.99, 3, discount_pct=10)
    assert round(calculate_order_total(order), 2) == 58.29
