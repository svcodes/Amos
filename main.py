from templatebot import Bot
from discord import Intents

from utils.loader import load

config = load()

bot = Bot(name="Amos", command_prefix=".", intents=Intents.all())
bot.config = config
bot.VERSION = "1.0.0"

bot.load_initial_cogs(
    "cogs.core.core",
    "cogs.fun.fun"
)

bot.run(config["token"])
