#  strings

greet = 'hello world'

# i can write down the string both using the single double and triple quotes 
# when to use which one 
# whenever you will have to use the single line string that time you can use the single or double quores string 
# when you wan to write the multiline string that time you can use triple quotes

# ex. 
greet = "hellow world how are you"
msg = 'good afternoon'
mail = """ 
Dear sir,

How are you i hope you are doing good
it was really nice to meet you see you soon 
best regards,
Saurabh
"""
print(greet)
print()
print(msg)
print()
print(mail)

# list is immutable in the nature 
# you cannot change the string once its declared 

# some methods about the string 
data = "hello world"
new_data = data.upper()

print(data)
print(new_data)

txt = "Company12"
x = txt.isalnum()
print(x)

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)

a = "hello how are you"
del a
print(a) #NameError: name 'a' is not defined

l = [1,2,3,4,5]
del l
print(l) # NameError: name 'l' is not defined

# above errors you are getting because del will delete the object from your memory 
# whose address that variable was storing


# Assignment Questions for next 2 days --> solve and upload on group upto Sunday evening 13 sep 2026
# Q1. STRING INDEXING

s = "MachineLearning"

# Find the output:

print(s[s[2]])

# Also explain why this works or gives an error.


# Q2. LIST INDEXING

numbers = [10, 20, [30, 40, [50, 60]], 70, 80]

# Find the output:

print(numbers[2][2][0])
print(numbers[-3][1])
print(numbers[2][-1][-2])


# Q3. LIST SLICING

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Find the output:

print(lst[8:2:-2])
print(lst[-1:-9:-3])
print(lst[2:8:-1])
print(lst[-3:3:-2])

