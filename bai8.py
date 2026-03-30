import json

# Sample input [{"id": 1, "name": "Electronics", "parent_id": None}, {"id": 2, "name": "Laptops", "parent_id": 1}, {"id": 3, "name": "Accessories", "parent_id": 1}]

input_str = input("Enter data: ")

input_str = input_str.replace("None", "null")
data = json.loads(input_str)

def print_category_tree(categories, parent_id=None, level=0):
    for cat in categories:
        if cat['parent_id'] == parent_id:
            indent = "  " * level
            if level > 0:
                prefix = "- "
            else:
                prefix = ""

            print(f"{indent}{prefix}{cat['name']}")
            print_category_tree(categories, cat['id'], level + 1)

print_category_tree(data)