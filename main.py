import asyncio
import aiohttp
import os
import sys
from utility.logger import *
from client import Zorak


def load_key():
    """
    Loads the bot key as the first arg when running the bot OR from an env variable.
    For example:
        "python __main__.py BOT_TOKEN_HERE"
    """
    if len(sys.argv) > 1:  # Check args for the token first
        token = sys.argv[1]
        log_info('Loading Token from arg.')
        return token

    elif os.environ['TOKEN'] is not None:  # if not in args, check the env vars
        log_info('Loading Token from environment variable.')
        return os.environ['TOKEN']

    else:
        log_info('ERROR: You must include a bot token.')
        log_info('Example: "python __main__.py BOT_TOKEN_GOES_HERE"')


async def main():
    async with aiohttp.ClientSession() as session:
        client = Zorak(session, load_key())
        await client.start()

asyncio.run(main())

