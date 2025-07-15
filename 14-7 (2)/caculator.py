try:
    a = float(input("Số thứ nhất: "))
    b = float(input("Số thứ hai: "))
    op = input("Phép toán (+,-,*,/): ")
    match op:
        case "+": print(f"{a}+{b}={a+b}")
        case "-": print(f"{a}-{b}={a-b}")
        case "*": print(f"{a}*{b}={a*b}")
        case "/": print(f"{a}/{b}={a/b}" if b != 0 else "Lỗi: Chia cho 0!")
        case _: print("Phép toán không hợp lệ!")
except:
    print("Vui lòng nhập số hợp lệ!")