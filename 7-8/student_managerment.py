import matplotlib.pyplot as plt

class Student:
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa

students = []

def add_student():
    try:
        id = input("Nhập ID sinh viên: ")
        if any(s.id == id for s in students):
            print("ID đã tồn tại!")
            return
        name = input("Nhập tên sinh viên: ")
        gpa = float(input("Nhập GPA (0-10): "))
        if not 0 <= gpa <= 10:
            print("GPA phải từ 0 đến 10!")
            return
        students.append(Student(id, name, gpa))
        print("Thêm sinh viên thành công!")
    except ValueError:
        print("Lỗi: GPA phải là số!")
    except Exception as e:
        print(f"Lỗi: {e}")

def display_all_students():
    if not students:
        print("Chưa có sinh viên nào!")
        return
    for s in students:
        print(f"ID: {s.id}, Tên: {s.name}, GPA: {s.gpa}")

def display_good_students():
    good_students = [s for s in students if s.gpa >= 8]
    if not good_students:
        print("Không có sinh viên nào có GPA >= 8!")
        return
    for s in good_students:
        print(f"ID: {s.id}, Tên: {s.name}, GPA: {s.gpa}")

def save_to_file():
    try:
        with open("students.txt", "w", encoding="utf-8") as f:
            for s in students:
                f.write(f"{s.id},{s.name},{s.gpa}\n")
        print("Lưu file thành công!")
    except Exception as e:
        print(f"Lỗi khi lưu file: {e}")

def view_student_by_id():
    try:
        id = input("Nhập ID sinh viên: ")
        for s in students:
            if s.id == id:
                print(f"ID: {s.id}, Tên: {s.name}, GPA: {s.gpa}")
                return
        print("Không tìm thấy sinh viên với ID này!")
    except Exception as e:
        print(f"Lỗi: {e}")

def plot_gpa_chart():
    if not students:
        print("Chưa có dữ liệu để vẽ biểu đồ!")
        return
    try:
        names = [s.name for s in students]
        gpas = [s.gpa for s in students]
        plt.bar(names, gpas)
        plt.xlabel("Tên sinh viên")
        plt.ylabel("GPA")
        plt.title("Biểu đồ GPA của sinh viên")
        plt.show()
    except Exception as e:
        print(f"Lỗi khi vẽ biểu đồ: {e}")

def main():
    menu = [
        ("1", "Thêm sinh viên"),
        ("2", "Hiển thị tất cả sinh viên"),
        ("3", "Hiển thị sinh viên giỏi GPA >=8"),
        ("4", "Lưu ra file"),
        ("5", "Xem thông tin sinh viên theo ID"),
        ("6", "Vẽ biểu đồ GPA"),
        ("7", "Thoát chương trình")
    ]
    
    while True:
        print("\n=== MENU QUẢN LÝ SINH VIÊN ===")
        for option, description in menu:
            print(f"{option}. {description}")
        
        choice = input("Chọn chức năng (1-7): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            display_good_students()
        elif choice == "4":
            save_to_file()
        elif choice == "5":
            view_student_by_id()
        elif choice == "6":
            plot_gpa_chart()
        elif choice == "7":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1-7.")

if __name__ == "__main__":
    main()