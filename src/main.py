import discord
from discord.ext import commands
import asyncio
from plugins import ngrok
import config
from logger import logger


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    async def on_ready(self):
        print(f" Logueado como {self.user} (ID: {self.user.id})")
        await self.ngrok_daemon()


    async def ngrok_daemon(self, previous_url=None):
        channel = self.get_channel(config.LOGGER_CHANNEL_ID)
        result = await ngrok.get_public_url()
        if result != previous_url:
            logger.info("La URL obtenida es diferente de la anterior, mandando mensaje.")
            result_str = config.MSG_URL_CHANGED.format(url=result)
            await channel.send(result_str)
        else:
            logger.info("La URL obtenida es igual a la anterior, no se manda mensaje.")
        await asyncio.sleep(60)
        await self.ngrok_daemon(previous_url=result)


client = Client(intents=discord.Intents.default())
client.run(config.TOKEN)
