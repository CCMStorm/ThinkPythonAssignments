# NAME: library.py
# IMPORT STATEMENTS

# CLASS DEFINITIONS
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        if self.is_available:
            status = "Available"
        else:
            status = "Checked Out"
        return f"'{self.title}' by {self.author} - {status}"

    def checkout(self):
        self.is_available = False

    # return_book(self)
        # set self.is_available = True
    def return_book(self):
        self.is_available = True    


# PROGRAM LOGIC
# create at least two Book objects
book1 = Book("Think Python", "Allen Downey")
book2 = Book("The Hobbit", "J.R.R. Tolkien")

# print both books
print("--- Library Status ---")
print(book1)
print(book2)

# call checkout() on one book
print("\nChecking out 'The Hobbit'...\n")
book2.checkout()

# print both books again to show updated status
print("--- Updated Status ---")
print(book1)
print(book2)