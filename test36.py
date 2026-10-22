# ATM Machine 
# Pin =  1901 
# curr balance = 20000 

atm_pin = 1901
acc_balance = 20000
print("Insert the card")
pin = int(input("Enter your pin: "))

if pin == atm_pin:
    print("Your pin is correct!")
    user_amt = int(input("Enter your amount to withdraw: "))
    if user_amt > acc_balance:
        print("Insufficent Balance")
    else:
        print(f"Withdrawl of {user_amt} succesfull")
        remaining_balance = acc_balance - user_amt
        print(f"Remaining balance in your acc is {remaining_balance}")
        
else:
    print("You have enterd incorrect atm pin")


# Insert the card
# Enter your pin: 1902
# You have enterd incorrect atm pin

# Insert the card
# Enter your pin: 1901
# Your pin is correct!
# Enter your amount to withdraw: 21000
# Insufficent Balance

# Insert the card
# Enter your pin: 1901
# Your pin is correct!
# Enter your amount to withdraw: 8000
# Withdrawl of 8000 succesfull
# Remaining balance in your acc is 12000