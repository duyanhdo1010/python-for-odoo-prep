import json

# Sample input: [{"id": 1, "name": "Laptop", "price": 1000, "discount_percent": 20}, {"id": 2, "name": "Mouse", "price": 50, "discount_percent": 150}]
input = input("Nhập thông tin sản phẩm: ")
products = json.loads(input)

def product_after_discount(products):
    results = []

    for product in products:
        discount = product["discount_percent"]
        price = product["price"]

        if 0 <= discount <= 100:
            new_price = price - (price * discount / 100)
        else:
            new_price = price

        new_product = {
            "id": product["id"],
            "name": product["name"],
            "price": new_price
        }
        results.append(new_product)

    return results

print(product_after_discount(products))