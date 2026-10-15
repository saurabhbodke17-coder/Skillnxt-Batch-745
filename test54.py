from arithmetics import multiply
res = multiply.multiply_2_numbers(20 , 30)
print(res)
# 600


from arithmetics.multiply import multiply_3_numbers
res = multiply_3_numbers(20 , 30 , 40)
print(res)
# 24000


from arithmetics.multiply import multiply_2_numbers
res = multiply_2_numbers(23 , 45)
print(res)
# 1035

# why the modules are used 
# they are used for the modularity and cleanness of program 
# if you want to update then its very eassy to track the updates 

# python 3.6 before 
# it was must to keep the __init__ file in your module 
# then only your python use to recogmnise it as a module 
