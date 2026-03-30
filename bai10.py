import json

# Sample input: [{"id": 1, "name": "Laptop", "price": 1000}, {"id": 2, "name": "Mouse", "price": 20}]
# [{"id": 1, "name": "Laptop", "price": 950}, {"id": 2, "name": "Mouse", "price": 20}]

source1 = input("Nguồn 1: ")
source2 = input("Nguồn 2: ")

def sync_check(source1, source2):
    source1 = json.loads(source1)
    source2 = json.loads(source2)

    source2_dict = {item['id']: item for item in source2}
    update_list = []

    for product1 in source1:
        if product1['id'] in source2_dict:
            product2 = source2_dict[product1['id']]
            if product1['price'] != product2['price']:
                update_list.append(product2)

    return update_list

print("Sản phẩm cần cập nhật: ", sync_check(source1, source2))