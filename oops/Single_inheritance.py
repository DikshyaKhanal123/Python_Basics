class Parent:
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")


class Child(Parent):
    pass


name = input("Enter name: ")
roll = input("Enter roll: ")

c = Child(name, roll)
c.show_details()
