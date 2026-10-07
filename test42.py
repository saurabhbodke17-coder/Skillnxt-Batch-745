# find the multiplication for n natural numbers 
# 1*2*3*4*5*6..*10
# Factorial
# 10! = 10*9*8*7*..*2*1

# number = int(input("Enter your number: "))
# prod = 1
# for i in range(1 , number+1):
#     prod = prod * i
# print(prod)


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
    if len(str(number)) < 10:
        print("Number enterd is not 10 digit")
        continue
    contact_book[name] = number
    print()
    print("="*60)

if len(contact_book.items()) ==0:
    print("Nothing in the contact book to print")
else:
    print("Contacts saved sucessfully!")
    for name , number in contact_book.items():
        print(f"Name: {name} ==> Number: {number}")