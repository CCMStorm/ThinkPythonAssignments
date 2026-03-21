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

# PROGRAM LOGIC
# - Create empty list called roster
roster = []
# - Call add_players(roster)
add_players(roster)
# - Ask user for a name to search
search_name = input("Enter a name to search on the roster: ")
# - Call is_on_roster(roster, name)
found = is_on_roster(roster, search_name)
# - Print result based on True/False
if found:
    print(f"{search_name} is on the roster.")
else:
    print(f"{search_name} is not on the roster.")
    