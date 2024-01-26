class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}"


class EBook(Book):
    def __init__(self, title, author, isbn, file_format):
        super().__init__(title, author, isbn)
        self.file_format = file_format

    def display_info(self):
        return f"{super().display_info()}\nFile Format: {self.file_format}"

class Library:
    def __init__(self):
        """
        Represents a library that stores books.
        """
        self.books = []

    def add_book(self, book):
        """
        Add a book to the library.

        Args:
        - book (Book): The book to be added to the library.
        """
        self.books.append(book)

    def list_books(self):
        """
        List all books in the library.

        Returns:
        - list: List of formatted strings containing information about each book.
        """
        return [book.display_info() for book in self.books]

    def search_book(self, title):
        """
        Search for a book by title.

        Args:
        - title (str): The title of the book to search for.

        Returns:
        - str: Formatted string containing information about the book if found, or an error message.
        """
        for book in self.books:
            if book.title.lower() == title.lower():
                return book.display_info()
        return "Book not found."

    def delete_book(self, isbn):
        """
        Delete a book from the library based on its ISBN.

        Args:
        - isbn (str): The ISBN of the book to be deleted.
        """
        self.books = [book for book in self.books if book.isbn != isbn]





