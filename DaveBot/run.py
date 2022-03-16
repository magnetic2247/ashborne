from discord.ext import commands
from Voice import Voice
from dotenv import load_dotenv
from os import getenv

load_dotenv()  # Adds .env to memory
bot_name = "Dave Mustaine"


class Emman(commands.Bot):
    """Startup Client for Bot."""

    def __init__(self, **options):
        # Set to True if running a test bot.
        super().__init__(**options)

    def start_up(self):
        # Add all cogs
        self.add_cogs()

    def add_cogs(self):
        """Add the cogs to the bot client."""
        self.add_cog(Voice(self))


if __name__ == '__main__':
    emman_bot = Emman(command_prefix="*", case_insensitive=True)
    emman_bot.start_up()
    print(f"Logging in as {bot_name}.")
    emman_bot.run("ODkyNzg5MzAwMTUwODAwNDI0.YVSA1A.pJKLFgx_y3B3yAIszI7s2XwlBSg")
