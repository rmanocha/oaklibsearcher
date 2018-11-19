import asyncio
import logging
import datetime

from oaklibapi import OaklandLibraryAPI, BranchesNotKnownException
from goodreads_api import GoodreadsQueryAPI

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID

gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY, 10)

async def print_book_data(book):
    start = datetime.datetime.now()
    log_str = "title={}, ISBN={}".format(book['title'], book['isbn'])
    logging.info("Looking for {}".format(log_str))

    if not book['isbn']:
        logging.warn("No ISBN available. Skipping")
        return {}

    olib = OaklandLibraryAPI(book['isbn'])
    book_data = {
        "isbn": book['isbn'],
        "title": olib.title(),
        "available": olib.is_available(),
    }
    logging.info("About to sleep for 2 seconds")
    await asyncio.sleep(2)
    if not olib.is_available():
        logging.info("title={} not available".format(book['title']))

    try:
        book_data["branches"] = olib.get_libs_available() if \
                                                olib.is_available() else []
    except BranchesNotKnownException:
        book_data["branches"] = ["Unable to retrieve branches"]

    end = datetime.datetime.now()
    logging.info("Time take for {} was {}".format(log_str, end - start))
    return book_data

async def main():
    values = []
    for book in gdr.get_books():
        values.append(asyncio.create_task(print_book_data(book)))

    for value in values:
        #print(await value)
        await value

async def main_regular():
    for book in gdr.get_books():
        await print_book_data(book)

gdr.get_books()
logging.info("Time with full asyncio")
start = datetime.datetime.now()
asyncio.run(main())
end = datetime.datetime.now()
logging.info("Time spent={}".format(end - start))

logging.info("Time without asyncio")
start = datetime.datetime.now()
asyncio.run(main_regular())
end = datetime.datetime.now()
logging.info("Time spent={}".format(end - start))
