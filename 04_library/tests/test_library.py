import pytest

from book import Book
from library import Library
from member import Member


def test_lend_then_return_updates_same_book():
    book = Book(1, "Python入門")
    library = Library([book], [Member(1, "田中")])

    library.lend_book(1, 1)
    assert book.borrower_id == 1
    assert library.books[0] is book

    library.return_book(1, 1)
    assert book.borrower_id is None


def test_second_loan_preserves_original_borrower():
    book = Book(1, "Python入門")
    library = Library([book], [Member(1, "田中"), Member(2, "佐藤")])
    library.lend_book(1, 1)

    with pytest.raises(ValueError) as error:
        library.lend_book(1, 2)

    assert str(error.value) == "貸出中です"
    assert book.borrower_id == 1


def test_other_member_cannot_return_book():
    book = Book(1, "Python入門")
    library = Library([book], [Member(1, "田中"), Member(2, "佐藤")])
    library.lend_book(1, 1)

    with pytest.raises(ValueError) as error:
        library.return_book(1, 2)

    assert str(error.value) == "借りた会員と一致しません"
    assert book.borrower_id == 1


# TODO: 不明な会員ID、本のID、未貸出の本の返却、エラーの優先順を確認する。
