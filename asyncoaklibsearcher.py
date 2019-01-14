import aiohttp
import asyncio
import logging
import datetime

from oaklibapi import OaklandLibraryAPI, BranchesNotKnownException, BookNotFoundException
from goodreads_api import GoodreadsQueryAPI

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID

gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY, 10)

gdr.get_books()

async def print_book_data(book, session):
    start = datetime.datetime.now()
    log_str = "title={}, ISBN={}".format(book['title'], book['isbn'])
    logging.info("Looking for {}".format(log_str))

    if not book['isbn']:
        logging.warn("No ISBN available. Skipping")
        return {}

    olib = OaklandLibraryAPI(session, book['isbn'])
    try:
        olib = await olib.get_book()
    except BookNotFoundException:
        olib = None
    #book_data = {
    #    "isbn": book['isbn'],
    #    "title": olib.title(),
    #    "available": olib.is_available(),
    #}
    #logging.info("About to sleep for 2 seconds")
    #await asyncio.sleep(2)
    #if not olib.is_available():
    #    logging.info("title={} not available".format(book['title']))

    #try:
    #    book_data["branches"] = olib.get_libs_available() if \
    #                                            olib.is_available() else []
    #except BranchesNotKnownException:
    #    book_data["branches"] = ["Unable to retrieve branches"]

    end = datetime.datetime.now()
    logging.info("Time take for {} was {}".format(log_str, end - start))
    return olib

async def main():
    values = []
    
    async with aiohttp.ClientSession() as session:
        for book in gdr.get_books():
            values.append(asyncio.create_task(print_book_data(book, session)))

        for value in values:
            #print(await value)
            print(await value)

logging.info("Time with full asyncio")
start = datetime.datetime.now()
asyncio.run(main())
end = datetime.datetime.now()
logging.info("Time spent={}".format(end - start))

