# from time import time
# import requests
#
#
# def get_file(url):
#     r = requests.get(url, allow_redirects=True)
#     return r
#
#
# def write_file(response):
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:
#         file.write(response.content)
#
#
# def main():
#     t0 = time()
#
#     url = 'https://loremflickr.com/320/240'
#
#     for i in range(10):
#         write_file(get_file(url))
#
#     print(time() - t0)
#
#
# if __name__ == '__main__':
#     main()
#
# 5 seconds

##################################################################################################

import asyncio
import aiohttp


async def fetch_content(url, session):
    async with session.get(url, allow_redirect=True) as response:
        data = await response.read()
