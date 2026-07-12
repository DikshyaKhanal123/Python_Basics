class Parent1 :
    def __init__(self):
        self.user = "ram"
        self.roll = 1
    def show(self):
        print(f"name: {self.user}, roll:{self.roll}")
    pass

class Child1(Parent1):
    pass
       
class Child2(Parent1):
    pass

c1 = Child1()
c1.show()

c2 = Child2()
c2.show()

