from utils import books

def add():
    book_name = input("Enter the Book name to add: ").upper()
    books[book_name] = "AVAILABLE"
    print(f"Book Added: {book_name}")
