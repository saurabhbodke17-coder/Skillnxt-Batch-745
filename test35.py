# loops 
# what is loops 
# print hello world for 20 times 

# for i in range(1 , 100000000):
#     print(f"Hello world {i}")

# for loop will iterate over the sequences
# for an example 

# l = [1,2,3,4,5,6,7]
# for i in l:
#     print(i)
# print("Loop execution is done: ")

# nested if else
# if after satisfying 1 condition if we have any other 
# condition as well
# that we can write inside the nested if else loop 

age = eval(input("Enter your age ")) 
# do you have pancard --> yes -->licence
if age >= 18:
    pancard = input("Do you have pancard ")
    if pancard.lower() == "yes":
        print("Allowed")
    else:
        print("Please get Pancard First")
else:
    print("Your age is not greater than equal to 18")

# Enter your age 34
# Do you have pancard yes
# Allowed

# Enter your age 12
# Your age is not greater than equal to 18