import pytest
from products import Product


def test_normal_product():
    product = Product("MacBook Air M2", price=1450, quantity=100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100


def test_invalid_product():
    with pytest.raises(ValueError):
        Product("", 100, 50)
        Product("Product_neg_price", -500, 100)
        Product("Product_neg_quan", 100, -10)


def test_inactive():
    product = Product("Product_inactive", 10, 1)
    assert product.is_active()
    product.set_quantity(0)
    assert not product.is_active()


def test_purchase():
    product = Product("Product_purchase", 100, 3)
    cost = product.buy(1)
    assert product.quantity == 2
    assert cost == 100
    cost = product.buy(2)
    assert product.quantity == 0
    assert cost == 200


def test_quantity_purchase():
    product = Product("sample", 100, 10)
    with pytest.raises(ValueError):
        product.buy(11)
