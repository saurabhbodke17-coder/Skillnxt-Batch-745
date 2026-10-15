print("The print is imported")

from test5 import car
innova = car(20 , 20)
print(innova.a)
print(innova.b)


L = [1,2,3,4,5,6]
print("length of L is: ",len(L))

# out of 5 
marks = [2 , 3, 4 , 4 ,3 ,2]
print(marks)
print("memory location of list is: ",id(marks))

# nested lists 
# list inside the list

l = [1 , 2, [3 , 4, 5, 6, 7] , 8 , 9]
# print(l[5])
print(l[2][1])
print(l[2][3])

print(id(l))

# 2L = [1,2,3,4]
# print(2L) --> invalid list name 

# store it in same list 
l = ["saurabh" , "kruthika" , 90.66 , 23 , True , False , None]
print(l)
print(id(l))

data = ["saurabh" , "bahubali" , 23 , 56, [12 , 34, 45,["parth" , 78 , 34.67] , 89,99], 87,34]
name = data[4][3][0]
print(name)
print(data[4][4])

# if you want to declare the empty list 
# how will you declare ?
l1 = [] # --> 1st method
l2 = list() # --> empty list

print("Type of both lists avove is List")
print(type(l1) , type(l2))

"""
you can use this list() function to create empty list 
also to convert other sequence into list we can use the list function
string to list , tuple to list 
"""

s = "saurabh"
t = (1,2,3,4,5)
print(t)

converted_list = list(s)
converted_tuple = list(t)
print(converted_list)
print(converted_tuple)

import pandas as pd
d = {"name":["saurabh" , "vishal" , "rahul"] , "marks":[100 , 35 , 12]}
df = pd.DataFrame(d)
df.to_excel("students_data.xlsx")


data = ["saurabh" , "bahubali" , 23 , 56, [12 , 34, 45,["parth" , 78 , 34.67] , 89,99], 87,34]
res = data[4][-3][-2]
print(res)
res = data[-3][-3][-1]
print(res)
res = data[-3][-3][2]
print(res)

l = []
print(l[0]) #IndexError: list index out of range