from library import Library


def build_report(library: Library) -> str:
    lines = ["図書館の本:"]
    for book in library.books:
        if book.borrower_id is None:
            lines.append(f"{book.book_id}: {book.title} [貸出可能]")
        else:
            member = None
            for candidate in library.members:
                if candidate.member_id == book.borrower_id:
                    member = candidate
                    break
            if member is None:
                raise ValueError("会員が見つかりません")
            lines.append(f"{book.book_id}: {book.title} [貸出中: {member.name}]")
    return "\n".join(lines)


# TODO: Libraryと重複する会員検索を、整理後の共通処理で置き換える。
