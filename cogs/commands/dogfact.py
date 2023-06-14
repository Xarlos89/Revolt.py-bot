from revolt.ext import commands
from client import Zorak

import json
import requests


class DogFact(commands.Cog[Zorak]):

    @commands.command()
    async def dogfact(self, ctx):
        try:
            # This URL seems to be offline... not sure why.
            await ctx.send(
                json.loads(requests.get("https://dog-api.kinduff.com/api/facts").text)[
                    "facts"
                ][0]
            )
        except requests.exceptions.ConnectionError as e:
            await ctx.send("No response")


def setup(client: Zorak):
    client.add_cog(DogFact())