# NAME: expense_tracker.py

# IMPORT STATEMENTS
# No imports needed

# FUNCTION DEFINITIONS

# add_expense function:
# Ask user for category, vendor, amount, and date
# Store one expense as a dictionary
# Add that dictionary to the expenses list

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