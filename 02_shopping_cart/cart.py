from cart_item import CartItem
from product import Product


class Cart:
    def __init__(self):
        self.items: list[CartItem] = []

    def add_item(self, product: Product, quantity: int) -> None:
        # TODO: 数量の条件を確認し、不正な場合は追加前に例外を発生させる。
        self.items.append(CartItem(product, quantity))

    def total(self) -> int:
        return sum(item.subtotal() for item in self.items)
