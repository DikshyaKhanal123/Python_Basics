class Parent1 :
    def __init__(self):
        self.user = "ram"
        self.roll = 1
    def show(self):
        print(f"name: {self.user}, roll:{self.roll}")
    pass

class Parent2:
    def show_details(self):
        print("this is parent2")


class Child1(Parent1, Parent2):
    pass

class Child2(Parent1, Parent2):
    pass

c1 = Child1()
c1.show()
c1.show_details()


c2 = Child2()
c2.show()
c2.show_details()

