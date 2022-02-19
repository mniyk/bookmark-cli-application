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
