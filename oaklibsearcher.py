import asyncio
import logging
import datetime

from oaklibapi import OaklandLibraryAPI, BranchesNotKnownException
from goodreads_api import GoodreadsQueryAPI

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID

gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY)

async def print_book_data(book):
    logging.info("Looking for title={}, ISBN={}".format(
                                            book['title'], book['isbn']))
    if not book['isbn']:
        logging.warn("No ISBN available. Skipping")
        return {}

    olib = OaklandLibraryAPI(book['isbn'])
    book_data = {
        "isbn": book['isbn'],
        "title": olib.title(),
        "available": olib.is_available(),
    }
    if not olib.is_available():
        logging.info("title={} not available".format(book['title']))

    try:
        book_data["branches"] = olib.get_libs_available() if \
                                                olib.is_available() else []
    except BranchesNotKnownException:
        book_data["branches"] = ["Unable to retrieve branches"]

    return book_data

    #logging.info("Looking for title={}, ISBN={}".format(book['title'], book['isbn']))
    #if not book['isbn']:
    #    return "No ISBN available. Skipping"

    #olib = OaklandLibraryAPI(book['isbn'])
    #logging.info("Done searching for title={}".format(olib.title()))

    #return "Book with title={} is {}".format(olib.title(), 
    #    "available" if olib.is_available() else "not available")

async def main():
    values = []
    for book in gdr.get_books():
        values.append(asyncio.create_task(print_book_data(book)))

    for value in values:
        print(await value)

async def main_regular():
    for book in gdr.get_books():
        print(await print_book_data(book))

start = datetime.datetime.now()
#asyncio.run(main())
asyncio.run(main_regular())
end = datetime.datetime.now()
print(end - start)
