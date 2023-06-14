from revolt.ext import commands
from client import Zorak

import json
import requests


class Quote(commands.Cog[Zorak]):

    @commands.command()
    async def quote(self, ctx):
        quote = json.loads(requests.get("https://zenquotes.io/api/random").text)[0]
        await ctx.send((quote["q"] + "\n- " + quote["a"]))


def setup(client: Zorak):
    client.add_cog(Quote())
