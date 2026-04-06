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
result = calculate_rectangle(5, 10)
print(result)   # Expected: (50, 30)