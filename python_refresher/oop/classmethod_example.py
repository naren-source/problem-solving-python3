class Book:
    Types = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.Types[0], page_weight+100)

    @classmethod
    def softcover(cls, name, page_weight):
        return cls(name, cls.Types[1], page_weight-100)

    def __str__(self):
        return f"{self.name} book of type {self.book_type} weighing {self.weight}"

hard_book = Book.hardcover("Harry Potter", 1500)
soft_book = Book.softcover("Python 1010", 500)

print(hard_book)
print(soft_book)
