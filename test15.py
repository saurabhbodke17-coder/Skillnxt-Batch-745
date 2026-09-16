# set
# unorderd , unique collection of element 
# only unique items will be stored in this datatype
# all duplicates will be droped while assigning the memory

data = {1,2,3,1,2,1,1}
print(data) # {1, 2, 3}

# how to declare empty set
# you can declare only using the set()

data = {}
print(type(data)) # <class 'dict'>

data = set()
print(data , type(data))
#     set()  <class 'set'>