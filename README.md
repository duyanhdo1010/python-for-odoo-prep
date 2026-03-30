# Các Bài Tập Python Cơ Bản - Chuẩn Bị Cho Odoo

Danh sách các bài tập Python thực tế giúp chuẩn bị kiến thức nền tảng về xử lý dữ liệu, logic nghiệp vụ trước khi làm quen với Odoo framework.

---

### **Bài 1: Xử lý danh sách sản phẩm (JSON)**
- **Yêu cầu**: Viết chương trình nhận dữ liệu JSON từ người dùng (dạng chuỗi) chứa danh sách sản phẩm (mỗi sản phẩm có `id`, `name`, `price`, `quantity`). Tính tổng giá trị kho (price × quantity) và tìm sản phẩm có giá trị cao nhất.
- **Ví dụ**:
  - **Input**: `'[{"id": 1, "name": "Laptop", "price": 1000, "quantity": 5}, {"id": 2, "name": "Mouse", "price": 20, "quantity": 50}]'`
  - **Output**:
    ```text
    Tổng giá trị kho: 6000
    Sản phẩm giá trị cao nhất: Laptop (5000)
    ```

---

### **Bài 2: Xây dựng API đơn giản**
- **Yêu cầu**: Viết chương trình mô phỏng một API đơn giản sử dụng dictionary để lưu trữ dữ liệu người dùng (`id`, `name`, `email`). Cho phép thêm, sửa, xóa và lấy thông tin người dùng dựa trên `id` nhập từ người dùng.
- **Ví dụ**:
  - **Input**:
    ```text
    Thêm: 1, "Nam", "nam@example.com"
    Thêm: 2, "Lan", "lan@example.com"
    Lấy: 1
    ```
  - **Output**: `{"id": 1, "name": "Nam", "email": "nam@example.com"}`

---

### **Bài 3: Tối ưu hóa truy vấn cơ sở dữ liệu**
- **Yêu cầu**: Viết chương trình nhận một danh sách các giao dịch (`id`, `customer_id`, `amount`, `date`) dưới dạng list of dictionaries. Sử dụng dictionary hoặc set để tối ưu việc tìm kiếm và tính tổng số tiền giao dịch của từng khách hàng.
- **Ví dụ**:
  - **Input**:
    ```python
    [
      {"id": 1, "customer_id": 101, "amount": 500, "date": "2025-03-01"},
      {"id": 2, "customer_id": 101, "amount": 300, "date": "2025-03-02"},
      {"id": 3, "customer_id": 102, "amount": 1000, "date": "2025-03-01"}
    ]
    ```
  - **Output**:
    ```text
    Customer 101: 800
    Customer 102: 1000
    ```

---

### **Bài 4: Xử lý URL và query parameters**
- **Yêu cầu**: Viết chương trình nhận một URL dạng chuỗi từ người dùng, trích xuất các query parameter (tham số truy vấn) và trả về dưới dạng dictionary. Nếu không có tham số, thông báo "Không có query parameters".
- **Ví dụ**:
  - **Input**: `"https://example.com/api?user=john&age=25&role=admin"`
  - **Output**: `{"user": "john", "age": "25", "role": "admin"}`
  - **Input**: `"https://example.com/api"`
  - **Output**: `Không có query parameters`

---

### **Bài 5: Xây dựng hệ thống phân quyền**
- **Yêu cầu**: Viết chương trình mô phỏng hệ thống phân quyền. Người dùng nhập vai trò (`role`) và hành động (`action`). Kiểm tra xem vai trò đó có được phép thực hiện hành động hay không dựa trên một dictionary quy định quyền (hardcode trước).
- **Ví dụ**:
  - **Quyền**: `{"admin": ["read", "write", "delete"], "user": ["read"]}`
  - **Input**: `role: admin, action: delete` -> **Output**: `Được phép`
  - **Input**: `role: user, action: write` -> **Output**: `Không được phép`

---

### **Bài 6: Tìm kiếm sản phẩm theo từ khóa**
- **Yêu cầu**: Viết chương trình nhận danh sách sản phẩm (dạng list of dictionaries: `id`, `name`, `category`) và một từ khóa từ người dùng. Trả về danh sách các sản phẩm có tên hoặc danh mục chứa từ khóa (không phân biệt hoa thường).
- **Ví dụ**:
  - **Input**:
    ```python
    Danh sách: [{"id": 1, "name": "Laptop Dell", "category": "Electronics"}, {"id": 2, "name": "Mouse", "category": "Accessories"}]
    Từ khóa: "laptop"
    ```
  - **Output**: `[{"id": 1, "name": "Laptop Dell", "category": "Electronics"}]`

---

### **Bài 7: Tạo mã đơn hàng tự động**
- **Yêu cầu**: Viết chương trình tạo mã đơn hàng tự động dựa trên ngày hiện tại (giả sử lấy từ người dùng dưới dạng "YYYY-MM-DD") và số thứ tự đơn hàng trong ngày (tăng dần). Định dạng mã: `YYYYMMDD-XXX` (XXX là số thứ tự, đủ 3 chữ số).
- **Ví dụ**:
  - **Input**: Ngày `2025-03-18`, thứ tự `5` -> **Output**: `20250318-005`
  - **Input**: Ngày `2025-03-18`, thứ tự `123` -> **Output**: `20250318-123`

---

### **Bài 8: Xử lý dữ liệu phân cấp (Category Tree)**
- **Yêu cầu**: Viết chương trình nhận danh sách danh mục dạng cây (mỗi danh mục có `id`, `name`, `parent_id`). In ra danh sách danh mục theo thứ tự phân cấp (dùng đệ quy hoặc vòng lặp).
- **Ví dụ**:
  - **Input**:
    ```python
    [
      {"id": 1, "name": "Electronics", "parent_id": None},
      {"id": 2, "name": "Laptops", "parent_id": 1},
      {"id": 3, "name": "Accessories", "parent_id": 1}
    ]
    ```
  - **Output**:
    ```text
    Electronics
    - Laptops
    - Accessories
    ```

---

### **Bài 9: Tính toán giá sản phẩm sau giảm giá**
- **Yêu cầu**: Viết chương trình nhận danh sách sản phẩm (`id`, `name`, `price`, `discount_percent`) và áp dụng giảm giá. Nếu `discount_percent` không hợp lệ (âm hoặc > 100), bỏ qua giảm giá. Trả về danh sách sản phẩm với giá mới.
- **Ví dụ**:
  - **Input**: `[ {"id": 1, "name": "Laptop", "price": 1000, "discount_percent": 20}, {"id": 2, "name": "Mouse", "price": 50, "discount_percent": 150} ]`
  - **Output**: `[ {"id": 1, "name": "Laptop", "price": 800}, {"id": 2, "name": "Mouse", "price": 50} ]`

---

### **Bài 10: Đồng bộ dữ liệu giữa 2 nguồn**
- **Yêu cầu**: Viết chương trình so sánh 2 danh sách sản phẩm từ 2 nguồn (list of dictionaries: `id`, `name`, `price`). Tìm các sản phẩm có giá khác nhau giữa 2 nguồn và in ra danh sách các sản phẩm cần cập nhật.
- **Ví dụ**:
  - **Input**:
    ```python
    Nguồn 1: [{"id": 1, "name": "Laptop", "price": 1000}, {"id": 2, "name": "Mouse", "price": 20}]
    Nguồn 2: [{"id": 1, "name": "Laptop", "price": 950}, {"id": 2, "name": "Mouse", "price": 20}]
    ```
  - **Output**: `Sản phẩm cần cập nhật: [{"id": 1, "name": "Laptop", "price": 950}]`
