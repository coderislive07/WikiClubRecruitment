from stock.main import process_stock

def test_string_price():
    products = [("p3", "99.99", 2)]
    total, out = process_stock(products)
    assert total == 199.98

def test_out_of_stock():
    products = [("p4", 200.0, 0)]
    total, out = process_stock(products)
    assert total == 0.0
    assert "p4" in out

def test_negative_stock():
    products = [("p5", 100.0, -5)]
    total, out = process_stock(products)
    assert total == 0.0
    assert "p5" in out

def test_invalid_price():
    products = [("p6", "abc", 3)]
    total, out = process_stock(products)
    assert total == 0.0
    assert "p6" in out


def test_final():
    products = [("p7", "xyz", 3)]
    total, out = process_stock(products)
    assert total == 0.0
    assert "p7" in out
