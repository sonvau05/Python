from datetime import datetime
import matplotlib.pyplot as plt

class Person:
    def __init__(self, firstname, middlename, lastname, birthday, address, phone):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = datetime.strptime(birthday, "%d/%m/%Y")
        self.address = address
        self.phone = phone

    def get_age(self):
        today = datetime.now()
        return today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))

class Student(Person):
    def __init__(self, firstname, middlename, lastname, birthday, address, phone, regno, gpa):
        super().__init__(firstname, middlename, lastname, birthday, address, phone)
        self.regno = regno
        self.gpa = float(gpa)

    def __str__(self):
        return f"{self.firstname} {self.middlename} {self.lastname}, Reg: {self.regno}, GPA: {self.gpa}, Age: {self.get_age()}"

students = [
    Student("Nguyen", "Van", "An", "15/03/2000", "Hanoi", "0901234567", "SV001", 8.5),
    Student("Tran", "Thi", "Binh", "22/07/2002", "HCMC", "0912345678", "SV002", 7.8),
    Student("Le", "Hoang", "Cuong", "10/11/1998", "Da Nang", "0923456789", "SV003", 9.0),
    Student("Pham", "Ngoc", "Diep", "05/05/2003", "Hue", "0934567890", "SV004", 6.5),
    Student("Ho", "Thi", "Mai", "12/12/2004", "Can Tho", "0945678901", "SV005", 8.2)
]

def add_student():
    firstname = input("First name: ")
    middlename = input("Middle name: ")
    lastname = input("Last name: ")
    birthday = input("Birthday (dd/mm/yyyy): ")
    address = input("Address: ")
    phone = input("Phone: ")
    regno = input("Register number: ")
    gpa = input("GPA: ")
    students.append(Student(firstname, middlename, lastname, birthday, address, phone, regno, gpa))
    print("Student added!")

def show_students():
    if not students:
        print("No students!")
    else:
        for student in students:
            print(student)

def filter_students_age():
    filtered = [s for s in students if s.get_age() > 22]
    if not filtered:
        print("No students over 22!")
    else:
        for student in filtered:
            print(student)

def filter_students_gpa_age():
    filtered = [s for s in students if 8.0 <= s.gpa <= 10.0 and s.get_age() < 22]
    if not filtered:
        print("No students with GPA 8.0-10.0 and under 22!")
    else:
        for student in filtered:
            print(student)

def save_to_file():
    with open('students.txt', 'w') as f:
        for s in students:
            f.write(f"{s.firstname},{s.middlename},{s.lastname},{s.birthday.strftime('%d/%m/%Y')},{s.address},{s.phone},{s.regno},{s.gpa}\n")
    print("Saved to students.txt")

def plot_gpa():
    if not students:
        print("No students to plot!")
        return
    names = [f"{s.firstname} {s.lastname}" for s in students]
    gpas = [s.gpa for s in students]
    plt.bar(names, gpas)
    plt.xlabel("Students")
    plt.ylabel("GPA")
    plt.title("Student GPA Chart")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n1. Add student\n2. Show students\n3. Filter students (>22 years)\n4. Filter students (GPA 8.0-10.0, <22 years)\n5. Save to file\n6. Plot GPA chart\n7. Exit")
        choice = input("Choose (1-7): ")
        if choice == '1':
            add_student()
        elif choice == '2':
            show_students()
        elif choice == '3':
            filter_students_age()
        elif choice == '4':
            filter_students_gpa_age()
        elif choice == '5':
            save_to_file()
        elif choice == '6':
            plot_gpa()
        elif choice == '7':
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    menu()