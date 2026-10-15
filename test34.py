# if elif elsewrite down the program to give grades to the student
# in between A , B , C

# Marks >= 90 A 
# Marks >= 70 B
# Marks >= 40 C

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("A")
# elif marks >= 70:
#     print("B")
# elif marks >= 40:
#     print("C")
# else:
#     print("Fail")

# Enter your marks: 91
# A

# Enter your marks: 75
# B

# Enter your marks: 45
# C

# Enter your marks: 29
# Fail


# Temperature Classifier 

# if temp >=40 Hot
# if temp >=30 <= 39 Medium 
# if temp is <30 and >=20 low 
# if temp < 20 ..cold 

temp = 40
if temp >= 40:
    print("Hot")
elif temp >= 30 and temp < 40:
    print("Medium")
elif temp >= 20 and temp <30:
    print("Low")
else:
    print("Cold")


