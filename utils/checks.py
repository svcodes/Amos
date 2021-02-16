from discord.ext.commands import check, Context

def channel():
    async def predicate(ctx: Context) -> bool:
        return ctx.channel.id == ctx.bot.config.get("channel", 0)

    return check(predicate)
