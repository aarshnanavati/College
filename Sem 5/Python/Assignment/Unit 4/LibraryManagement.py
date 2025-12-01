# Design a mini Library Management System with Book, Member, and Transaction classes to demonstrate
#  attributes, methods, encapsulation, and object relationships. Add books, issue/return books, and t
#  rack availability.


class Book:
    def __init__(self, title, author, total_copies):
        self.title = title
        self.author = author
        self._total_copies = total_copies  # encapsulated attribute
        self._available_copies = total_copies  # tracks available books

    def is_available(self):
        """Check if the book is available."""
        return self._available_copies > 0

    def issue(self):
        """Issue a book if available."""
        if self.is_available():
            self._available_copies -= 1
            return True
        else:
            return False

    def return_book(self):
        """Return a book."""
        if self._available_copies < self._total_copies:
            self._available_copies += 1
            return True
        return False

    def display(self):
        """Display book details."""
        print(f"'{self.title}' by {self.author} | Available: {self._available_copies}/{self._total_copies}")

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []  # list of borrowed books

    def display(self):
        print(f"Member: {self.name} (ID: {self.member_id}) | Borrowed books: {[book.title for book in self.borrowed_books]}")
class Transaction:
    def __init__(self):
        self.transactions = []  # store transaction history

    def issue_book(self, book, member):
        """Issue a book to a member."""
        if book.issue():
            member.borrowed_books.append(book)
            self.transactions.append(f"{member.name} issued '{book.title}'")
            print(f"✅ Book '{book.title}' issued to {member.name}")
        else:
            print(f"❌ Book '{book.title}' is not available")

    def return_book(self, book, member):
        """Return a book from a member."""
        if book in member.borrowed_books:
            book.return_book()
            member.borrowed_books.remove(book)
            self.transactions.append(f"{member.name} returned '{book.title}'")
            print(f"✅ Book '{book.title}' returned by {member.name}")
        else:
            print(f"❌ {member.name} did not borrow '{book.title}'")

    def display_transactions(self):
        print("\n--- Transaction History ---")
        for t in self.transactions:
            print(t)

# Create some books
book1 = Book("Python Programming", "John Doe", 3)
book2 = Book("Data Science 101", "Jane Smith", 2)

# Create members
member1 = Member("Alice", 101)
member2 = Member("Bob", 102)

# Create transaction manager
transaction = Transaction()

# Display books
book1.display()
book2.display()

# Issue books
transaction.issue_book(book1, member1)  # Alice borrows Python book
transaction.issue_book(book2, member2)  # Bob borrows Data Science book
transaction.issue_book(book1, member2)  # Bob borrows Python book

# Return book
transaction.return_book(book1, member1)  # Alice returns Python book

# Display updated status
book1.display()
book2.display()
member1.display()
member2.display()

# Show transaction history
transaction.display_transactions()
