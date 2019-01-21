import aiohttp
import asyncio
from quart import Quart, jsonify, request, Response

from oaklibapi import OaklandLibraryAPI, BranchesNotKnownException, BookNotFoundException
from goodreads_api import GoodreadsQueryAPI

import datetime
import logging

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID, GOODREADS_COUNT

from werkzeug.contrib.atom import AtomFeed

app = Quart(__name__)

async def print_book_data(book, session):
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

    return olib

async def get_books_branches():
    gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY,
                            GOODREADS_COUNT)
    values = []
    books_available = []

    async with aiohttp.ClientSession() as session:
        for book in gdr.get_books():
            values.append(asyncio.create_task(print_book_data(book, session)))

        for value in values:
            books_available.append(await value)

    return books_available

@app.route("/oaklibatom/available_books")
async def get_available_books():
    books = await get_books_branches()
    ret_books = []
    for book in books:
        if book:
            ret_books.append({"title": book.title, "isbn": book.isbn, "branches": book.branches})
    return jsonify(ret_books)

@app.route("/oaklibatom/available_books.atom")
async def get_available_books_rss():
    books_available = await get_books_branches()

    feed = AtomFeed("Available Books",
            feed_url=request.url_root + "oaklibatom/available_books.atom",
            url=request.url_root)
    for book in books_available:
        if book and book.branches:
            content = "{} (isbn={}) is available at {}".format(book.title,
                    book.isbn, ",".join(book.branches))
            feed.add(book.title, content, updated=datetime.datetime.now(),
                    url=request.url_root + book.isbn, content_type="text")

    return Response(response=feed.to_string(), mimetype="application/atom+xml")
