import os


TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
ADMIN_CHANNEL_ID = int(os.environ.get("ADMIN_CHANNEL_ID"))
LOGGER_CHANNEL_ID = int(os.environ.get("LOGGER_CHANNEL_ID"))

NGROK_URL = "http://ngrok:4040"
NGROK_TUNNELS_PATH = "/api/tunnels"
NGROK_TUNNEL_NAME = "menumaker"
NGROK_APP_NAME = "Menu Maker"

MSG_URL_CHANGED = f"## AVISO:\nLa URL de la aplicación **{NGROK_APP_NAME}** ha sido actualizada.\nURL: " + "**{url}**"