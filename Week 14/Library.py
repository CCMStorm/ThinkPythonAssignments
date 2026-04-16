# NAME: library.py
# IMPORT STATEMENTS

# CLASS DEFINITIONS
class Book:
    # __init__(self, title, author)
        # set self.title = title
        # set self.author = author
        # set self.is_available = True (default)

    # __str__(self)
        # if self.is_available is True
            # status = "Available"
        # else
            # status = "Checked Out"
        # return formatted string with title, author, and status

    # checkout(self)
        # set self.is_available = False

    # return_book(self)
        # set self.is_available = True


# PROGRAM LOGIC
# create at least two Book objects

# print both books

# call checkout() on one book

# print both books again to show updated status