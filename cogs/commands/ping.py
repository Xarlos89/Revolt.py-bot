"""
Command: /ping
Description: Pongs back, mostly just to test connectivity
"""
from revolt.ext import commands

from client import Zorak  # pylint: disable=E0401


class Ping(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def ping(self, ctx: commands.Context):
        """
        This message satisfies the linter.
        It's a ping, what more do you want?
        """
        await ctx.send("pong")


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(Ping())
