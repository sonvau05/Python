products = []

def add_product():
    id = input("Nhập ID sản phẩm: ")
    name = input("Nhập tên sản phẩm: ")
    price = float(input("Nhập giá sản phẩm: "))
    source = input("Nhập nguồn gốc sản phẩm: ")
    products.append({"id": id, "name": name, "price": price, "source": source})
    print("Thêm sản phẩm thành công!")

def display_products():
    if not products:
        print("Danh sách sản phẩm rỗng!")
    else:
        for p in products:
            print(f"ID: {p['id']}, Tên: {p['name']}, Giá: {p['price']}, Nguồn: {p['source']}")

def filter_products_by_price():
    max_price = float(input("Nhập giá tối đa để lọc: "))
    filtered = [p for p in products if p['price'] < max_price]
    if not filtered:
        print("Không có sản phẩm nào phù hợp!")
    else:
        for p in filtered:
            print(f"ID: {p['id']}, Tên: {p['name']}, Giá: {p['price']}, Nguồn: {p['source']}")

def update_product():
    id = input("Nhập ID sản phẩm cần cập nhật: ")
    for p in products:
        if p['id'] == id:
            p['name'] = input("Nhập tên mới: ")
            p['price'] = float(input("Nhập giá mới: "))
            p['source'] = input("Nhập nguồn gốc mới: ")
            print("Cập nhật thành công!")
            return
    print("Không tìm thấy sản phẩm với ID này!")

def delete_product():
    id = input("Nhập ID sản phẩm cần xóa: ")
    for i, p in enumerate(products):
        if p['id'] == id:
            products.pop(i)
            print("Xóa sản phẩm thành công!")
            return
    print("Không tìm thấy sản phẩm với ID này!")

while True:
    print("\n=== MENU QUẢN LÝ SẢN PHẨM ===")
    print("1. Thêm sản phẩm")
    print("2. Hiển thị danh sách sản phẩm")
    print("3. Lọc sản phẩm theo giá")
    print("4. Cập nhật sản phẩm")
    print("5. Xóa sản phẩm")
    print("6. Thoát")
    
    choice = input("Chọn chức năng (1-6): ")
    
    if choice == "1":
        add_product()
    elif choice == "2":
        display_products()
    elif choice == "3":
        filter_products_by_price()
    elif choice == "4":
        update_product()
    elif choice == "5":
        delete_product()
    elif choice == "6":
        print("Thoát chương trình!")
        break
    else:
        print("Lựa chọn không hợp lệ! Vui lòng chọn lại.")