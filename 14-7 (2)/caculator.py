try:
    a = float(input("Nhập số thứ nhất: "))
    b = float(input("Nhập số thứ hai: "))
    op = input("Nhập phép toán (+, -, *, /): ").strip()
    match op:
        case "+": print(f"{a} + {b} = {a + b}")
        case "-": print(f"{a} - {b} = {a - b}")
        case "*": print(f"{a} * {b} = {a * b}")
        case "/":
            if b != 0:
                print(f"{a} / {b} = {a / b}")
            else:
                print("Lỗi: Không chia được cho 0!")
        case _: print("Lỗi: Phép toán không hợp lệ!")
except ValueError:
    print("Lỗi: Vui lòng nhập số hợp lệ!")