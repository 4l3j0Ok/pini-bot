from logger import logger
import config


class Commands:
    def __init__(self, bot):
        self.bot = bot
        logger.info("Registrando comandos...")

        @bot.command()
        async def ping(ctx):
            await ctx.send("Pong!")

        @bot.command()
        async def send(ctx, *, message: str):
            if not any(role.id in config.ADMIN_ROLES_IDS for role in ctx.author.roles):
                logger.warning(
                    f"El usuario '{ctx.author}' intentó enviar un mensaje sin los permisos necesarios."
                )
                return
            await ctx.message.delete()
            await ctx.send(message)
