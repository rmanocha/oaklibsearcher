from flask import Flask, jsonify, request

from oaklibapi import OaklandLibraryAPI, BranchesNotKnownException
from goodreads_api import GoodreadsQueryAPI

import datetime
import logging

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID, GOODREADS_COUNT

from werkzeug.contrib.atom import AtomFeed

app = Flask(__name__)

def get_books_branches():
    gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY,
                            GOODREADS_COUNT)
    books_available = []

    for book in gdr.get_books():
        logging.info("Looking for title={}, ISBN={}".format(
                                            book['title'], book['isbn']))
        if not book['isbn']:
            logging.warn("No ISBN available. Skipping")
            continue

        olib = OaklandLibraryAPI(book['isbn'])
        book_data = {
            "isbn": book['isbn'],
            "title": olib.title(),
            "available": olib.is_available(),
        }
        try:
            book_data["branches"] = olib.get_libs_available() if \
                                                    olib.is_available() else []
        except BranchesNotKnownException:
            book_data["branches"] = ["Unable to retrieve branches"]

        books_available.append(book_data)

    return books_available

@app.route("/available_books")
def get_available_books():
    return jsonify(get_books_branches())

@app.route("/available_books.atom")
def get_available_books_rss():
    books_available = get_books_branches()

    feed = AtomFeed("Available Books", feed_url=request.url,
            url=request.url_root)
    for book in books_available:
        if book["available"]:
            content = "{} (isbn={}) is available at {}".format(book["title"],
                    book["isbn"], ",".join(book["branches"]))
            feed.add(book["title"], content, updated=datetime.datetime.now(),
                    url=request.url_root + book["isbn"], content_type="text")

    return feed.get_response()
