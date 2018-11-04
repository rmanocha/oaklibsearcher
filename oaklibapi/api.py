import logging

from bs4 import BeautifulSoup
from typing import List

from .exceptions import BranchesNotKnownException
from .utils import get_url

DOMAIN = "http://encore.oaklandlibrary.org/"
SEARCH_URL = DOMAIN + "iii/encore/search/C__S{isbn}__Orightresult__U?lang=eng&suite=cobalt"
AVAILABLE_LIBS_URL = DOMAIN + "{available_libs_url}"

class OaklandLibraryAPI(object):
    def __init__(self, isbn: str):
        self.isbn = isbn
        response = get_url(SEARCH_URL.format(isbn=isbn))
        self.soup = BeautifulSoup(response.content, "lxml")
        self.__verify_results()

    def __verify_results(self) -> bool:
        self.__no_results = self.soup.find('div', {'class': 'tryAgainMessage'}) is not None

    def is_available(self) -> bool:
        if self.__no_results:
            return False
        return self.soup.find('span', {'class': 'itemsAvailable'}) is not None

    def title(self) -> str:
        if self.__no_results:
            return ""
        return self.soup.find('a', id="recordDisplayLink2Component").text.strip()

    def get_libs_available(self) -> List[str]:
        logging.info("Looking for branches for title={}".format(self.title()))
        if self.__no_results:
            return []

        try:
            available_libs_url = self.soup.find('a',
                                    id="showMaxItemsLink2Component").get("href")
        except AttributeError:
            # so far, I've only seen this when there's only one copy of the 
            # book available. In those cases, the "show only available..." 
            # checkbox is not available and neither is the URL. Let's just 
            # exit out of this process for now when that happens
            raise BranchesNotKnownException("Unable to fetch branches")
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
