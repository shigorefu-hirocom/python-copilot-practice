from book import Book
from member import Member


class Library:
    def __init__(self, books: list[Book], members: list[Member]):
        self.books = books
        self.members = members

    def lend_book(self, book_id: int, member_id: int) -> None:
        member = None
        for candidate in self.members:
            if candidate.member_id == member_id:
                member = candidate
                break
        if member is None:
            raise ValueError("会員が見つかりません")

        book = None
        for candidate in self.books:
            if candidate.book_id == book_id:
                book = candidate
                break
        if book is None:
            raise ValueError("本が見つかりません")
        if book.borrower_id is not None:
            raise ValueError("貸出中です")
        book.borrower_id = member.member_id

    def return_book(self, book_id: int, member_id: int) -> None:
        member = None
        for candidate in self.members:
            if candidate.member_id == member_id:
                member = candidate
                break
        if member is None:
            raise ValueError("会員が見つかりません")

        book = None
        for candidate in self.books:
            if candidate.book_id == book_id:
                book = candidate
                break
        if book is None:
            raise ValueError("本が見つかりません")
        if book.borrower_id is None:
            raise ValueError("この本は貸し出されていません")
        if book.borrower_id != member.member_id:
            raise ValueError("借りた会員と一致しません")
        book.borrower_id = None

    # TODO: 動作を保ち、繰り返している検索処理を整理する。
