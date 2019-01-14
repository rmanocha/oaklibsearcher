from oaklibapi import OaklandLibraryAPI
from goodreads_api import GoodreadsQueryAPI

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID

gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY)

for book in gdr.get_books():
    print("Looking for title={}, ISBN={}".format(book['title'], book['isbn']))
    if not book['isbn']:
        print("No ISBN available. Skipping")
        continue

    olib = OaklandLibraryAPI(book['isbn'])
    print("Book with title={} is {}".format(olib.title(), 
        "available" if olib.is_available() else "not available"))
