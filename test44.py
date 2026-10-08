# break statment 
# what is the break statment -> you know that 
# to break the loops we use break statnents 
# what generally the break statment do 
# it breaks the current loop
# inner loops break will break inner loop and 
# outer one will break outer loop

for i in range(1 , 11):
    for j in range(1 , 20):
        if j == 5:
            print(f"{i} 5 breaking the inner loop")
            break
        else:
            print(i ,j , sep = " ")
    print("Interpritor saw the outer break")
    break

# 1 1
# 1 2
# 1 3
# 1 4
# 1 5 breaking the inner loop
# 2 1
# 2 2
# 2 3
# 2 4
# 2 5 breaking the inner loop
# 3 1
# 3 2
# 3 3
# 3 4
# 3 5 breaking the inner loop
# 4 1
# 4 2
# 4 3
# 4 4
# 4 5 breaking the inner loop
# 5 1
# 5 2
# 5 3
# 5 4
# 5 5 breaking the inner loop
# 6 1
# 6 2
# 6 3
# 6 4
# 6 5 breaking the inner loop
# 7 1
# 7 2
# 7 3
# 7 4
# 7 5 breaking the inner loop
# 8 1
# 8 2
# 8 3
# 8 4
# 8 5 breaking the inner loop
# 9 1
# 9 2
# 9 3
# 9 4
# 9 5 breaking the inner loop
# 10 1
# 10 2
# 10 3
# 10 4
# 10 5 breaking the inner loop

# next session will see for else loop 
# while loop