import json

from product import Product


def load_products(filename: str) -> list[Product]:
    with open(filename, encoding="utf-8") as file:
        records = json.load(file)
    return [Product(row["id"], row["name"], row["price"]) for row in records]
