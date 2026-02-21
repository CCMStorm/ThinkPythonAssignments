# IMPORT STATEMENTS
# (None)

# FUNCTION DEFINITIONS
# 1. Define verify_pin(): 
#    - Create a loop that asks for a PIN until it equals "1234"
#    - Return True
def verify_pin():
    while True:
        pin = input("Enter PIN: ")
        
        if pin == "1234":
            print("PIN Verified.")
            return True
        else:
            print("Incorrect PIN. Try again.")

# 2. Define withdraw(balance, amount):
#    - Check if enough money exists
#    - Return the new (or old) balance
def withdraw(balance, amount):
    if amount <= balance:
        new_balance = balance - amount
        print("Withdrawal successful.")
        return new_balance
    else:
        print("Insufficient funds.")
        return balance
    
# PROGRAM LOGIC

current_balance = 500.0
# Verify PIN first
verify_pin()
# Ask for withdrawal amount
amount = float(input("Enter withdrawal amount: "))
# Update balance using returned value
current_balance = withdraw(current_balance, amount)
# Print final balance
print("Current Balance: $" + str(current_balance))

