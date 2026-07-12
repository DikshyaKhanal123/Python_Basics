class Employee :

    def __init__(self):
        self.user = "ram"
        self.address = "kathmandu"

    def show_details(self):
        print("this is parent method")
    pass

class Developer (Employee):
    # def __init__(self):
    #     self.roll = 101

    
    def show_details(self): #method overriding
        print("this is child method")
    pass



d1 = Developer()
print(d1.user) #if there is constructor or method in child class then the object donot go to parent class
d1.show_details()

