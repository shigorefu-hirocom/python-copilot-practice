from book import Book
from library import Library
from member import Member
from report import build_report


def main() -> None:
    library = Library(
        [Book(1, "Python入門"), Book(2, "データの扱い方")],
        [Member(1, "田中"), Member(2, "佐藤")],
    )
    library.lend_book(1, 1)
    print(build_report(library))
    library.return_book(1, 1)
    print("\n返却後:")
    print(build_report(library))


if __name__ == "__main__":
    main()
