from bs4 import BeautifulSoup

from .utils import get_url

DOMAIN = "http://encore.oaklandlibrary.org/"
SEARCH_URL = DOMAIN + "iii/encore/search/C__S{isbn}__Orightresult__U?lang=eng&suite=cobalt"
AVAILABLE_LIBS_URL = DOMAIN + "{available_libs_url}"

class OaklandLibraryAPI(object):
    def __init__(self, isbn):
        self.isbn = isbn
        response = get_url(SEARCH_URL.format(isbn=isbn))
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

    def get_libs_available(self):
        if self.__no_results:
            return []

        available_libs_url = self.soup.find('a', 
                                id="showMaxItemsLink2Component").get("href")
        available_libs = BeautifulSoup(
                get_url(AVAILABLE_LIBS_URL.format(
                            available_libs_url=available_libs_url)).content,
                "lxml")

        available_lib_names = []
        for tr in available_libs.find('table', {'class': 'itemTable'}). \
                                                            findAll('tr')[1:]:
            lib_name_td = tr.find('td')
            available_lib_names.append(lib_name_td.text.strip())
        return available_lib_names
        
