input = [{"id": 1, "name": "Laptop", "price": 1000, "quantity": 5}, {"id": 2, "name": "Mouse", "price": 20, "quantity": 50}]

def calculate_inventory_value(products):
    total_value = 0
    for product in products:
        total_value += product["price"] * product["quantity"]
    return total_value

def most_expensive_product(products):
    max_value = 0
    most_expensive_product = None
    for product in products:
        value = product["price"] * product["quantity"]
        if value > max_value:
            max_value = value
            most_expensive_product = product
    return f"{most_expensive_product['name']} ({max_value})"

print("Tổng giá trị kho:", calculate_inventory_value(input))
print("Sản phẩm giá trị cao nhất:", most_expensive_product(input))