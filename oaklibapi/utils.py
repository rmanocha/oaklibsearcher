import logging
import requests

def get_url(url):
    logging.debug("Fetching URL={}".format(url))
    return requests.get(url)

