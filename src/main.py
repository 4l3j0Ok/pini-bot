import discord
from discord.ext import tasks
from datetime import datetime
from plugins import challenges
import config
from logger import logger
import time


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previous_url = None

    async def on_ready(self):
        logger.info(f" Logueado como {self.user} (ID: {self.user.id})")
        if "challenges" in config.ENABLED_PLUGINS:
            logger.warning("PLUGIN DE CHALLENGES ACTIVO")
            self.send_weekly_challenge.start()

    @tasks.loop(minutes=15)
    async def send_weekly_challenge(self):
        today = datetime.today()
        admin_channel = self.get_channel(config.ADMIN_CHANNEL_ID)
        channel = (
            self.get_channel(config.WEEKLY_CHALLENGES_CHANNEL_ID)
            if not config.TESTING
            else self.get_channel(config.ADMIN_CHANNEL_ID)
        )
        challenges.fetch_challenges()
        if challenges.is_weekly_challenge_time(today):
            challenge = await challenges.get_weekly_challenge()
            if not challenge:
                logger.warning(
                    "No hay retos semanales disponibles en la base de datos."
                )
                logger.warning("Avisando en el canal de administración.")
                await admin_channel.send(config.MSG_NO_CHALLENGES_AVAILABLE)
                return
            logger.info("Enviando mensaje.")
            await channel.send("¡Hoy es día de reto semanal! @everyone")
            await channel.send(challenge["content"])
            await challenges.mark_challenge(challenge["_id"], sent_at=today)
        return


if __name__ == "__main__":
    time.tzset()
    client = Client(intents=discord.Intents.default())
    client.run(config.TOKEN)
