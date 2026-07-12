class Parent1 :
    def __init__(self):
        self.user = "ram"
        self.roll = 1
    def show(self):
        print(f"name: {self.user}, roll:{self.roll}")
    pass

class Parent2(Parent1):
    def show_details(self):
        print("this is parent2")


class Child(Parent2):
    pass

c = Child()
c.show()
c.show_details()

