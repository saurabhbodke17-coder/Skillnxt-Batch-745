# set 
# what is set ?
# set is unique collection of elements
# this is unorderd collection
# values are orderd as per their hash value 

s = {1,2,3,1,2,3,4,5,4,5,3}
print(s) # {1, 2, 3, 4, 5}

l = [1,2,3,1,2,2,1,3,4,4,5,3,4,5]
# i want to find the unique elements from the list 
new_list = list(set(l))
print(new_list) # [1, 2, 3, 4, 5]


# add method adds the elements inside the set 
fruits = {"apple", "banana", "cherry"}
fruits.add("orange") # {'banana', 'cherry', 'apple', 'orange'}
print(fruits)

# set is also mutable bacause you can perfoem the changes in same object 
# frozenset
# frozenset is not mutable 
# you can not add or remove or update element in frozenset 

# how to declare the frozenset 
s = {1,2,3,4,2,3,1}
s = frozenset(s)
print(s)
print(type(s)) # <class 'frozenset'>
s.add(23)
print(s) # AttributeError: 'frozenset' object has no attribute 'add'
# you cant update the frozenset once the decleration happen 
# inside same object 