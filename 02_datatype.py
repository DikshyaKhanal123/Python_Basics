#list
list1 = [10,20,30, 'hello']
print(list1[0])

list1[0] = 100
print (list1[0])

list1.pop(0)#remove value from index 
print(list1)

list1.remove(30)#remove the value 
print(list1)

list1.append(90)#insert value at the end
print(list1)

list1.insert(1,"Ram")# insert value at specific position
print(list1)

#tuple

t = (1,2,3,4)#cannot change the values like list in the tuple

print(type(t))
t1 = (1)# not a tuple it is an integer

t2 = (1,)#tuple.. wtihout comma tuple is not possible
print(type(t1))
print(type(t2))

t3 = (1, 2, 'ram' ,'2') # can store heterogenous data .. also aalow duplicate
print(t3)

#dictionary

student = { 
    "name" : "ram",
    "roll" : 1,
    "address" : "ktm",
    "mobile" : "98666895894"
}
print(student)
student["name"] = "Dikshya" #update dictionary if key found:modify value else insert value
print(student)
print(student["address"]) #print specific value

#print(student["phone"]) #error .. student doesnt conatain key phone

print(student.get("phone", "no value"))  #by default none


# | { #merge two dictionary}
student.pop("name")#delete key and value from dictionary
print(student)

student["name"]="Dikshya"
print(student)

#set

s = {10, 30, 20, "ram"} #does not have index 
print(s)

s1 = {10,10,10,10} #does not allow duplicate
print(s1)

s.add(25)#insert values in set
print(s)

s.remove(25)#remove items from set
print(s)

s= {10, 1, 0, True, False} #0=true and 1=false
print(s)





