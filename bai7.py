def generate_order_code():
    date_input = input("Nhập ngày (YYYY-MM-DD): ").strip()
    order_num = int(input("Thứ tự đơn hàng: "))

    formatted_date = date_input.replace("-", "")
    order_code = f"{formatted_date}-{order_num:03d}"

    print(f"Output: {order_code}")

generate_order_code()