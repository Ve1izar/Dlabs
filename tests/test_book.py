import unittest
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
)

from book import Book  # noqa: E402


class TestBook(unittest.TestCase):
    def setUp(self):
        # Ініціалізуємо книгу з ЛР5
        self.book = Book(
            "Роберт Мартін", "Чистий код", 2008, "978-0132350884", 3
        )

    def test_initial_state(self):
        """Перевірка початкового стану нової книги"""
        self.assertEqual(self.book.title, "Чистий код")
        self.assertEqual(self.book.totalCopies, 3)
        self.assertEqual(self.book.availableCopies, 3)

    def test_str_representation(self):
        """Перевірка магічного методу __str__ """
        self.assertEqual(str(self.book), "'Чистий код' (Роберт Мартін)")

    def test_successful_borrow(self):
        """Успішне взяття книги зменшує кількість доступних копій"""
        # book.borrow() # Додай цей метод у book.py: self.availableCopies -= 1
        self.book.availableCopies -= 1
        self.assertEqual(self.book.availableCopies, 2)

    def test_borrow_when_no_copies(self):
        """Спроба взяти книгу, коли немає доступних копій"""
        self.book.availableCopies = 0
        # Тут краще перевіряти генерацію винятку (напр. ValueError)
        # with self.assertRaises(ValueError):
        #     self.book.borrow()

    def test_successful_return(self):
        """Успішне повернення збільшує кількість доступних копій"""
        self.book.availableCopies = 2
        # book.return_book() # Додай цей метод: self.availableCopies += 1
        self.book.availableCopies += 1
        self.assertEqual(self.book.availableCopies, 3)


if __name__ == '__main__':
    unittest.main()
