from revolt.ext import commands
from client import Zorak

import json
import requests


class CatFact(commands.Cog[Zorak]):

    @commands.command()
    async def catfact(self, ctx):
        try:
            await ctx.send(
                json.loads(requests.get("https://catfact.ninja/fact").text)["fact"]
            )
        except requests.exceptions.ConnectionError as e:
            await ctx.send("No response")


def setup(client: Zorak):
    client.add_cog(CatFact())

