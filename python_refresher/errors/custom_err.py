class TooManyPagesRead(ValueError):
    pass


class MyBook:
    def __init__(self, name: str, total_pages: int):
        self.name = name
        self.total_pages = total_pages
        self.pages_read_already = 0

    def read(self, pages_read):
        if (pages_read + self.pages_read_already) > self.total_pages:
            raise TooManyPagesRead(
                f"You tried to read {pages_read} more pages. But the book has only {self.total_pages - self.pages_read_already} pages remaining"
            )
        self.pages_read_already += pages_read

        print(f"You have read {pages_read+self.pages_read_already} out of {self.total_pages} pages")


python = MyBook("Python_Jose", 100)

try:
    python.read(50)
    python.read(100)
except TooManyPagesRead as e:
    print(e)
    print("You tried to read too much pages")

