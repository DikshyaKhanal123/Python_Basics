class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self): #what to display when object is called
        return self.name

    def display(self):
        print(f"the name of the person is {self.name}")

name = input("enter name")
p = Person(name)
p.display()
