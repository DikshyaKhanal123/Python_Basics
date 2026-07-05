class Student:

    def __init__(self, name):
        self.name = name
    def user_detail(self):
        print(f"this is user details of  {self.name}")

    def total_marks(self):
        print("this shows the total mark")


s1 = Student("ram")
s1.user_detail()
s1.total_marks()

class Teacher:
    def details(self):
        print("Name: Ram, phone : 2902903")

    def salary(self):
        print("salary:200000")

t = Teacher()
t.details()
t.salary()


class SubNumber:
    def add(self,a, b):
        return a-b;

    def __init__(self): #constructor
        print("this is constructor")
ob = SubNumber()
print(ob.add(5,6))