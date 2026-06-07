from abc import ABC, abstractmethod


class Observer(ABC):
    """Інтерфейс для отримання сповіщень (з ЛР №4)"""
    @abstractmethod
    def update(self, book_title: str) -> None:
        pass


class BookSearch(ABC):
    """Інтерфейс для пошуку книг у каталозі"""
    @abstractmethod
    def search_books(self, query: str) -> list:
        pass
