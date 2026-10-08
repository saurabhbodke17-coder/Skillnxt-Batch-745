# how to take input from user in python 
# builtins function is there called input()
# input() will take the string as input 
# it will take everything as string 
# whatever input you are providing to the input function its default datatype will
# be a string only 
# example 

name = input("Enter your name: ")
print(name , type(name)) # Saurabh <class 'str'>

age = input("Enter your age: ")
print(age , type(age)) # 34 <class 'str'>
# because as we saw the rules of list 
# input function will always thake any value as string 

# Enter your age: ["saurabh" , "vishal" , "rahuk"]
# ["saurabh" , "vishal" , "rahuk"] <class 'str'>

# so how to take input in our desired format
# int --> int(input("Enter your age: "))
# float --> float(input("Enter your age: "))


# to take integer as input
# age = int(input("Enter your age: "))
# print(age , type(age)) # 78 <class 'int'>

# Enter your age: 23
# 23 <class 'int'>

# Enter your age: 0
# 0 <class 'int'>


# if you are passing integer inside the int function then only it will work
# else it will giuve error for any other datatype
# Enter your age: 67.45
# ValueError: invalid literal for int() with base 10: '67.45'
# when your passing the string of float as input then only it will fail
# if you pass pure float it will work


# but for floats its diffrent 
# you can pass either int , float any thing 

age = float(input("Enter your age: "))
print(age , type(age))

# Enter your age: 78.555
# 78.555 <class 'float'>

# Enter your age: 90.0
# 90.0 <class 'float'>

# Enter your age: 81
# 81.0 <class 'float'>

# Enter your age: string is passed
# ValueError: could not convert string to float: 'string is passed'

a = 10.55
b = int(a)
print(b) # 10

# again .. if you are passing pure float as input to the int function
# then you will get actual int part of the float 

# how will you take input from user 
# for integer 
age = int(input("Enter your age: "))

# for float
weight = float(input("Enter your weight: "))

# for string 
name = input("Enter your name: ")

# ipop
# Enter your age: 90
# Enter your weight: 23.44
# Enter your name: saurabh

# now what if input datatype is not certain
# user can provide the int , float anything 
# how will we work on this 
# eval type 
# eval will convert the input into the desierd datatype

age = eval(input("Enter your age: "))
print(age , type(age))

# ipop
# Enter your age: 23
# 23 <class 'int'>

# Enter your age: 78.88
# 78.88 <class 'float'>

# eval will convert the data into the its actual datatype
