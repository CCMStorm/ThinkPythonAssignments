# IMPORT STATEMENTS
# (None)

# FUNCTION DEFINITIONS
# 1. Define print_bio with three parameters: name, age, goal
# 2. Inside the function, print a border line using string multiplication (*)
# 3. Print the bio details using the parameter names
def print_bio(name, age, goal):
    # Print top border
    print("*" * 25)
    # Print bio sentence
    print("Name:", name + ",", "Age:", age, "Goal:", goal)
    # Print bottom border
    print("*" * 25)

# PROGRAM LOGIC
# 1. Call print_bio using my own info
print_bio ( "Conner Monahan", 28, "Learn Python." )
# 2. Call print_bio using a famous person
print_bio ( "Albert Einstein", 76, "Discover the theory of relativity." )
# 3. Call print_bio using a fictional character
print_bio ( "Harry Potter", 17, "Defeat Voldemort." )