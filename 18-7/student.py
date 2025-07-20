class Student:
    def __init__(self, id, firstname, middlename, lastname, birthday):
        self.id = id
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthday = birthday
    
    def displayinfo(self):
        print(f"ID: {self.id}")
        print(f"Full name: {self.firstname} {self.middlename} {self.lastname}")
        print(f"Birthday: {self.birthday}")

student1 = Student("001", "Nguyen", "Van", "An", "2000-05-15")
student1.displayinfo()