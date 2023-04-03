class BookShelf:
    def __init__(self, *books):
        print(books)
        self.books = books

    def __str__(self):
        return f"Booksehlf with {len(self.books)} books"


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book1 = Book("Harry Potter")
print(book1)
book2 = Book("Harry Potter1")
print(book2)

shelf = BookShelf(book1, book2)
print(shelf)
