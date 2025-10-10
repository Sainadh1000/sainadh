# Create a Book class with:

# Private attributes:

# title (string)

# author (string)

# isbn (string)

# is_available (bool)

# ✅ Public methods:

# borrow_book() – marks the book as not available if it isn't already borrowed.

# return_book() – marks the book as available again.

# display_info() – prints all details including whether the book is available.

# Getters for all attributes.

# Optional: Setters to update title, author, or ISBN.

class Book:
    def __init__(self, title, author, isbn):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__is_available = True  

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def is_available(self):
        return self.__is_available

    
    def borrow_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"You have borrowed '{self.__title}'.")
        else:
            print(f"'{self.__title}' is currently not available.")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"You have returned '{self.__title}'.")
        else:
            print(f"'{self.__title}' was not borrowed.")

    def display_info(self):
        status = "Available" if self.__is_available else "Not Available"
        print(f"Title : {self.__title}")
        print(f"Author: {self.__author}")
        print(f"ISBN  : {self.__isbn}")
        print(f"Status: {status}")