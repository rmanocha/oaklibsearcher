import requests
from bs4 import BeautifulSoup

# For now, the "to-read" shelf is hardcoded
GOODREADS_QUERY_URL = "https://www.goodreads.com/review/list?v=2&key={access_key}&id={user_id}&shelf=to-read"

class GoodreadsQueryAPI(object):
    def __init__(self, user_id, access_key):
        self.user_id = user_id
        self.access_key = access_key # This could be moved to an env var too
        response = requests.get(GOODREADS_QUERY_URL.format(
                                    access_key=access_key, user_id=user_id))
        self.soup = BeautifulSoup(response.content, 'xml')

    
    def get_isbns(self):
        reviews = self.soup('review')
        isbns = []
        for review in reviews:
            isbns.append(GoodreadsBook(review.find('isbn13').text,
                                       review.find('title').text))

            #isbns.append(review.find('isbn13').text)

        return isbns

class GoodreadsBook(object):
    def __init__(self, isbn, title):
        self.isbn = isbn
        self.title = title

    def __str__(self):
        return "{title}<{isbn}>".format(title=self.title, isbn=self.isbn)
