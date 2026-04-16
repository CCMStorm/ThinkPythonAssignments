# NAME: library.py
# IMPORT STATEMENTS

# CLASS DEFINITIONS
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

# PROGRAM LOGIC
# create one book object
my_book = Book("Think Python", "Allen Downey")

# test that object works
print(my_book.title)
print(my_book.author)
print(my_book.is_available)