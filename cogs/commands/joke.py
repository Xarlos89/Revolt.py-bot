"""
Command: /joke
Description: Tells a joke
"""
import json
import requests
from revolt.ext import commands

from client import Zorak  # pylint: disable=E0401


class Joke(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def joke(self, ctx):
        """
        Tells a not-so-funny joke.
        """
        await ctx.send(
            json.loads(
                requests.get(
                    "https://geek-jokes.sameerkumar.website/api?format=json"
                    , timeout=5
                ).text
            )["joke"]
        )


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(Joke())
