# l = [1,2,3,4,5,6]
# res = l[1:4:1]
# print(res)

# res1 = l[0:5:2]
# print(res1)

# res2 = l[3:6]
# print(res2)

# res = l[1:6:2]
# print(res)

# l = ["vishal" , 23 , 56 , "raj" , 90,True, "Saurabh"]
# res = l[2:6]
# print(res)

# ress = l[0:7:2]
# resm = l[0:7:3]

# print(ress)
# print(resm)


# l = ["vishal" , 23 , 56 , "raj" , 90,True, "Saurabh"]
# print(l[-4:0:1])
# print(l[-4:-8:-1])

# print(l[0:])
# print(l[:4])
# print(l[-1:-5:-1])
# print(l[6:2:-1])

# done with slicing part ..
# go for the methods 
# methods are the functions of the datatype which 
# allow to do some operations on it 


data = [1,2,3,4,5]
print(data)
print(id(data)) # --> 4330690688

# to add element inside the list
data.append("last element")
print(data)
print(id(data)) # --> 4330690688


# This method is used to insert the element at specific index location
data = [1,2,3,4,5]
data.insert(4 , "inserted element")
print(data)

data.insert(0,"At O Index number")
print(data)

data.clear()
print(data)

l = [2,4,1,8,5,6,9,5,5,5,5,5,11,3]
l.sort()
print(l)

res = l.count(5)
print(res) 

# Example TO SOLVE AT HOME 

data = [10 , 20 , 30, [10 , 20 , "vishal" , "raj" , [10 , 30 ,60 , 90] , 80 , 100] , 234 , 567]


# ===================================================================================
# NOW BY USING SLICING OR INDEXING YOU NEED TO SOLVE THIS EXAMPLE

# --> [80 , 100]
# --> [10 , 60] 
# --> [20 , "raj" , 80]
# print entire list in reverse order 


print(data[3][5:7])
print(data[3][4][0:3:2])
print(data[3][1:6:2])