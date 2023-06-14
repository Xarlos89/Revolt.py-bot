"""
Command: /eightball [question]
Description: Asks a magic 8ball a question, and returns an answer
"""
from random import choice
from revolt.ext import commands

from client import Zorak #pylint: disable=E0401


class EightBall(commands.Cog[Zorak]):
    """
    Hosts only the 1 command.
    """
    @commands.command()
    async def eightball(self, ctx, *question):
        """
        Currently uses Kwargs, must be a better way.
        """
        answer = choice(
            [
                "It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs points to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not to tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good",
                "Very doubtful.",
                "Be more polite.",
                "How would i know",
                "100%",
                "Think harder",
                "Sure",
                "In what world will that ever happen",
                "As i see it no.",
                "No doubt about it",
                "Focus",
                "Unfortunately yes",
                "Unfortunately no,",
                "Signs point to no",
            ]
        )
        await ctx.send(f"Question: {' '.join(question)}\n🎱 - {answer}")


def setup(client: Zorak):
    """
    Loads the cog into the Client (Zorak)
    """
    client.add_cog(EightBall())
