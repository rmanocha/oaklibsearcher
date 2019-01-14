import logging
import aiohttp
import asyncio

async def fetch_url(session, url):
    logging.debug("Fetching URL={}".format(url))
    async with session.get(url) as response:
        return await response.text()
