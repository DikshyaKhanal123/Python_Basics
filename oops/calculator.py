#simple caclulator
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1+self.num2
    
    def sub(self):
        return self.num1-self.num2
    
    def mul(self):
        return self.num1*self.num2
    
    def div(self):
        return self.num1/self.num2

num1 = int(input("enter first number:"))

num2 = int(input("enter second number:"))
c = Calculator(num1, num2)

op = input("enter operation:")

if(op == "+"):
    result = c.add()
elif (op == "-"):
    result = c.sub()
elif (op == "*"):
    result = c.mul()
elif( op == "/"):
    result = c.div()


print("result:",result)
