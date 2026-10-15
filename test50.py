# return .

# without return 
# def greet(name):
#     print( f"Good morning {name}")

# res = greet("Saurabh")
# print(res)

# Good morning Saurabh
# None


# without return 
# def greet(name):
#     return f"Good morning {name}"

# res = greet("Saurabh")
# print(res)

# Good morning Saurabh

# def payload(key , value):
#     res = {key:value}
#     return res

# res = payload("Saurabh" , "AI Engineer")
# print(res)
# {'Saurabh': 'AI Engineer'}

# function with default arguments 
# if you didnt pass any value in function it will take default values 

def greet(name = "User" , timing = "Morning"):
    return f"Hey {name} good {timing}"
    print("hello")

res = greet()
print(res)
# Hey User good Morning

res = greet("Vishal" , "Afternoon")
print(res)
# Hey Vishal good Afternoon

# posirion of the arguments is very imporant

res = greet("Afternoon" , "Vishal" )
print(res)
# Hey Afternoon good Vishal

res = greet(timing = "Afternoon",name = "Vishal")
print(res)
# Hey Vishal good Afternoon

a = 10 , 20
print(a)
# (10, 20)


