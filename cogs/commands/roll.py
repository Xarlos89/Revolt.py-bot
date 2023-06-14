from revolt.ext import commands
from client import Zorak

from random import choice


class Roll(commands.Cog[Zorak]):

    @commands.command()
    async def roll(self, ctx):
        await ctx.send(f"**{ctx.author.name}** rolled a **{choice(range(1,7))}**")


def setup(client: Zorak):
    client.add_cog(Roll())
