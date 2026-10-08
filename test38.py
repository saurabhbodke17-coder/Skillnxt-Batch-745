# add deposite facility
# whether you want to deposite or withdraw

atm_pin = 1901
acc_balance = 20000
print("Insert the card")
pin = int(input("Enter your pin: "))
if pin == atm_pin:
    print("Your pin is correct!")
    uset_input = input("Do you want to withdraw or deposite the amt?\nIf you want to deposite Enter D else W for withdraw: ")

    if uset_input.lower() == "w":
        user_amt = int(input("Enter your amount to withdraw: "))
        if user_amt > acc_balance:
            print("Insufficent Balance")
        else:
            print(f"Withdrawl of {user_amt} succesfull")
            remaining_balance = acc_balance - user_amt
            print(f"Remaining balance in your acc is {remaining_balance}")

    elif uset_input.lower() == "d":
        user_amt = int(input("Enter your amount to Deposite: "))
        acc_balance = acc_balance + user_amt
        print(f"Deposite of {user_amt} is succesfull!")
        print(f"Your updated balance is {acc_balance}")

    else:
        print("You have provided the incorrect Input!")
 
else:
    print("You have enterd incorrect atm pin")

# Insert the card
# Enter your pin: 1901
# Your pin is correct!
# Do you want to withdraw or deposite the amt?
# If you want to deposite Enter D else W for withdrawD
# Enter your amount to Deposite: 4500
# Deposite of 4500 is succesfull!
# Your updated balance is 24500

# Insert the card
# Enter your pin: 1901
# Your pin is correct!
# Do you want to withdraw or deposite the amt?
# If you want to deposite Enter D else W for withdraw: k
# You have provided the incorrect Input!

# Insert the card
# Enter your pin: 1901
# Your pin is correct!
# Do you want to withdraw or deposite the amt?
# If you want to deposite Enter D else W for withdraw: w
# Enter your amount to withdraw: 2300
# Withdrawl of 2300 succesfull
# Remaining balance in your acc is 17700

# Insert the card
# Enter your pin: 1901
# Your pin is correct!
# Do you want to withdraw or deposite the amt?
# If you want to deposite Enter D else W for withdraw: w
# Enter your amount to withdraw: 80000
# Insufficent Balance