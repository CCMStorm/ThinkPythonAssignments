# IMPORT STATEMENTS
# 1. Import math

# FUNCTION DEFINITIONS
# 1. Define area(radius): returns pi * r squared
import math


def area (radius):
    return math.pi * radius ** 2
# 2. Define circumference(radius): returns 2 * pi * r
def circumference (radius):
    return 2 * math.pi * radius
# 3. Define volume(radius, height): 
def volume(radius, height):
#    - Call area(radius) and multiply by height.
#    - Return the result.
    return area(radius) * height

# PROGRAM LOGIC
# 1. Input for radius (float)
radius = float(input("Enter the radius of the circle: "))
# 2. Call and print area and circumference.
print("Area:", area(radius))
print("Circumference:", circumference(radius))
# 3. Input for height (float)
height = float(input("Enter the height of the cylinder: "))
# 4. Call and print volume.
print("Volume:", volume(radius, height))
