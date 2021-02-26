from discord import Embed
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType


from templatebot import Bot

class Fun(commands.Cog):
    """A set of fun commands for Amos"""

    def __init__(self, bot: Bot):
        self.bot = bot
    
    @commands.cooldown(1, 60, BucketType.member) 
    @commands.command(name="duckgen")
    async def duckgen(self, ctx: commands.Context, duckname = None):
      name = duckname or ctx.author.name
      embed = Embed(title="Duck!", description=f"Here's your duck, {ctx.author.mention}!")
      embed.set_image(f"https://ducks.vcokltf.re/duck/{name}")
      await ctx.send(embed=embed)
    


def setup(bot: Bot):
    bot.add_cog(Fun(bot))
