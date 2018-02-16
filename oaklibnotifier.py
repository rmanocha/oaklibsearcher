from oaklibapi import OaklandLibraryAPI
from goodreads_api import GoodreadsQueryAPI

import logging
import smtplib

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID, \
        NOTIFICATIONS_COUNT, NOTIFICATION_RECIPIENT, \
        NOTIFICATION_SENDER_USER, NOTIFICATION_SENDER_PASS

NOTIFICATION_SUBJECT = "Books available at Oakland Library"

gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY)

books_available = []

for book in gdr.get_books():
    logging.info("Looking for title={}, ISBN={}".format(
                                                book['title'], book['isbn']))
    if not book['isbn']:
        logging.warn("No ISBN available. Skipping")
        continue

    olib = OaklandLibraryAPI(book['isbn'])
    if olib.is_available():
        books_available.append(olib)

    if len(books_available) >= NOTIFICATIONS_COUNT:
        break

notification_message = ""

for olib in books_available:
    msg = "Book with title={} is available".format(olib.title())
    logging.info(msg)
    notification_message += msg + "\n"

if notification_message:
    email_msg = "Subject: {}\n\n{}".format(NOTIFICATION_SUBJECT, notification_message)

    logging.debug("Connecting to gmail")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(NOTIFICATION_SENDER_USER, NOTIFICATION_SENDER_PASS)
    logging.debug("Connected to gmail")

    logging.debug("Sending email")
    server.sendmail(NOTIFICATION_SENDER_USER, NOTIFICATION_RECIPIENT, 
            email_msg)
    server.quit()
    logging.info("Email sent")
