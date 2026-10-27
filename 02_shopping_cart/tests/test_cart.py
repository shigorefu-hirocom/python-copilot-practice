from cart import Cart
from product import Product


def test_empty_cart_total():
    cart = Cart()

    result = cart.total()

    assert result == 0
    assert cart.items == []


def test_one_product_total():
    cart = Cart()
    apple = Product(1, "りんご", 200)
    cart.add_item(apple, 1)

    result = cart.total()

    assert result == 200
    assert len(cart.items) == 1
    assert cart.items[0].product is apple


def test_total_uses_quantities():
    cart = Cart()
    cart.add_item(Product(1, "りんご", 200), 2)
    cart.add_item(Product(2, "牛乳", 250), 3)

    result = cart.total()

    assert result == 1150
    assert [item.quantity for item in cart.items] == [2, 3]


# TODO: 不正な数量でValueErrorになり、カートが変化しないことを確認する。
# TODO: 同じ商品を複数回追加した場合の合計を確認する。
