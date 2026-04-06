# NAME: The Rectangle Calculator.py
# IMPORT STATEMENTS

# FUNCTION DEFINITIONS
# define calculate_rectangle(length, width)
#     calculate area = length * width
#     calculate perimeter = 2 * (length + width)
#     pack both values into a tuple (area, perimeter)
#     return the tuple
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

# PROGRAM LOGIC
# get user input for length
length = float(input("Enter the length of the rectangle: "))
# get user input for width
width = float(input("Enter the width of the rectangle: "))
# call calculate_rectangle function
result = calculate_rectangle(length, width)
# unpack returned tuple into my_area and my_perimeter
my_area, my_perimeter = calculate_rectangle(length, width)
# print results clearly
print("\n--- Results ---")
print(f"The area of the rectangle is: {my_area}")
print(f"The perimeter of the rectangle is: {my_perimeter}")

