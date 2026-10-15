# identity operator
# it will check that whether the given variable reffering to the another variable 
# this will check the memory location of objects 
a = 10
b = 10

print(id(a))
print(id(b))
# 4351766784
# 4351766784

print(a is b)

c = [1,2,3,4]
d = [3,4,5,6]
print(id(c))
print(id(d))

# 4375238848
# 4375399424
print(c is d) # False

# logical statments 
# loops 