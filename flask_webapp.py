from flask import Flask, jsonify

from oaklibapi import OaklandLibraryAPI
from goodreads_api import GoodreadsQueryAPI

import logging

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID

app = Flask(__name__)

@app.route("/available_books")
def get_available_books():
    gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY)
    books_available = []

    for book in gdr.get_books()[:5]:
        logging.info("Looking for title={}, ISBN={}".format(
                                            book['title'], book['isbn']))
        if not book['isbn']:
            logging.warn("No ISBN available. Skipping")
            continue

        olib = OaklandLibraryAPI(book['isbn'])
        books_available.append({
            "isbn": book['isbn'],
            "title": olib.title(),
            "available": olib.is_available(),
            "branches": olib.get_libs_available() if olib.is_available() else []
        })


    return jsonify(books_available)

