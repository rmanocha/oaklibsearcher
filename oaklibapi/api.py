import logging

import aiohttp
from bs4 import BeautifulSoup
from typing import List

from .exceptions import BranchesNotKnownException, BookNotFoundException
from .utils import fetch_url

DOMAIN = "http://encore.oaklandlibrary.org/"
SEARCH_URL = DOMAIN + "iii/encore/search/C__S{isbn}__Orightresult__U?lang=eng&suite=cobalt"
AVAILABLE_LIBS_URL = DOMAIN + "{available_libs_url}"

class LibBook(object):
    def __init__(self, isbn: str, title: str, branches: List[str]):
        self.isbn = isbn
        self.title = title
        self.branches = branches

    def __str__(self):
        return "Title={} with ISBN={} available at {} branches".format(
                self.title, self.isbn, len(self.branches))

class OaklandLibraryAPI(object):
    def __init__(self, session: aiohttp.ClientSession, isbn: str):
        self.isbn = isbn
        self.session = session

    async def get_book(self) -> LibBook:
        html = await fetch_url(self.session, SEARCH_URL.format(isbn=self.isbn))
        self.soup = BeautifulSoup(html, "lxml")
        self.__verify_results()
        if self.__no_results:
            raise BookNotFoundException("ISBN: {}".format(self.isbn))

        try:
            branches = await self.__get_libs_available()
        except BranchesNotKnownException:
            branches = []

        return LibBook(self.isbn, self.__get_title(), branches)

    def __verify_results(self):
        self.__no_results = self.soup.find('div', {'class': 'tryAgainMessage'}) is not None

    def __get_title(self) -> str:
        if self.__no_results:
            return ""
        return self.soup.find('a', id="recordDisplayLink2Component").text.strip()

    async def __get_libs_available(self) -> List[str]:
        logging.info("Looking for branches for title={}".format(self.__get_title()))
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
                await fetch_url(self.session, AVAILABLE_LIBS_URL.format(
                            available_libs_url=available_libs_url)),
                "lxml")

        available_lib_names = []
        try:
            for tr in available_libs.find('table', {'class': 'itemTable'}). \
                                                                findAll('tr')[1:]:
                lib_name_td = tr.find('td')
                available_lib_names.append(lib_name_td.text.strip())
        except AttributeError: #TODO: Understand why this happens. Was happening for "Grant"
            raise BranchesNotKnownException("Unable to fetch branches")
        return available_lib_names

