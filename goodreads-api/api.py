import requests
from bs4 import BeautifulSoup

# For now, the "to-read" shelf is hardcoded
GOODREADS_QUERY_URL = "https://www.goodreads.com/review/list?v=2&key={access_key}&id={user_id}&shelf=to-read&per_page=200"

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
            isbns.append({'isbn': review.find('isbn13').text,
                          'title': review.find('title').text})

        return isbns
