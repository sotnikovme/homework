"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio
import logging
import aiohttp
from aiohttp import ClientSession
from homework_04.common import configure_logging

log = logging.getLogger(__name__)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/"
POSTS_DATA_URL = "https://github.com/typicode/xv.git"

async def fetch_json(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data

async def main():
    configure_logging()
    result = await fetch_json(USERS_DATA_URL)
    result = await fetch_json(POSTS_DATA_URL)
    log.info("got result %s", result)

if  __name__ == "__main__":
    asyncio.run(main())
