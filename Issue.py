from utils import books, issue_books

def issue():
    book_name = input("Enter book name: ").upper()

    if book_name in books:
        issue_books[book_name] = "ISSUED"
        del books[book_name]
        print("Book assigned successfully")
    else:
        print("Book not available")
