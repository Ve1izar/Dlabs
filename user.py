from interfaces import BookSearch


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email


class Reader(User):
    def __init__(self, name: str, email: str, address: str, phone: str):
        super().__init__(name, email)
        self.address = address
        self.phone = phone
        self.hasDebt = False

    def perform_search(self, search_provider: BookSearch, query: str):
        print(f"{self.name} шукає книгу за запитом '{query}':")
        results = search_provider.search_books(query)
        for r in results:
            print(f" - Знайдено: {r}")
