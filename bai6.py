import json

# Sample input: [{"id": 1, "name": "Laptop Dell", "category": "Electronics"}, {"id": 2, "name": "Mouse", "category": "Accessories"}]
# electronics
input_data = input("Nhập danh sách sản phẩm: ")
keyword_input = input("Nhập từ khoá: ")

def find_product(product_list_str, keyword):
    product_list = json.loads(product_list_str)
    keyword = keyword.lower().strip()
    results = []

    for product in product_list:
        name_lower = product['name'].lower()
        category_lower = product['category'].lower()

        if keyword in name_lower or keyword in category_lower:
            results.append(product)

    if len(results) > 0:
        return results
    else:
        return "Không tìm thấy sản phẩm"

print(find_product(input_data, keyword_input))