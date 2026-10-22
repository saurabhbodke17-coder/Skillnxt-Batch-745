# ==============================================================================
# Python Assignment - test29.py
# Topics Covered (Test 16 to Test 26):
#   1. Dictionaries (indexing, .get() method, default values)
#   2. Sets & Frozensets (uniqueness, set(), .add(), frozenset())
#   3. User Input & Type Casting (input(), int(), float(), eval())
#   4. Arithmetic Operators (+, -, *, /, //, %, **) on numbers, strings, lists
#   5. Comparison Operators (>, <, >=, <=, ==, !=)
#   6. Assignment & Compound Operators (=, +=, -=, *=, //=)
#   7. Logical Operators (and, or, not)
#   8. Membership Operators (in, not in)
#   9. Identity Operators (is, is not) & id()
# ==============================================================================


# ------------------------------------------------------------------------------
# Q1. DICTIONARIES: .get() vs Direct Indexing
# ------------------------------------------------------------------------------
# Consider the following dictionary:
car = {
    "brand": "Toyota",
    "model": "Fortuner",
    "year": 2022
}

# (a) Predict the output of:
# print(car["brand"])
# print(car.get("model"))
# print(car.get("color"))
# print(car.get("color", "White"))

# (b) What error will occur if you run: print(car["color"])?

# Write your answers below:
# Ans (a):
# Ans (b):




# ------------------------------------------------------------------------------
# Q2. DICTIONARY LOOKUP (Code Task)
# ------------------------------------------------------------------------------
# 1. Create a dictionary `student` with keys: "name", "roll_no", "course".
# 2. Use the `.get()` method to retrieve the key "grade" with a default value "Not Assigned".
# 3. Print the result.

# Write your code below:




# ------------------------------------------------------------------------------
# Q3. SETS: Uniqueness and .add()
# ------------------------------------------------------------------------------
# (a) You are given a list with duplicate numbers:
numbers = [5, 10, 15, 10, 20, 5, 25, 30, 20]
# How will you convert this list to get only unique numbers as a list?

# (b) Predict the output:
fruits = {"apple", "banana", "mango"}
fruits.add("orange")
fruits.add("apple")
# print(fruits)

# Write your answers below:
# Ans (a):
# Ans (b):




# ------------------------------------------------------------------------------
# Q4. FROZENSET vs SET
# ------------------------------------------------------------------------------
# (a) What is the main difference between a `set` and a `frozenset`?
# (b) Predict the output/error of the following code:

s = frozenset([1, 2, 3, 4])
# s.add(5)
# print(s)

# Write your answer below:
# Ans (a):
# Ans (b):




# ------------------------------------------------------------------------------
# Q5. USER INPUT & TYPE CASTING
# ------------------------------------------------------------------------------
# What will be the output or error for each case?

# Case 1: If user enters 25
# val1 = input("Enter number: ")
# print(type(val1))

# Case 2: If user enters 45
# val2 = int(input("Enter number: "))
# print(val2 * 2)

# Case 3: If user enters 10.5
# val3 = int(input("Enter number: "))
# What happens and why?

# Case 4: If user enters 10.5
# val4 = float(input("Enter number: "))
# print(val4)

# Case 5: If user enters 50
# val5 = eval(input("Enter value: "))
# print(type(val5))

# Write your answers below:
# Ans:
# Case 1:
# Case 2:
# Case 3:
# Case 4:
# Case 5:




# ------------------------------------------------------------------------------
# Q6. SIMPLE USER INPUT PROGRAM (Code Task)
# ------------------------------------------------------------------------------
# Write a simple program that:
# 1. Takes two numbers as input from the user using float(input()).
# 2. Calculates their Addition, Multiplication, and Average.
# 3. Prints all three results.

# Write your code below:




# ------------------------------------------------------------------------------
# Q7. ARITHMETIC OPERATORS
# ------------------------------------------------------------------------------
# Find the output of each expression:
p = 20
q = 6

# print("p + q  =", p + q)
# print("p - q  =", p - q)
# print("p * q  =", p * q)
# print("p / q  =", p / q)      # float division
# print("p // q =", p // q)     # floor division
# print("p % q  =", p % q)      # remainder
# print("p ** 2 =", p ** 2)     # power

# String and List Arithmetic:
# print("Python " * 3)
# print([1, 2] + [3, 4])

# Write your answers below:
# Ans:




# ------------------------------------------------------------------------------
# Q8. COMPARISON OPERATORS
# ------------------------------------------------------------------------------
# Predict whether the output is True or False:
x = 25
y = 40

# print(x > y)
# print(x < y)
# print(x == 25)
# print(x != y)
# print(x >= 25)
# print(y <= 30)

# Write your answers below:
# Ans:




# ------------------------------------------------------------------------------
# Q9. ASSIGNMENT OPERATORS (Tracing)
# ------------------------------------------------------------------------------
# Trace the value of variable `num` after each step:
num = 10
num += 5       # num = ?
num *= 2       # num = ?
num -= 6       # num = ?
num //= 4      # num = ?

# What is the final value of num?
# print("Final num =", num)

# Write your answers below:
# Ans:




# ------------------------------------------------------------------------------
# Q10. LOGICAL OPERATORS (and, or, not)
# ------------------------------------------------------------------------------
# Predict the output (True or False):

# print(True and True)
# print(True and False)
# print(True or False)
# print(False or False)
# print(not True)
# print(not False)

# Compound conditions:
age = 22
has_id = True

# print(age >= 18 and has_id == True)
# print(age < 18 or has_id == False)
# print(not (age >= 18))

# Write your answers below:
# Ans:




# ------------------------------------------------------------------------------
# Q11. MEMBERSHIP OPERATORS (in, not in)
# ------------------------------------------------------------------------------
# Predict the output (True or False):
colors = ["red", "green", "blue", "yellow"]
data = {"name": "Saurabh", "city": "Pune", "age": 28}

# print("green" in colors)
# print("purple" in colors)
# print("black" not in colors)
# print("name" in data)         # Membership in dict checks keys!
# print("Pune" in data)
# print("P" in "Python")

# Write your answers below:
# Ans:




# ------------------------------------------------------------------------------
# Q12. IDENTITY OPERATORS (is, is not) & id()
# ------------------------------------------------------------------------------
# Predict the output and understand the difference between == and is:

a = 100
b = 100
# print(a is b) # 
# print(a == b)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
# print(list1 == list2)        # Checks values
# print(list1 is list2)        # Checks memory address (id)
# print(id(list1) == id(list2))

# Write your answers below:
# Ans:
