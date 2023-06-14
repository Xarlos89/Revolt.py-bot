"""
Command: /catfact
Description: Sends a fantastic cat fact.
"""
import json
import requests
from revolt.ext import commands

from client import Zorak #pylint: disable=E0401




class CatFact(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """
    @commands.command()
    async def catfact(self, ctx):
        """
        We have an exception for when the API is down.
        """
        try:
            await ctx.send(
                json.loads(requests.get(
                    "https://catfact.ninja/fact"
                    , timeout=5
                ).text)["fact"]
            )
        except requests.exceptions.ConnectionError as conn_error:
            await ctx.send("No response", conn_error)


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(CatFact())
