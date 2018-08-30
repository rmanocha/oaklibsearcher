from oaklibapi import OaklandLibraryAPI
from goodreads_api import GoodreadsQueryAPI

import logging
import smtplib

from settings import GOODREADS_ACCESS_KEY, GOODREADS_USER_ID, \
        NOTIFICATIONS_COUNT, NOTIFICATION_RECIPIENT, \
        NOTIFICATION_SENDER_USER, NOTIFICATION_SENDER_PASS

NOTIFICATION_SUBJECT = "Books available at Oakland Library"

class CheckNotifyBooks(object):
    def __init__(self):
        self.gdr = GoodreadsQueryAPI(GOODREADS_USER_ID, GOODREADS_ACCESS_KEY)
        self.books_available = []

    def check_books(self):
        for book in self.gdr.get_books():
            logging.info("Looking for title={}, ISBN={}".format(
                                                book['title'], book['isbn']))
            if not book['isbn']:
                logging.warn("No ISBN available. Skipping")
                continue

            olib = OaklandLibraryAPI(book['isbn'])
            if olib.is_available():
                self.books_available.append(olib)

            if len(self.books_available) >= NOTIFICATIONS_COUNT:
                break

    def notify_user(self):
        # each time this is called, check for books
        self.check_books()
        if not self.books_available:
            return

        notification_message = ""

        for olib in self.books_available:
            msg = "Book with title={} is available at {}".format(olib.title(),
                    ", ".join(olib.get_libs_available()))
            logging.info(msg)
            notification_message += msg + "\n"

        if notification_message:
            email_msg = "Subject: {}\n\n{}".format(NOTIFICATION_SUBJECT,
                                                        notification_message)

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

if __name__=="__main__":
    cnb = CheckNotifyBooks()
    cnb.notify_user()
