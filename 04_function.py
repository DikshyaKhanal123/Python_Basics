def function_name(c,d): #use snake case to define function name
    print(c,d)

a = 10
b = 20
function_name(10,20)#function call
function_name(a,b) #function call


# name = input("enter your name:")#for input #by default string
# print(name)

# a = int(input("enter any number")) #type casting
# print(a)

# list1 = list(input("enter numbers"))
# print(list1)

#return 
def func1(c,d):
    """ this function add two values""" #for doc string
    sum = c+d
    sub = c-d
    return sum, sub
add, diff = func1(10,20)
result = func1(10,20) # 2 values can store in 1 variable #store as tuple
print(add, diff)
print(result)
print(result[0])

# a,b,c = func1(10,20) error.. 2 value cnnnot store in 3 variables

l1 = [10, 20, 30, 40, 50,31,33,43]
l2 = []
l3 = []

def divisible():

    a = int(input("enter the number to divide: "))
    for i in l1:
        if i%a==0:
            l2.append(i)
        else:
            l3.append(i)
divisible()
print("divisible list:",l2)
print("not divisible list:",l3)
print(f"divisible list: {l2}") #f string 



