from revolt.ext import commands
from client import Zorak

from bs4 import BeautifulSoup
import requests


class Taunt(commands.Cog[Zorak]):

    @commands.command()
    async def taunt(self, ctx):
        taunt = BeautifulSoup(
            requests.get(
                "https://fungenerators.com/random/insult/shakespeare/"
            ).content,
            "html.parser",
        ).find("h2")
        await ctx.send(f"{taunt.text}")


def setup(client: Zorak):
    client.add_cog(Taunt())




