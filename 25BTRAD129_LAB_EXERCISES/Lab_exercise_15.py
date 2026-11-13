class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print(f'"{self.title}" issued successfully.')
        else:
            print(f'"{self.title}" is currently unavailable.')

    def return_book(self):
        if not self.available:
            self.available = True
            print(f'"{self.title}" returned successfully.')
        else:
            print(f'"{self.title}" was not issued.')

    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.book_id:<8} {self.title:<22} {self.author:<18} {status}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\nID      Title                  Author             Status")
        print("-" * 65)
        for book in self.books:
            book.display()

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

library = Library()
library.add_book(Book("B101", "Python Basics", "John Smith"))
library.add_book(Book("B102", "Data Science", "Rita Kumar"))

while True:
    print("\nLIBRARY MENU")
    print("1. Display books")
    print("2. Issue book")
    print("3. Return book")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        library.display_books()
    elif choice in ("2", "3"):
        book_id = input("Enter book ID: ").strip()
        book = library.find_book(book_id)
        if book is None:
            print("Book not found.")
        elif choice == "2":
            book.issue()
        else:
            book.return_book()
    elif choice == "4":
        print("Library system closed.")
        break
    else:
        print("Invalid choice.")
