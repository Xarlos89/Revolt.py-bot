"""
Command: /dogfact
Description: Sends a fantastic dog fact.
"""
import json
import requests
from revolt.ext import commands

from client import Zorak  # pylint: disable=E0401


class DogFact(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def dogfact(self, ctx):
        """
        We have an exception for when the API is down.
        """
        try:
            # This URL seems to be offline... not sure why.
            await ctx.send(
                json.loads(requests.get(
                    "https://dog-api.kinduff.com/api/facts"
                    , timeout=5
                ).text)["facts"][0]
            )
        except requests.exceptions.ConnectionError as conn_error:
            await ctx.send("No response", conn_error)


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(DogFact())
