class Book:
    def __init__(self, book_id: int, title: str):
        self.book_id = book_id
        self.title = title
        self.borrower_id: int | None = None
