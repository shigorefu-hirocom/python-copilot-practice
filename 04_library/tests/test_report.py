from book import Book
from library import Library
from member import Member
from report import build_report


def test_report_shows_available_and_borrowed_books_without_mutation():
    books = [Book(1, "Python入門"), Book(2, "データの扱い方")]
    library = Library(books, [Member(1, "田中")])
    library.lend_book(1, 1)
    before = [book.borrower_id for book in books]

    result = build_report(library)

    assert result.splitlines() == [
        "図書館の本:",
        "1: Python入門 [貸出中: 田中]",
        "2: データの扱い方 [貸出可能]",
    ]
    assert [book.borrower_id for book in books] == before


# TODO: 空の図書館と、返却後のレポートをテストする。
