import os


TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

ADMIN_CHANNEL_ID = 1099504669446901871
LOGGER_CHANNEL_ID = 1152686748967637103
NGROK_URL = "http://ngrok:4040"
NGROK_TUNNELS_PATH = "/api/tunnels"
NGROK_TUNNEL_NAME = "menumaker"
NGROK_APP_NAME = "Menu Maker"

MSG_URL_CHANGED = f"## AVISO:\nLa URL de la aplicación **{NGROK_APP_NAME}** ha sido actualizada.\nURL: " + "**{url}**"