class Argument:
    def sum(self, *args): #stored in tuple
        self.result = 0

        for i in args:
            self.result += i


    def func(self, **kwargs): #stored in dictionary
        for key, value in kwargs.items():
            print(f"{key} : {value}")

    def display(self):
        print(f"Sum is: {self.result}")


a = Argument()
a.sum(1,2,3,4,5)
a.display()
a.func(name = "dikshya" , age = 20)