from revolt.ext import commands
from client import Zorak

import json
import requests


class FakePerson(commands.Cog[Zorak]):

    @commands.command()
    async def fakeperson(self, ctx):
        person = json.loads(requests.get("https://randomuser.me/api/").text)["results"]
        name = "Name: {} {} {}".format(
            person[0]["name"]["title"],
            person[0]["name"]["first"],
            person[0]["name"]["last"],
        )
        hometown = "Hometown: {}, {}".format(
            person[0]["location"]["city"], person[0]["location"]["country"]
        )
        age = "Age: {} Years old".format(person[0]["dob"]["age"])
        await ctx.send(
            "You have requested a fake person:\n\n"
            + name
            + "\n"
            + hometown
            + "\n"
            + age
        )


def setup(client: Zorak):
    client.add_cog(FakePerson())
