from discord import Embed
from discord.ext import commands

from templatebot import Bot

from utils.checks import channel as inchannel


class Core(commands.Cog):
    """A set of core commands for Amos"""

    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command(name="info")
    @commands.check_any(inchannel(), commands.is_owner())
    async def info(self, ctx: commands.Context):
        embed = Embed(title=f"Amos Info - v{self.bot.VERSION}", colour=0x87ceeb)
        embed.description = f"Ping: {round(self.bot.latency * 1000, 3)}ms\n"
        embed.description += f"Guild: {ctx.guild.id}\n"
        embed.description += f"User: {ctx.me.id}"
        await ctx.send(embed=embed)


def setup(bot: Bot):
    bot.add_cog(Core(bot))