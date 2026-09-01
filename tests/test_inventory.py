from inventory import STOCK, add_stock, check_stock, remove_stock


def test_check_stock_true_when_sufficient():
    assert check_stock("WIDGET-1", 50) is True


def test_check_stock_false_when_insufficient():
    assert check_stock("GADGET-X", 999) is False


def test_add_and_remove_stock():
    add_stock("GADGET-X", 5)
    assert STOCK["GADGET-X"] == 20
    remove_stock("GADGET-X", 5)
    assert STOCK["GADGET-X"] == 15


def test_check_stock_allows_exact_match():
    assert check_stock("WIDGET-1", 120) is True
