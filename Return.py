from utils import issue_books, books

def return_book():
    book_name = input("Enter book name: ").upper()

    if book_name in issue_books:
        books[book_name] = "AVAILABLE"
        del issue_books[book_name]
        print("Book returned")
    else:
        print("wrong number")
