"""bookmark.pyのunittest
"""
import logging
import os
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
    def setUp(self) -> None:
        self.books = bookmark.Bookmarks()

        self.book1 = bookmark.Bookmark(
            url='test1', title='test1', tag=['test1'])
        self.book2 = bookmark.Bookmark(
            url='test2', title='test2', tag=['test2'])


    def test_create_bookmark(self):
        book = bookmark.Bookmark(url='test', title='test', tag=['test'])

        print(book)

    def test_add_bookmarks(self):
        self.books.add(book=self.book1)
        self.books.add(book=self.book1)

        self.assertEqual(len(self.books.books), 1)

        self.books.add(book=self.book2)

        self.assertEqual(len(self.books.books), 2)

    def test_delete_bookmarks(self):
        self.books.add(book=self.book1)
        self.books.add(book=self.book2)

        self.assertEqual(len(self.books.books), 2)

        self.books.delete(url='test1')

        self.assertEqual(len(self.books.books), 1)

    def test_output_bookmarks(self):
        self.books.add(book=self.book1)
        self.books.add(book=self.book2)

        self.books.output('bookmarks.json')

        os.remove('bookmarks.json')


    def test_read_json(self):
        self.books.add(book=self.book1)
        self.books.add(book=self.book2)

        self.books.output('bookmarks.json')

        self.books.read_json('bookmarks.json')

        self.assertEqual(len(self.books.books), 2)

        os.remove('bookmarks.json')
