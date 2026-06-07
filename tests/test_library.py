import unittest
from unittest.mock import Mock
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from library import LibrarySystem  # noqa: E402
from interfaces import Observer  # noqa: E402
from book import Book  # noqa: E402


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = LibrarySystem()
        self.book = Book("Роберт Мартін", "Чистий код", 2008, "12345", 3)

    def tearDown(self):
        LibrarySystem._instance = None
        if hasattr(self.library, '_observers'):
            self.library._observers = []
        if hasattr(self.library, 'catalog'):
            self.library.catalog = []

    def test_singleton_instance(self):
        """Перевірка унікальності екземпляра Singleton"""
        library2 = LibrarySystem()
        self.assertIs(self.library, library2)

    def test_attach_detach_observer(self):
        """Перевірка підписки та відписки"""
        mock_observer = Mock(spec=Observer)

        self.library.attach(mock_observer)
        self.assertIn(mock_observer, self.library._observers)

        self.library.detach(mock_observer)
        self.assertNotIn(mock_observer, self.library._observers)

    def test_add_book_notifies_observers(self):
        mock_observer1 = Mock(spec=Observer)
        mock_observer2 = Mock(spec=Observer)

        self.library.attach(mock_observer1)
        self.library.attach(mock_observer2)

        self.library.add_book(self.book)

        mock_observer1.update.assert_called_once_with("Чистий код")
        mock_observer2.update.assert_called_once_with("Чистий код")


if __name__ == '__main__':
    unittest.main()
