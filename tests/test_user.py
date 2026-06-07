import unittest
from unittest.mock import Mock
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from user import Reader  # noqa: E402
from interfaces import BookSearch  # noqa: E402


class TestReader(unittest.TestCase):
    def setUp(self):
        # Створюємо користувача
        self.reader = Reader(
            "Даніеле", "dan@email.com", "м. Рівне", "123-456"
        )
        # Створюємо mock-об'єкт для інтерфейсу пошуку
        self.mock_search_provider = Mock(spec=BookSearch)

    def test_initial_state(self):
        """Перевірка ініціалізації читача [cite: 148]"""
        self.assertEqual(self.reader.name, "Даніеле")
        self.assertEqual(self.reader.email, "dan@email.com")
        self.assertFalse(self.reader.hasDebt)

    def test_perform_search_calls_provider(self):
        """Перевіряємо, що perform_search викликає search_books у провайдера"""
        # Налаштовуємо повернення фейкових даних
        self.mock_search_provider.search_books.return_value = ["Чистий код"]

        # Виконуємо дію
        self.reader.perform_search(self.mock_search_provider, "код")

        # Перевіряємо, чи був викликаний метод заглушки з правильним параметром
        self.mock_search_provider.search_books.assert_called_once_with("код")


if __name__ == '__main__':
    unittest.main()
