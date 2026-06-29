def func(name, age):
    print(f"name is : {name}")
    print(f"age is :{age}")

name ="ram"
age = 20
func(name,age)
func(age,name)
func(age=age, name=name) #match the variable parameter and the variable of argument : name must be same to pass value like this
func(age = 10, name = "hari")


def func(a,b,c=20): #defult value must be in last position
    #def func(a=20,b,c) gives error
    print(f"a = {a}, b = {b}, c = {c}")
func(1, 2, 3)
func(1, 2)

from test import func1
add, diff = func1(10,20)
print(add, diff)


