"""ブックマークのモジュール
"""
from typing import List


class Bookmark:
    def __init__(self, url: str, title: str, tag: List) -> None:
        """初期化

        Args:
            url (str): URL
            title (str): タイトル
            tag (List): タグ

        Examples:
            >>> book = Bookmark(url='test', title='test', tag=['test'])
        """
        self.url = url
        self.title = title
        self.tag = tag


class Bookmarks:
    def __init__(self) -> None:
        """初期化

        Examples:
            >>> books = Bookmarks()
        """
        self.books = []

    def add(self, book: Bookmark) -> None:
        """Bookmarkの追加

        Args:
            book (Bookmark): ブックマーク

        Examples:
            >>> book = Bookmark(url='test', title='test', tag=['test'])
            >>> books.add(book=book)
        """
        is_add = False

        for b in self.books:
            if b.url == book.url:
                is_add = True

                break

        if not is_add:
            self.books.append(book)
