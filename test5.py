# we will store the data in variable 
# variable only contains the reference of object where data is stored 


a = 10 # int datatype
b = 23 # int datatype 
print(a , b)
print(type(a) , type(b)) # to check the datatype we have type function
# what will store inside the int? -> all the natural numbers will be stored as the int including 0
# or all the whole numbers ex -> 23, 45, 76, 1000 



# what about the numbers with decimal ?
# so , numbers with decimal will be stored as the float 
a = 10.67 # float datatype
b = 23.89 # float datatype
print(type(a) , type(b))
# it will store all the decimal numbers in it 



a = 10
b = 10
print(id(a) , id(b))

c = 100000
d = 100000
print(id(c) , id(d))


# boolean datatype
# True , False


a = True
b = False

print(a, type(a))
print(b, type(b))



# if - else , whlie , these all blocks are dependent on boolean values 
# boolean datatype we can achive using the conditions 
print(2>=3)
print(2<=3)
res = 34 <= 78
print(res)
# while dealing witrh block of codes we are gonna use this datratype multiple times 
# my block of code depends on this datatype only 



# use of boolean or how to achive the boolean datatype

age = int(input("Enter your age: "))
if age >= 18:
    print("you are eligible for the licence")
else:
    print("you are not eligible for the licence")



data = ["saurabh" , 23 , 90.66 , [12, 34,45]]
print(data)
print(type(data))

# list is the orderd collection so every element will have the index number in list 
# that index number starts with the 0
# and continue till the n-1 (total number of elements in list -1)
# we can access each element in list using indexing 
# how to do indexing just varname[index number] 

print(data[0])
print(data[2])

# this is how you will do the indexing 
# now what if we provide the index number which is not there/available in the list 
data = [10 , 20 , 30.44 , 60]
print(data[3])
# print(data[4]) # IndexError: list index out of range

# you can also do the negetive indexing 
# how it starts from the -1 and from the rightmost element of the list



data = [10 , 20 , 30.44 , 60]
#       -4   -3     -2    -1
print(data[-1]) # --> 60


class car:
    def __init__(self):
        self.a = 10
        self.b = 20

c = car()
print(c.a)
print(c.b)

# 

class car:
    def __init__(self, a , b):
        self.a = a
        self.b = b
