def func1(c,d):
    """ this function add two values""" #for doc string
    sum = c+d
    sub = c-d
    return sum, sub

a = int(input("enter first number:"))
b = int(input("enter second number:"))

op = input("enter operator that you want to perform")

def operation (a,b):
    if(op == "+"):
        return a+b
    elif (op == "-"):
        return a-b
    elif (op == "*"):
        return a*b
    elif (op == "/"):
        return a/b
    else:
        print("invalid operator")

result = operation
print(result(a,b))