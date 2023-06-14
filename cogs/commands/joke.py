from revolt.ext import commands
from client import Zorak

import json
import requests


class Joke(commands.Cog[Zorak]):

    @commands.command()
    async def joke(self, ctx):
        await ctx.send(
            json.loads(
                requests.get(
                    "https://geek-jokes.sameerkumar.website/api?format=json"
                ).text
            )["joke"]
        )


def setup(client: Zorak):
    client.add_cog(Joke())
