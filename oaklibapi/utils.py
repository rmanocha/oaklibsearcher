import logging
import requests

def get_url(url):
    logging.info("Fetching URL={}".format(url))
    return requests.get(url)

