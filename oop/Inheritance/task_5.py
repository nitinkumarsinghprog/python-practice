# Parent: LibraryItem
#   - attributes: title, item_id, is_available (default True)
#   - method: checkout() -> is_available = False
#   - method: return_item() -> is_available = True
#   - method: display()
#
# Child: Book
#   - extra: author, pages
#   - override display()
#
# Child: DVD
#   - extra: director, duration
#   - override display()
#
# Child: Magazine
#   - extra: issue_number, month
#   - override display()

class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_available = True

    def checkout(self):
        if not self.is_available:
            print(f"❌ '{self.title}' already checked out!")
            return
        self.is_available = False
        print(f"✅ '{self.title}' checked out successfully!")

    def return_item(self):
        if self.is_available:
            print(f"⚠️  '{self.title}' is already available!")
            return
        self.is_available = True
        print(f"✅ '{self.title}' returned successfully!")

    def display(self):
        status = "✅ Available" if self.is_available else "❌ Not Available"
        print(f"--- {type(self).__name__} Details ---")
        print(f"Title     : {self.title}")
        print(f"Item ID   : {self.item_id}")
        print(f"Status    : {status}")

    def __str__(self):
        return f"{self.title} ({self.item_id})"


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def display(self):
        super().display()
        print(f"Author    : {self.author}")
        print(f"Pages     : {self.pages}")


class DVD(LibraryItem):
    def __init__(self, title, item_id, director, duration):
        super().__init__(title, item_id)
        self.director = director
        self.duration = duration

    def display(self):
        super().display()
        print(f"Director  : {self.director}")
        print(f"Duration  : {self.duration} mins")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number, month):
        super().__init__(title, item_id)
        self.issue_number = issue_number
        self.month = month

    def display(self):
        super().display()
        print(f"Issue No. : {self.issue_number}")
        print(f"Month     : {self.month}")


# ===== Test =====
print("=" * 50)
print("📚 LIBRARY MANAGEMENT SYSTEM")
print("=" * 50)

b = Book("Python Guide", "B001", "Guido van Rossum", 500)
b.display()
print("-" * 50)
b.checkout()
b.checkout()        # Already checked out — error message aayega
print("-" * 50)
b.return_item()
b.return_item()     # Already available — warning aayegi
print("-" * 50)

d = DVD("Inception", "D001", "Christopher Nolan", 148)
d.display()
print("-" * 50)

m = Magazine("Tech Today", "M001", 45, "October")
m.display()
print("-" * 50)

# __str__ test
print(f"\nItems: {b}, {d}, {m}")