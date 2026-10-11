# Functions 
# datatypes 
# conditional statments 
# loops 
# functions 

# now what loops were doing 
# so loops were removing the job of continous or repetive tasks 
# to print 1 to 100 loop will do the task efficently 

# now sometime 1 functionality you will need to use at multiple places 
# that bloc of code rather writing everytime there we will create the functions 

# i am creating the webside 
# no every new page it will greet you
# for this reason i will create the simple function of greeting and i will call that 
# function whenever i want to greet 

# we declare the function with def keyword

# def functionname(parameter):
#     print(f"Good morning {parameter}")

# functionname("Saurabh")
# functionname("vishal")

# i wanrt to check whether the given number is prime or not 
def isprimeornot(n):
    for i in range(2 , n):
        if n % i == 0:
            print("Not Prime Number")
            break
    else:
        print("This is the prime number")

isprimeornot(91)
# Not Prime Number

isprimeornot(13)
# This is the prime number


