# NAME: expense_tracker.py

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

    while True:
        try:
            amount = float(input("Enter Amount: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

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
def total_all(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

# total_by_category function:
# Ask for category
# Loop through expenses
# Only add amounts where category matches
# Return the total
def total_by_category(expenses, category):
    total = 0
    for expense in expenses:
        if expense["category"].lower() == category.lower():
            total += expense["amount"]
    return total

# total_by_vendor function:
# Ask for vendor
# Loop through expenses
# Only add amounts where vendor matches
# Return the total
def total_by_vendor(expenses, vendor):
    total = 0
    for expense in expenses:
        if expense["vendor"].lower() == vendor.lower():
            total += expense["amount"]
    return total

# show_totals_menu function:
# Display A, C, V options
# Call the correct total function based on user choice
def show_totals_menu(expenses):
    print("--- Totaling Options ---")
    print("A: All Expenses")
    print("C: Filter by Category")
    print("V: Filter by Vendor")

    choice = input("Choice: ").upper()

    if choice == "A":
        total = total_all(expenses)
        print(f"The total for all expenses is: ${total:.2f}")

    elif choice == "C":
        category = input("Enter Category to sum: ")
        total = total_by_category(expenses, category)
        print(f"The total for {category} is: ${total:.2f}")

    elif choice == "V":
        vendor = input("Enter Vendor to sum: ")
        total = total_by_vendor(expenses, vendor)
        print(f"The total for {vendor} is: ${total:.2f}")

    else:
        print("Invalid choice.")

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
def main():
    expenses = []

    while True:
        print("\nMain Menu:")
        print("1. Add New Expense")
        print("2. Get Totals")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_totals_menu(expenses)
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.")
main()