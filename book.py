class Book:
    def __init__(
            self, author: str, title: str,
            year: int, isbn: str, copies: int
    ):
        self.author = author
        self.title = title
        self.year = year
        self.isbn = isbn
        self.totalCopies = copies
        self.availableCopies = copies

    def __str__(self):
        return f"'{self.title}' ({self.author})"
