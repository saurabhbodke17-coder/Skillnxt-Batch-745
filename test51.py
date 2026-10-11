# write down the function who will return me the max number 
# pass 2 numbers and find the max number

def get_max(a,b):
    if a > b:
        return a
    elif a == b:
        return "Both are same"
    else:
        return b

# res = get_max(10 , 20)
# print(res)
# # 20

# write down the function for showing the given number is odd or even 
def is_odd_or_even(num):
    if num % 2 == 0:
        return "Even Number"
    else:
        return "Odd number"
    
# res = is_odd_or_even(100)
# print(res)
# # Even Number


# write down the function and chech whether given string is palindrome or not
# madam , pop , eve 
def is_palindrome(string):
    # string which is input should be equal to its reverse 
    a = string
    b = string[::-1]
    if a.lower() == b.lower():
        return True
    else:
        return False

# res = is_palindrome("Madam")
# print(res)
# # True

# res = is_palindrome("Vishal")
# print(res)
# # False

res = is_palindrome("eve")
print(res)
# # True


