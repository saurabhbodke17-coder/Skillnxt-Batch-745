# for else loop 
# when inside the for loop we use break that 
# time generally this loop comes into picture 
# if break execute then your else part will not execute 
# if break doesnot execute then else part will execute 

# check whether the given number is prime or not ?
# either can divided by 1 , and number itself not any other number
# if any other number divides that number then its not prime number 

# 44 
n = int(input("Enter the number: "))
for i in range(2 , n):
    if n % i == 0:
        print("Not Prime Number")
        break
else:
    print("This is the prime number")

# Enter the number: 13
# This is the prime number

# Enter the number: 80
# Not Prime Number


names = ["rahul" , "aniket" , "roshan"]
for i in names:
    if i == "vishal":
        print("Vishal Found in list")
        break
else:
    print("Vishal not Found")

