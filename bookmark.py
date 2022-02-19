"""ブックマークのモジュール
"""
import json
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
        is_add = True

        for b in self.books:
            if b.url == book.url:
                is_add = False

                break

        if is_add:
            self.books.append(book)

    def delete(self, url: str):
        """Bookmarkの削除

        Args:
            url (str): URL

        Examples:
            >>> books.delete(url='test')
        """
        is_delete = False
        target = None

        for i, b in enumerate(self.books):
            if b.url == url:
                is_delete = True
                target = i

                break
        
        if is_delete:
            self.books.pop(target)

    def output(self, path: str):
        """Bookmarksの出力

        Args:
            path (str): 出力先パス

        Examples:
            >>> books.output('bookmarks.json')
        """
        books = [
            {'url': book.url, 'title': book.title, 'tag': book.tag} 
            for book in self.books]

        with open(path, 'w') as f:
            json.dump(books, f, indent=4, ensure_ascii=False)

    def read_json(self, path: str):
        """BookmatksのJSONファイルを読み込み

        Args:
            path (str): 読込元パス

        Examples:
            >>> books.read_json('bookmarks.json')
        """
        with open(path, 'r') as f:
            data = json.load(f)

        self.books = [
            Bookmark(url=book['url'], title=book['title'], tag=book['tag'])
            for book in data]
