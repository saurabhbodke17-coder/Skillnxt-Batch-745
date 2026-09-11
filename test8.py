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


l = [1,2,3,4,5]
l.remove(2) # remove the element 2 from the list 
print(l)
