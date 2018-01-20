import requests
from bs4 import BeautifulSoup

DOMAIN = "http://encore.oaklandlibrary.org/"
SEARCH_URL = DOMAIN + "iii/encore/search/C__S{isbn}__Orightresult__U?lang=eng&suite=cobalt"

class OaklandLibraryAPI(object):
    def __init__(self, isbn):
        self.isbn = isbn
        response = requests.get(SEARCH_URL.format(isbn=isbn))
        self.soup = BeautifulSoup(response.content, "lxml")
        self.__verify_results()

    def __verify_results(self):
        self.__no_results = self.soup.find('div', {'class': 'tryAgainMessage'}) is not None

    def is_available(self):
        if self.__no_results:
            return False
        return self.soup.find('span', {'class': 'itemsAvailable'}) is not None

    def title(self):
        if self.__no_results:
            return ""
        return self.soup.find('a', id="recordDisplayLink2Component").text.strip()
