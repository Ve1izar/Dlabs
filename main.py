from library import LibrarySystem
from notifications import UserNotifier, EmailAlert
from book import Book
from user import Reader


def main():
    print("--- Ініціалізація компонентів системи ---")
    # Отримуємо єдиний екземпляр бібліотеки (Singleton)
    lib = LibrarySystem()

    # Створюємо конкретних спостерігачів
    reader1_notifier = UserNotifier("Даніеле")
    reader2_notifier = UserNotifier("Олена")
    email_service = EmailAlert()

    # Створюємо користувача-читача
    reader_user = Reader("Даніеле", "dan@email.com", "м. Рівне", "123-456")

    print("\n--- Налаштування підписок (через інтерфейс Observer) ---")
    lib.attach(reader1_notifier)
    lib.attach(reader2_notifier)
    lib.attach(email_service)

    print("\n--- Демонстрація роботи системи ---")
    book1 = Book("Роберт Мартін", "Чистий код", 2008, "978-0132350884", 3)
    book2 = Book(
        "Адітья Бхаргава", "Грокаємо алгоритми", 2017, "978-1617292231", 5
    )

    print("Бібліотекар додає книги...")
    lib.add_book(book1)
    print("-" * 20)
    lib.add_book(book2)

    print("\n--- Демонстрація пошуку (через інтерфейс BookSearch) ---")
    reader_user.perform_search(lib, "код")


if __name__ == "__main__":
    main()
