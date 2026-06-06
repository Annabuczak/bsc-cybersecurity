class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_info(self):
        for book in self.books:
            status = "available" if book.is_available else "not available"
            print(f"{book.title} by {book.author} is {status}")

    def borrow(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"{book.title} by {book.author} has been borrowed.")
                else:
                    print(f"{book.title} by {book.author} is not available.")
                return

        print(f"{title} is not in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    print(f"{book.title} by {book.author} was already returned.")
                else:
                    book.is_available = True
                    print(f"{book.title} by {book.author} has been returned.")
                return

        print(f"{title} is not in the library.")


class Book:
    def __init__(self, title, author, isbn, is_available):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = is_available


book_1 = Book("Gone with the Wind", "Margaret Mitchell", "123456", True)
book_2 = Book("The Shadow of The Wind", "Carlos Ruiz Zafon", "654321", True)
book_3 = Book("The Lord of The Rings", "J.R.R Tolkien", "34443", False)
book_4 = Book("Wolf Hall", "Hilary Mantel", "234244", False)
book_5 = Book("Les Miserables", "Victor Hugo", "576282", True)

library = Library()
library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)
library.add_book(book_5)

library.display_info()

print()
library.borrow("Gone with the Wind")
library.borrow("Wolf Hall")

print()
library.return_book("Wolf Hall")

print()
library.display_info()
