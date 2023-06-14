"""
This module hosts the Zorak class, which is the main instance of our bot.
"""
import revolt
from revolt.ext import commands

from utility.logger import log_info  # pylint: disable=E0401


class Zorak(commands.CommandsClient):
    """
    Upon loading the bot in main, these things are run.
    """
    async def get_prefix(self, message: revolt.Message):
        """
        Sets the prefix to be used in the chat
        ex:
            /command
        """
        return "/"

    async def on_ready(self):
        """
        Only called when the bot is finished loading and ready to take commands
        """
        log_info(f"{self.user.name} is ready to destroy the planet.")
        await self.edit_status(
            presence=revolt.PresenceType.online
            , text="I'm watching you."
        )
