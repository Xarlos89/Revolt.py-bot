"""
Command: /google
Description: Sarcastically googles something
"""
from revolt.ext import commands

from client import Zorak  # pylint: disable=E0401


class Google(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """

    @commands.command()
    async def google(self, ctx, *question):
        """
        Just sends a sarcastic link.
        """
        await ctx.send(
            f"Here, allow me to google that one for you: \
            \nhttps://letmegooglethat.com/?q={'+'.join(question)}"
        )


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(Google())
