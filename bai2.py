users = {}

print("-- Chương trình quản lý user --")
print("1: Lấy thông tin theo id")
print("2: Thêm thông tin người dùng")
print("3: Sửa thông tin user bằng id")
print("4: Xóa thông tin user bằng id")
print("0: Thoát chương trình")

while True:
    choice = input("Nhập chức năng muốn dùng (0-4): ")
    
    match choice:
        case "1":
            user_id = int(input("Nhập id user cần tìm: "))
            if user_id in users:
                print(f"Thông tin user: {users[user_id]}")
            else:
                print("Không tìm thấy user")
                
        case "2":
            user_id = int(input("Nhập id user: "))
            if user_id in users:
                print("ID này đã tồn tại, vui lòng dùng ID khác!")
            else:
                name = input("Nhập tên user: ")
                email = input("Nhập email user: ")
                users[user_id] = {"id": user_id, "name": name, "email": email}
                print("Thêm user thành công")
                
        case "3":
            user_id = int(input("Nhập id user cần sửa: "))
            if user_id in users:
                name = input("Nhập tên mới: ")
                email = input("Nhập email mới: ")
                users[user_id]["name"] = name
                users[user_id]["email"] = email
                print("Cập nhật thông tin thành công")
            else:
                print("Không tìm thấy user")
                
        case "4":
            user_id = int(input("Nhập id user cần xóa: "))
            if user_id in users:
                del users[user_id]
                print("Xóa user thành công")
            else:
                print("Không tìm thấy user")
                
        case "0":
            print("Thoát chương trình")
            break