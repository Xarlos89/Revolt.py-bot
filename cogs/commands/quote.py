"""
Command: /quote
Description: Sends an inspiring quote
"""
import json
import requests

from revolt.ext import commands
from client import Zorak  # pylint: disable=E0401


class Quote(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def quote(self, ctx):
        """
        Sends a quote from zenquotes
        """
        quote = json.loads(
            requests.get(
                "https://zenquotes.io/api/random"
                , timeout=5
            ).text)[0]
        await ctx.send((quote["q"] + "\n- " + quote["a"]))


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(Quote())
