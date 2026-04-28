# NAME: expense tracker.py

# IMPORT STATEMENTS
# No imports needed

# FUNCTION DEFINITIONS

# add_expense function:
# Ask user for category, vendor, amount, and date
# Store one expense as a dictionary
# Add that dictionary to the expenses list
def add_expense(expenses):
    category = input("Enter Category: ")
    vendor = input("Enter Vendor: ")
    amount = float(input("Enter Amount: "))
    date = input("Enter Date: ")
    expense = {
        "category": category,
        "vendor": vendor,
        "amount": amount,
        "date": date
    }
    expenses.append(expense)


# total_all function:
# Loop through all expense dictionaries
# Add every amount together
# Return the total

# total_by_category function:
# Ask for category
# Loop through expenses
# Only add amounts where category matches
# Return the total

# total_by_vendor function:
# Ask for vendor
# Loop through expenses
# Only add amounts where vendor matches
# Return the total

# show_totals_menu function:
# Display A, C, V options
# Call the correct total function based on user choice

# PROGRAM LOGIC

# Create an empty list called expenses
# Start a while loop
# Display main menu:
# 1. Add New Expense
# 2. Get Totals
# 3. Exit
# If user chooses 1, add expense
# If user chooses 2, show totals menu
# If user chooses 3, exit program

expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add New Expense")
    print("2. View Raw Expense List")
    print("3. Exit")

    selection = input("Selection: ")

    if selection == "1":
        add_expense(expenses)

    if selection == "2":
        print(expenses)

    if selection == "3":
        break