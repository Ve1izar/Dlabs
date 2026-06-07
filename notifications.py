from interfaces import Observer


class UserNotifier(Observer):
    def __init__(self, username: str):
        self.username = username

    def update(self, book_title: str) -> None:
        print(
            f"[{self.username} Сповіщення]: "
            f"Нова книга у каталозі '{book_title}'"
        )


class EmailAlert(Observer):
    def update(self, book_title: str) -> None:
        print(
            f"[EmailAlert]: "
            f"Надсилаємо email підписникам про книгу '{book_title}'."
              )
