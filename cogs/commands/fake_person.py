"""
Command: /fakeperson
Description: Sends a profile for a fake person
"""
import json
import requests
from revolt.ext import commands

from client import Zorak  # pylint: disable=E0401


class FakePerson(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def fakeperson(self, ctx):
        """
        Can always add more info from the request.
        Lots more info available.
        """
        person = json.loads(requests.get(
            "https://randomuser.me/api/"
            , timeout=5
        ).text)["results"]
        name = f'Name: {person[0]["name"]["title"]} \
                       {person[0]["name"]["first"]} \
                       {person[0]["name"]["last"]}'
        hometown = f'Hometown: {person[0]["location"]["city"]} \
                             , {person[0]["location"]["country"]}'
        age = f'Age: {person[0]["dob"]["age"]} Years old'
        await ctx.send(
            "You have requested a fake person:\n\n"
            + name
            + "\n"
            + hometown
            + "\n"
            + age
        )


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(FakePerson())
