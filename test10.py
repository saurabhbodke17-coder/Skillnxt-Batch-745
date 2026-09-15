# how to update any element in list
# l = [1,2,3,4,5]
# i want to update the 3 with 9
# l[2] = 9
# print(l) # [1, 2, 9, 4, 5]

# l = ["vishal" , "rahul" , "raj" , "alex"]
# l[1] = "saurabh"
# print(l) # ['vishal', 'saurabh', 'raj', 'alex']

# you can do this in list because list is mutable 
# but you cant do it in the string or tuple who are immutable 

# s = "saurabh"
# s[6] = "b" # TypeError: 'str' object does not support item assignment
# print(s)
# as the string is immutable you cant change the string by using the index as we 
# were doing in list

# if you want to merge two strings there you can use + operator

# s1 = "hello"
# s2 = "world"
# s3 = s1 + s2
# print(s3) # helloworld

# s1 = "hello"
# s2 = "world"
# s3 = s1 + " " + s2 # hello world
# print(s3)

# s1 = "hello"
# s2 = " world"
# s3 = s1 + s2 # hello world
# print(s3)

# s1 = "hello "
# s2 = "world"
# s3 = s1 + s2 # hello world
# print(s3)

# string methods 
# if you want to declare empty string how will you declare ?
# two ways are there 

# a = ""
# b = str()
# print(a , len(a))
# print(b , len(b))

# to convert other datatypes into string we use the str() function
# will see this in more depth when will see typecastig

# greet = "hello world"
# print(id(greet)) # 4304413872
# greet = greet.upper()
# print(greet) # HELLO WORLD
# print(id(greet)) # 4304415152


greet = "hello world"
greet = greet.title() 
print(greet) # Hello World

greet = "heLlo WoRlD"
greet = greet.lower()
print(greet) # hello world

# LOWER Method is the one whoch we are gonna use in most of the cases 
# it will be used in string matching 
# if user_input.lower() == "matching string"
# here in this use case this lower will convert the string into the lower case 
# user_input input given by user 
# will take input from user by using the input() function
# this will see once the datatype is completed
# there is no nested string 
# you cant declare the nested string 