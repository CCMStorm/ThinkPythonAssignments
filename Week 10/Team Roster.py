# NAME: roster.py
# IMPORT STATEMENTS

# FUNCTION DEFINITIONS

# Function: add_players(roster)
# - Use a while loop
# - Ask user to enter player name
# - If user enters "quit", stop loop
# - Otherwise, append name to roster list
def add_players(roster):
    while True:
        name = input("Enter player name (or 'quit' to stop): ")
        
        if name.lower() == "quit":
            break
        
        roster.append(name)

# Function: is_on_roster(roster, name)
# - Loop through roster
# - If name matches a player, return True
# - If loop ends without match, return False
def is_on_roster(roster, name):
    for player in roster:
        if player == name:
            return True
    return False

roster = []

add_players(roster)

# Test to confirm names were added
print("Current roster:", roster)


# PROGRAM LOGIC
# - Create empty list called roster
# - Call add_players(roster)
# - Ask user for a name to search
# - Call is_on_roster(roster, name)
# - Print result based on True/False