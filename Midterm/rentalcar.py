# NAME: rentalcar.py
# IMPORT STATEMENTS

# FUNCTION DEFINITIONS
# get_daily_rate(code)
#   return the daily rate based on classification code
def get_daily_rate(code):
    if code == "B":
        return 40
    if code == "S":
        return 60
    if code == "L":
        return 80
#     
# get_classification_name(code)
#   return full classification name
def get_classification_name(code):
    if code == "B":
        return "Budget"
    if code == "S":
        return "Standard"
    if code == "L":
        return "Luxury"
#
# calculate_charged_miles(total_miles)
#   first 100 miles are free
#   return miles over 100, or 0 if under 100
def calculate_charged_miles(total_miles):
    if total_miles > 100:
        return total_miles - 100
    else:
        return 0
#
# calculate_total_bill(code, days, total_miles)
#   use daily rate
#   use charged miles
#   mileage charge = charged miles * 0.35
#   total = daily rental cost + mileage charge
#   return total bill
def calculate_total_bill(code, days, total_miles):
    daily_rate = get_daily_rate(code)
    charged_miles = calculate_charged_miles(total_miles)
    mileage_charge = charged_miles * 0.35
    total_rental_cost = daily_rate * days
    total_bill = total_rental_cost + mileage_charge
    return total_bill
#
# validate_code()
#   ask user for B, S, or L
#   keep asking until valid
def validate_code():
    while True:
        code = input("Enter classification code (B, S, L): ")
        if code in ["B", "S", "L"]:
            return code
        else:
            print("Invalid code. Please enter B, S, or L.")


# PROGRAM LOGIC
# 1. Get valid classification code
classification_code = validate_code()
# 2. Get start odometer
start_odometer = int(input("Enter start odometer reading: "))
# 3. Get end odometer
end_odometer = int(input("Enter end odometer reading: "))
# 4. Get days rented
days_rented = int(input("Enter number of days rented: "))
# 5. Calculate total miles
total_miles = end_odometer - start_odometer
# 6. Calculate charged miles
charged_miles = calculate_charged_miles(total_miles)
# 7. Calculate total bill
total_bill = calculate_total_bill(classification_code, days_rented, total_miles)
# 8. Print rental summary
classification_name = get_classification_name(classification_code)
print("\nRental Summary:")
print(f"Classification: {classification_name}")
print(f"Total miles driven: {total_miles}")
print(f"Charged miles: {charged_miles}")
print(f"Total bill: ${total_bill:.2f}")

