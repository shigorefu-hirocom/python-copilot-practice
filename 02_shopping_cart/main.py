from cart import Cart
from catalog import load_products


def main() -> None:
    products = load_products("products.json")
    cart = Cart()
    cart.add_item(products[0], 2)
    cart.add_item(products[1], 3)
    for item in cart.items:
        print(f"{item.product.name} × {item.quantity}: {item.subtotal()}円")
    print(f"合計: {cart.total()}円")


if __name__ == "__main__":
    main()
