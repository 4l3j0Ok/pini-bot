from logger import logger


class Commands:
    def __init__(self, bot):
        self.bot = bot
        logger.info("Registrando comandos...")

        @bot.command()
        async def ping(ctx):
            await ctx.send("Pong!")

        @bot.command()
        async def send(ctx, *, message: str):
            await ctx.message.delete()
            await ctx.send(message)
