"""
Command: /taunt
Description: Sends a classical shakespearian taunt
"""
import requests
from bs4 import BeautifulSoup
from revolt.ext import commands

from client import Zorak  # pylint: disable=E0401


class Taunt(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def taunt(self, ctx):
        """
        Sends a taunt that we scrape using bs4
        """
        taunt = BeautifulSoup(
            requests.get(
                "https://fungenerators.com/random/insult/shakespeare/"
                , timeout=5
            ).content,
            "html.parser",
        ).find("h2")
        await ctx.send(f"{taunt.text}")


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(Taunt())
