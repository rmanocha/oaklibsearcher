from flask import Flask, jsonify, request

from oaklibapi import OaklandLibraryAPI, BranchesNotKnownException
from goodreads_api import GoodreadsQueryAPI

import logging

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID

app = Flask(__name__)

@app.route("/available_books")
def get_available_books(request):
    gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY)
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


    return jsonify(books_available)

