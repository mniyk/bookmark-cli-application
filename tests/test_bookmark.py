"""bookmark.pyのunittest
"""
import logging
import unittest

import bookmark


logging.basicConfig(
    level=logging.INFO,
    format='\t'.join([
        '%(asctime)s',
        '%(levelname)s',
        '%(filename)s',
        '%(funcName)s',
        '%(processName)s',
        '%(process)d',
        '%(threadName)s',
        '%(thread)d',
        '%(message)s']))
logger = logging.Logger(__name__)


class TestBookmark(unittest.TestCase):
    def test_create_bookmark(self):
        book = bookmark.Bookmark(url='test', title='test', tag=['test'])

        print(book)

    def test_add_bookmarks(self):
        books = bookmark.Bookmarks()

        book1 = bookmark.Bookmark(url='test1', title='test1', tag=['test1'])
        book2 = bookmark.Bookmark(url='test2', title='test2', tag=['test2'])

        books.add(book=book1)
        books.add(book=book1)

        self.assertEqual(len(books.books), 1)

        books.add(book=book2)

        self.assertEqual(len(books.books), 2)
