from revolt.ext import commands
from zorak import Zorak


class Ping(commands.Cog[Zorak]):

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong")


def setup(client: Zorak):
    client.add_cog(Ping())

