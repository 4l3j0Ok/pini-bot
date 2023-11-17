import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime, timedelta
from plugins import ngrok, challenges
import config
from logger import logger


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


    @tasks.loop(seconds = 60)
    async def ngrok_daemon(self):
        channel = self.get_channel(config.LOGGER_CHANNEL_ID) \
            if not config.TESTING else self.get_channel(config.ADMIN_CHANNEL_ID)
        result = await ngrok.get_public_url()
        if result != self.previous_url:
            logger.info("La URL obtenida es diferente de la anterior, mandando mensaje.")
            result_str = config.MSG_URL_CHANGED.format(url=result)
            await channel.send(result_str)
        else:
            logger.info("La URL obtenida es igual a la anterior, no se manda mensaje.")
        self.previous_url = result


    @tasks.loop(seconds = 60)
    async def send_weekly_challenge(self):
        now = datetime.now()
        time_to_wait = timedelta(weeks=1)
        admin_channel = self.get_channel(config.ADMIN_CHANNEL_ID)
        channel = self.get_channel(config.CHALLENGES_CHANNEL_ID) \
            if not config.TESTING else self.get_channel(config.ADMIN_CHANNEL_ID)
        challenge = await challenges.get_weekly_challenge()
        if not challenge:
            logger.error("No hay retos semanales disponibles en la base de datos.")
            await admin_channel.send(config.MSG_NO_CHALLENGES_AVAILABLE)
        latest_message_date = challenges.get_latest_challenge_date()
        if not latest_message_date:
            await channel.send(challenge["content"])
            await challenges.mark_challenge(challenge["_id"], sent_at=now)
        else:
            if now - latest_message_date > time_to_wait:
                await channel.send(challenge["content"])
                await challenges.mark_challenge(challenge["_id"], sent_at=now)
            else:
                logger.info("Todavía no ha pasado el tiempo necesario para mandar el reto semanal.")
                logger.info(f"Quedan {time_to_wait - (now - latest_message_date)} para mandar el reto semanal.")


client = Client(intents=discord.Intents.default())
client.run(config.TOKEN)
