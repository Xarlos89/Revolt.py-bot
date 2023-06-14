"""
Our main file, and entrypoint for the bot.
Here we load the token either in an arg or an env-var,
and then we run our bot.
"""
import os
import sys
import asyncio
import aiohttp

from utility.logger import log_debug, log_info, log_critical  # pylint: disable=E0401
from client import Zorak  # pylint: disable=E0401


async def main():
    """
    Main function, loads cogs, then starts the bot.
    """
    async with aiohttp.ClientSession() as session:
        client = Zorak(session, load_key())
        load_extensions(client)
        await client.start()


def load_extensions(bot):
    """
    This function reads through the directory tree in /cogs and
    loads every .py file it finds in there.
    """
    log_info("Loading Cogs...")

    for directory in os.listdir("./cogs"):
        if not directory.startswith("_"):  # Makes sure __innit.py__ doesnt get called
            for file in os.listdir(f"./cogs/{directory}"):
                if file.endswith('.py') and not file.startswith('__init__'):
                    log_debug(f"Loading Cog: \\{directory}\\{file}")
                    bot.load_extension(f"cogs.{directory}.{file[:-3]}")

    log_info(" - Success.")


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

    if os.environ['TOKEN'] is not None:  # if not in args, check the env vars
        log_info('Loading Token from environment variable.')
        return os.environ['TOKEN']

    log_critical('ERROR: You must include a bot token.')
    log_info('Example: "python __main__.py BOT_TOKEN_GOES_HERE"')



asyncio.run(main())
