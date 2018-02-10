from oaklibapi import OaklandLibraryAPI
from goodreads_api import GoodreadsQueryAPI

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID

gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY)

books_available = []

for book in gdr.get_books():
    print("Looking for title={}, ISBN={}".format(book['title'], book['isbn']))
    if not book['isbn']:
        print("No ISBN available. Skipping")
        continue

    olib = OaklandLibraryAPI(book['isbn'])
    if olib.is_available():
        books_available.append(olib)

for olib in books_available:
    print("Book with title={} is available".format(olib.title()))
