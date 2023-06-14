from revolt.ext import commands
from client import Zorak


class Google(commands.Cog[Zorak]):

    @commands.command()
    async def google(self, ctx, *question):
        await ctx.send(
            f"Here, allow me to google that one for you:\nhttps://letmegooglethat.com/?q={'+'.join(question)}"
        )


def setup(client: Zorak):
    client.add_cog(Google())
