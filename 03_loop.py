#for loop
name = "ram karki"
for i in name : #linear time complexity:O(N)
    print(i)

for index, value in enumerate (name):#to print with index
    print(index, value)

for index, value in enumerate (name, start=10):#to print with index  start from 10
    print(index, value)

# for loop in list
list1 = [1, 2, 3, 10, 30, 31, 35]
odd = []
even = []
for i in list1:
    print(i)

#odd and even list from list1
for i in list1:
    if i % 2 == 0:
        odd.append(i)
    else:
        even.append(i)
print("odd:", odd)
print("even:", even)

#if_else statement
age=70
if (age>18 and age<60):
    print("young")

elif(age>60):
    print("old")

else:
    print("child")

#for loop in dictionary

student = { 
    "name" : "ram",
    "roll" : 1,
    "address" : "ktm",
    "mobile" : "98666895894"
}
for key, value in student.items(): #for both keys and values
    print(key, value)
for key in student.keys(): #only for keys
    print(key)
for value in student.values(): #only for values
    print(value)

for i in student:#access key by default
    print(i)

#for loop in sets
s = {1,2,3,4,5,6}
for i in s:
    print(i)

