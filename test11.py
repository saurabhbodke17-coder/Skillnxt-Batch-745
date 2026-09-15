# tuple datatype
# this is the immutable datatype
# once you declare you cant change values inside the tuple 
# but if you have any list inside the tuple that list we can update 
# this is very fast as compared to the list
# as like list you can store any value of any datatype inside tuple 

# tuple will ve declare inside the ()
# there are multiple ways 

t = (1 , 2, 3,4)
print(type(t)) # <class 'tuple'>

t = (1)
print(type(t)) # <class 'int'>
# then how to declare the single value tuple

t = (1,)
print(type(t)) # <class 'tuple'>

# another way of declaring the tuple 
t = 1,2,3,4,5
print(type(t)) # <class 'tuple'>

t = ()
print(type(t)) # <class 'tuple'>
t = tuple()
print(type(t)) # <class 'tuple'>

t = (1,2,3,4)
print(t[2])

t[2] = "updated element"
print(t) # TypeError: 'tuple' object does not support item assignment

l = [1,2,3,4,5]
l[2] = "updated element"
print(l) # [1, 2, 'updated element', 4, 5]

# because tuple is the immutable datatype so you cant change it 
# all indexing , slicing will word same for the tuple as list 
# you can do te nested tuple

t = (1,2,3 ,(3,4,5,6) , 7 , 8)
print(t) # (1, 2, 3, (3, 4, 5, 6), 7, 8)
# this is called as the nested tuple

t = (1,2,3,4,5)
t[0]= 1
print(t) # TypeError: 'tuple' object does not support item assignment


t = (1,2 , [1,2,3,4,5] , 3 , 4)
t[2][0] = "updated element"
print(t) # (1, 2, ['updated element', 2, 3, 4, 5], 3, 4)

# how will we update the tuple if there is any emergency situation
# 1st convert tuple into the list
# 2nd update operation will be done on list
# 3rd again convert it into the tuple
# but this new tuple will be stored inside the new object 

t = (1,2,3,4,5)
print("initita id " , id(t)) # 4351844960
t = list(t)
print("id when tupe converted into list" , id(t)) # 4352277888

t[3] = "updated element"
t = tuple(t) # type casting
print("last id " , id(t)) # 4351850240
print(t)

# tuple is hetrogenous collection of elements so that you can write down any 
# datatype can come inside the tuple -> list , boolean , None , int , string  ,float ,tuple
# datatype can come inside the list -> list , boolean , None , int , string  ,float,tuple
# in next session we are gonna look into the dictionary very important datatype