# 2. Library Management System

# Features:

# Add books.
# Borrow books.
# Return books.
# Search books.
# Show overdue books.

# Challenge: Prevent duplicate IDs and unavailable books.
from datetime import datetime, date

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.due_date = None

    def __str__(self):
        status = f"Borrowed (Due: {self.due_date})" if self.is_borrowed else "Available"
        return f"ID: {self.book_id} | Title: '{self.title}' | Author: {self.author} | Status: {status}"


class LibrarySystem:
    def __init__(self):
        self.books = {}

    def add_book(self, book_id: str, title: str, author: str):
        if book_id in self.books:
            print(f" Error: Cannot add book. ID '{book_id}' already exists ({self.books[book_id].title}).")
            return False
        
        self.books[book_id] = Book(book_id, title, author)
        print(f" Success: '{title}' added to the library.")
        return True

    def borrow_book(self, book_id: str, days_to_borrow: int = 14):
        book = self.books.get(book_id)
        
        if not book:
            print(f" Error: Book ID '{book_id}' not found in the library.")
            return False
        
        if book.is_borrowed:
            print(f" Error: '{book.title}' is currently unavailable (already borrowed).")
            return False
        
        book.is_borrowed = True
       
        from datetime import timedelta
        book.due_date = date.today() + timedelta(days=days_to_borrow)
        print(f" Success: You have borrowed '{book.title}'. Due date: {book.due_date}")
        return True

    def return_book(self, book_id: str):
        book = self.books.get(book_id)
        
        if not book:
            print(f" Error: Book ID '{book_id}' not found.")
            return False
        
        if not book.is_borrowed:
            print(f" Warning: '{book.title}' was not checked out.")
            return False
        
        book.is_borrowed = False
        book.due_date = None
        print(f"Success: '{book.title}' has been returned and is now available.")
        return True

    def search_books(self, keyword: str):
        keyword = keyword.lower()
        results = [
            book for book in self.books.values()
            if keyword in book.title.lower() or keyword in book.author.lower() or keyword in book.book_id.lower()
        ]
        
        print(f"\n Search Results for '{keyword}':")
        if not results:
            print("   No matching books found.")
        for book in results:
            print(f"   - {book}")
        print()

    def show_overdue_books(self):
        today = date.today()
        overdue_books = [
            book for book in self.books.values()
            if book.is_borrowed and book.due_date < today
        ]
        
        print(f"\n Overdue Books Report (As of {today}):")
        if not overdue_books:
            print("Perfect! No overdue books right now.")
        for book in overdue_books:
            days_overdue = (today - book.due_date).days
            print(f"   - '{book.title}' (ID: {book.book_id}) | Overdue by {days_overdue} day(s)")
        print()
            

        

library = LibrarySystem()


library.add_book("B01", "Designing Data-Intensive Applications", "Martin Kleppmann")
library.add_book("B02", "Understanding Transformers", "Attention Team")

library.add_book("B01", "Duplicate Book Title", "Fake Author") 


library.borrow_book("B01")

library.borrow_book("B01") 


library.search_books("Data")


library.return_book("B01")

library.borrow_book("B01") 


library.add_book("B03", "Legacy Systems Guide", "Old Coder")
library.borrow_book("B03")
library.books["B03"].due_date = date(2026, 5, 1) 

library.show_overdue_books()
        
