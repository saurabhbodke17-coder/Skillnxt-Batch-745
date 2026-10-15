# if conditional statment
"""
if condition:
    print("hello")
"""

# Example 1
# i want to check that whether the given number if positive or not 
# if your number is >0 it means its positive 

# number = int(input("Enter the number: "))
# if number>0:
#     print("Number is positive")
#     print(f"you have provided {number} as input")
# Enter the number: 34
# Number is positive
# you have provided 34 as input


# Example 2
# i want to check whether the user is eligible for viting or not
# for voting age should be greater than or equal to 18 years 

# age = int(input("Enter the age: "))
# if age >= 18:
#     print("You are eligible")
#     print(f"your provided age is {age}")
# Enter the age: 23
# You are eligible
# your provided age is 23


age = int(input("Enter the age: "))
if age >= 18:
    print("You are eligible")
    print(f"your provided age is {age}")
    
print("above block of code execution is done ")
print("now you are outside the block of code ")
# Enter the age: 45
# You are eligible
# your provided age is 45
# above block of code execution is done 
# now you are outside the block of code 



age = int(input("Enter the age: "))
if age >= 18:
    print("You are eligible")
    print(f"your provided age is {age}")
    
print("above block of code execution is done ")
print("now you are outside the block of code ")
# Enter the age: 11
# above block of code execution is done 
# now you are outside the block of code 