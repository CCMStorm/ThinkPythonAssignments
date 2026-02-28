# IMPORT STATEMENTS
# No imports needed

# FUNCTION DEFINITIONS
# Define is_palindrome(word)
#   Make the word lowercase 
#   Reverse the word using slicing 
#   Compare the lowercase word to the reversed word
#   Return True if they match, otherwise return False
def is_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    
    if word == reversed_word:
        return True
    else:
        return False

# PROGRAM LOGIC
# Ask the user for a word
# Call is_palindrome on the user's word
# If True, print "(word) is a palindrome"
# Else, print "(word) is not a palindrome"