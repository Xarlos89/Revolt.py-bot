"""
Command: /roll
Description: rolls a 6 sided die
"""
from random import choice
from revolt.ext import commands

from client import Zorak  # pylint: disable=E0401


class Roll(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def roll(self, ctx):
        """
        Rolls a die, and displays the result
        """
        await ctx.send(f"**{ctx.author.name}** rolled a **{choice(range(1,7))}**")


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(Roll())
