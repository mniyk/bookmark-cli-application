"""メイン処理
"""
import argparse
import os
import webbrowser

import bookmark


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', action='store_true')
    parser.add_argument('--list', action='store_true')
    parser.add_argument('-p', '--path', required=True)
    parser.add_argument('-u', '--url')
    parser.add_argument('-t', '--title')
    parser.add_argument('--tag')
    args = parser.parse_args()
    
    books = bookmark.Bookmarks()

    if os.path.isfile(args.path):
        books.read_json(args.path)

    if args.add:
        if args.url and args.title:
            if args.tag:
                tag = args.tag.split(',')
            else:
                tag = []

            book = bookmark.Bookmark(url=args.url, title=args.title, tag=tag)
            books.add(book=book)

        books.output(args.path)
    elif args.list:
        for i, book in enumerate(books.books, start=1):
            print(
                f'{i:<3} -> URL:{book.url} TITLE:{book.title}, TAG:{book.tag}')

        processing_number = int(
            input('Input processin number(0=exit, 1=open, 2=delete): '))

        if processing_number == 1:
            target = int(input('Input open bookmark number(0=exit): '))

            if target > 0:
                webbrowser.open(books.books[target - 1].url)
        elif processing_number == 2:
            target = int(input('Input delet bookmark number(0=exit): '))

            if target > 0:
                books.delete(url=books.books[target - 1].url)

                books.output(args.path)


if __name__ == '__main__':
    main()
