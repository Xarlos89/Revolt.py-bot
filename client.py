import revolt
from revolt.ext import commands
import pathlib
import os

from utility.logger import *


class Zorak(commands.CommandsClient):
    async def get_prefix(self, message: revolt.Message):
        return "/"

    async def on_ready(self):
        log_info(f"{self.user.name} is ready to destroy the planet.")
        await self.edit_status(presence=revolt.PresenceType.online, text="I'm watching you.")


