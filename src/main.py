import discord
from discord.ext import tasks
from datetime import datetime, timedelta
from plugins import ngrok, challenges
import config
from logger import logger
import time


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.previous_url = None


    async def on_ready(self):
        logger.info(f" Logueado como {self.user} (ID: {self.user.id})")
        if "ngrok" in config.ENABLED_PLUGINS:
            logger.warning("PLUGIN DE NGROK ACTIVO")
            self.ngrok_daemon.start()
        if "challenges" in config.ENABLED_PLUGINS:
            logger.warning("PLUGIN DE CHALLENGES ACTIVO")
            self.send_weekly_challenge.start()


    @tasks.loop(minutes = 15)
    async def ngrok_daemon(self):
        channel = self.get_channel(config.LOGGER_CHANNEL_ID) \
            if not config.TESTING else self.get_channel(config.ADMIN_CHANNEL_ID)
        result = await ngrok.get_public_url()
        if result and result != self.previous_url:
            logger.info("La URL obtenida es diferente de la anterior, mandando mensaje.")
            result_str = config.MSG_URL_CHANGED.format(url=result)
            await channel.send(result_str)
        else:
            logger.info("La URL obtenida es igual a la anterior, no se manda mensaje.")
        self.previous_url = result


    @tasks.loop(minutes = 15)
    async def send_weekly_challenge(self):
        today = datetime.today()
        admin_channel = self.get_channel(config.ADMIN_CHANNEL_ID)
        channel = self.get_channel(config.WEEKLY_CHALLENGES_CHANNEL_ID) \
            if not config.TESTING else self.get_channel(config.ADMIN_CHANNEL_ID)
        challenge = await challenges.get_weekly_challenge()
        if not challenge:
            logger.warning("No hay retos semanales disponibles en la base de datos.")
            logger.warning("Avisando en el canal de administración.")
            await admin_channel.send(config.MSG_NO_CHALLENGES_AVAILABLE)
            return
        if challenges.is_weekly_challenge_time(today):
            logger.info("Enviando mensaje.")
            await channel.send(f"¡Hoy es día de reto semanal! @everyone")
            await channel.send(challenge["content"])
            await challenges.mark_challenge(challenge["_id"], sent_at=today)
        return


if __name__=="__main__":
    time.tzset()
    client = Client(intents=discord.Intents.default())
    client.run(config.TOKEN)

