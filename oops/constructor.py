# class Person:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self): #what to display when object is called
#         return self.name

#     def display(self):
#         print(f"the name of the person is {self.name}")

# name = input("enter name")
# p = Person(name)
# p.display()


class Student:
    def __init__(self, n, a):
        self.name = n
        self.age = a
    def show_details(self, age):
        print(f"name is {self.name}, age is {self.age}")

s = Student( "dikshya" , 20)
s.show_details(20)

