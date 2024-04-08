#Day 64
class Library:
    def __init__(self):
        # Initializing instance variables
        self.noBooks = 0  # Variable to store the number of books in the library
        self.books = []   # List to store the books in the library

    def addBook(self, book):
        # Method to add a book to the library
        self.books.append(book)    # Adding the book to the list of books
        self.noBooks = len(self.books)  # Updating the number of books in the library

    def showInfo(self):
        # Method to display information about the library
        print(f"The library has {self.noBooks} books. The books are")
        for book in self.books:  # Iterating through the list of books
            print(book)  # Printing each book

# Creating an instance of the Library class
l1 = Library()

# Adding books to the library
l1.addBook("Harry Potter1")
l1.addBook("Harry Potter2")
l1.addBook("Harry Potter3")

# Displaying information about the library
l1.showInfo()

'''
Output:
The library has 3 books. The books are
Harry Potter1
Harry Potter2
Harry Potter3
'''
