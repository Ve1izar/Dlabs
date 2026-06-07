from interfaces import Observer, BookSearch
from book import Book


class LibrarySystem(BookSearch):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.catalog = []
            cls._instance.borrowings = []
            cls._instance._observers = []
        return cls._instance

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, book_title: str) -> None:
        for obs in self._observers:
            obs.update(book_title)

    def add_book(self, book: Book) -> None:
        self.catalog.append(book)
        self.notify(book.title)

    def search_books(self, query: str) -> list:
        # Реалізація інтерфейсу BookSearch
        return [
            book for book in self.catalog
            if query.lower() in book.title.lower()
        ]
