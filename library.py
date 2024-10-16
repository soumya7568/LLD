from datetime import datetime, timedelta

class BookItem:
    def __init__(self, barcode, status="Available"):
        self.barcode = barcode
        self.status = status

class Book:
    def __init__(self, isbn, title, author, category, total_copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.category = category
        self.book_items = [BookItem(f"{isbn}_{i}") for i in range(total_copies)]

    def get_available_copies(self):
        return [item for item in self.book_items if item.status == "Available"]

class Loan:
    def __init__(self, book_item, loan_date, return_date):
        self.book_item = book_item
        self.loan_date = loan_date
        self.return_date = return_date
        self.fine_amount = 0

    def calculate_fine(self):
        today = datetime.now()
        if today > self.return_date:
            late_days = (today - self.return_date).days
            self.fine_amount = late_days * 2  # Assume $2 fine per day
        return self.fine_amount

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book_item):
        if book_item.status == "Available":
            book_item.status = "Borrowed"
            loan = Loan(book_item, datetime.now(), datetime.now() + timedelta(days=14))
            self.borrowed_books.append(loan)
            print(f"Book {book_item.barcode} borrowed by {self.name}")
        else:
            print(f"Book {book_item.barcode} is not available")

    def return_book(self, book_item):
        loan = next((l for l in self.borrowed_books if l.book_item == book_item), None)
        if loan:
            fine = loan.calculate_fine()
            if fine > 0:
                print(f"Fine for late return: ${fine}")
            book_item.status = "Available"
            self.borrowed_books.remove(loan)
            print(f"Book {book_item.barcode} returned by {self.name}")

class Librarian:
    def __init__(self, name):
        self.name = name

    def issue_book(self, user, book_item):
        user.borrow_book(book_item)

    def accept_return(self, user, book_item):
        user.return_book(book_item)

# Example Usage
book = Book("978-0132350884", "Clean Code", "Robert C. Martin", "Programming", 5)
user = User("U001", "John Doe")
librarian = Librarian("Alice")

# Borrow a book
available_books = book.get_available_copies()
if available_books:
    librarian.issue_book(user, available_books[0])

# Return the book
librarian.accept_return(user, available_books[0])
