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
            >>> Bookmark(url='test', title='test', tag=['test'])
        """
        self.url = url
        self.title = title
        self.tag = tag


class Bookmarks:
    def __init__(self) -> None:
        books = None
