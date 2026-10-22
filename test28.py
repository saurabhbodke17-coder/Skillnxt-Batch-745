# # Type casting 
# # what is the type casting 
# # converting the one datatype into another datatype 


# # # int to float
# # a = 10
# # b = float(a)
# # print(a , type(a)) # 10 <class 'int'>
# # print(b , type(b)) # 10.0 <class 'float'>

# # int to str
# a = 10
# b = str(a)
# print(a , type(a)) # 10 <class 'int'>
# print(b , type(b)) # 10 <class 'str'>

# # int to boolean
# # True , False
# # anything other than 0 will be true and only 0 will be false 
# # whenever you are converting any number to boolean

# a = 10
# print(bool(a)) # True

# b = 0
# print(bool(b)) # False

# c = 0.00000
# print(bool(c)) # False

# c = 0.00001
# print(bool(c)) # True

# d = -1
# print(bool(d)) # True

# # whenever you are gonna conver the int into the list 
# # you will get the erro
# # int is not iterable 
# # premative can be converted into premetive 
# # and non premetive can be converted into non premetive 

# a = 10
# print(list(a))
# # TypeError: 'int' object is not iterable (this part will see in loops)


# # converting float into other datatypes
# a = 10.89
# print(int(a)) # 10
# print(str(a)) # "10"
# print(bool(a))# True
# print(list(a)) # error TypeError: 'float' object is not iterable

# str - > other datatypes

# a = "abc"
# print(int(a)) # ValueError: invalid literal for int() with base 10: 'abc'

# a = "10"
# b = int(10)
# print(b , type(b)) # 10 <class 'int'>

# c = "10.78"
# # print(int(c)) # ValueError: invalid literal for int() with base 10: '10.78'
# d = float(c)
# print(d , type(d)) # 10.78 <class 'float'>
# # int is premetive datatype you cant convert it into collection

# a = 10 
# b = []
# b.append(a)
# print(b) # [10]

# s = "hello world"
# # boolean
# print(bool(s)) # True

# s = ""
# print(bool(s)) # False

# s = "hello world"
# print(list(s))
# # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
# print(tuple(s))
# # ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')

# a = True
# b = False
# print(int(a)) # 1
# print(int(b)) # 0
# print(str(a)) # "True"
# print(list(a)) # TypeError: 'bool' object is not iterable
# print(tuple(a)) # TypeError: 'bool' object is not iterable

# how can we convert the int , float , bool , str into other datatypes 

# # List to other datatypes 
# l = [1,2,3,4,5,5,3,4,2,1]
# # print(int(l))
# # TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
# # same error for float as well

# print(bool(l)) # True
# print(tuple(l)) # (1, 2, 3, 4, 5)
# print(set(l)) # {1, 2, 3, 4, 5} -> output will contain only unique values 
# # print(dict(l)) # TypeError: object is not iterable

# l = [[1 ,2 ] , [3,4] , [5,6]]
# print(dict(l)) # {1: 2, 3: 4, 5: 6}
# # to convert the list into dict your list should be list of key and value 

# tuple
# everything same as the list 


# # dictionary
# d = {"name":"saurabh" , "age":30 , "gender":"male"}
# print(list(d)) # ['name', 'age', 'gender']
# print(tuple(d)) # ('name', 'age', 'gender')
# # how can i convert the dictionary into list of tuples 
# print(d.items()) # dict_items([('name', 'saurabh'), ('age', 30), ('gender', 'male')])

# set 
# how to work with set
s = {"saurabh" , "raj" , "vishal" , "nitin"}
print(list(s)) # ['raj', 'saurabh', 'vishal', 'nitin'] hash value 

name= "saurabh"
print(hash(name)) # 5896597877236817518
print(tuple(s)) # ('nitin', 'raj', 'saurabh', 'vishal')
