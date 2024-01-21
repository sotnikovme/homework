"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_json(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            user_data = await response.json()
            keys = ["name", "username", "email"]
            users_data = []
            for user in user_data:
                users_dict = {}
                for key, value in user.items():
                    if key in keys:
                        users_dict[key] = value
                users_data.append(users_dict)
                return users_data

            return 
async def fetch_users():
    data = fetch_json(USERS_DATA_URL)
    return data

async def fetch_posts():
    data = fetch_json(USERS_DATA_URL)
    return data


# async def main():
#     configure_logging()
#     result = await fetch_json(USERS_DATA_URL)
#     result = await fetch_json(POSTS_DATA_URL)
#     log.info("got result %s", result)

#if  __name__ == "__main__":
#    asyncio.run(main())
