# for loop 
# how to start for loop
# syntax of for loop 

# how to print tables using the for loop
# it workd on the sequences or collections
# itrerarted it over the list , tuple , dict , set , string
# use of break statment 

# to break the for loop break statment 

# i want to print the table of any number upto the 15th multiplier 
# range function 
# which will provide memoronly to start , stop , step 
# it will not create the sequence but if you want to creat that sequence 
# then you have to use the typecasting functions

# list , tuple , set
# 1 * 15 = 15
# 2 * 15 = 30


num = int(input("Enter the number: "))
nultiplier = int(input("Upto What multiplier "))
for i in range(1 , nultiplier + 1):
    print(f"{num} * {i} = {i * num}")


# there is a app who will ask you for multiplier 
# if multiplier is upto 20 then it will print the table 
# if greater than 20 then it will print max upto 20 only and break the code inside the for loop

num = int(input("Enter the number: "))
nultiplier = int(input("Upto What multiplier "))
for i in range(1 , nultiplier + 1):
    if i <=20:
        print(f"{num} * {i} = {i * num}")
    else:
        print("We have printed your table upto 20 we are stopping here")
        break


# will ask user how many contacts he want to store in the phone 
# and then ask him to save name and number in phone 
# whatever contacts i have saved print them on terminal as name ==> number
# name : number

contact_book = {}
number = int(input("How many contacts do you want to save in mobile: "))
if number == 0: # 10
    print("No contact added")
for i in range(1 , number + 1):
    name = input("Enter your name: ")
    number = int(input("Enter your number: "))
    contact_book[name] = number
    print()
    print("="*60)
print("Contacts saved sucessfully!")

for name , number in contact_book.items():
    print(f"Name: {name} ==> Number: {number}")

# to iterate the dictionary we should have the dict.items method
# it wil convert the dict into list of tuples 

data = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

d =  data.items()
print(d)
for i in [('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)]:
    print(i)

# ('brand', 'Ford')
# ('model', 'Mustang')
# ('year', 1964)

# t , v = ('brand', 'Ford')
# print(t)
# print(v)


contact_book = {}
number = int(input("How many contacts do you want to save in mobile: "))
if number == 0: # 10
    print("No contact added")
for i in range(1 , number + 1):
    name = input("Enter your name: ")
    if name in contact_book.keys():
        print("Name alredy Exist")
        continue
    number = int(input("Enter your number: "))
    contact_book[name] = number
    print()
    print("="*60)
print("Contacts saved sucessfully!")

for name , number in contact_book.items():
    print(f"Name: {name} ==> Number: {number}")


# for i in range(1 , 11): # 4 , 5
#     if i == 3 or i == 5:
#         continue
#     print(i)


# i want to print the sum of n natural numbers asked by the user 
sum = 0
n = int(input("Upto what number you want the sum: "))
for i in range(1 , n+1):
    sum = sum + i
    print("Current sum is: ",sum)
print(sum)

# find the multiplication for n natural numbers 
# 1*2*3*4*5*6..*10