import os


# General
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
TESTING = os.environ.get("TESTING") == "True"
ADMIN_CHANNEL_ID = int(os.environ.get("ADMIN_CHANNEL_ID"))
LOGGER_CHANNEL_ID = int(os.environ.get("LOGGER_CHANNEL_ID"))
ENABLED_PLUGINS = os.environ.get("ENABLED_PLUGINS", "").split(",")


# Ngrok Plugin
NGROK_URL = os.getenv("NGROK_URL")
NGROK_TUNNELS_PATH = "/api/tunnels"
NGROK_TUNNEL_NAME = "menumaker"
NGROK_APP_NAME = "Menu Maker"


# Challenges plugin
CHALLENGES_CHANNEL_ID = int(os.environ.get("CHALLENGES_CHANNEL_ID"))
INITIAL_CHALLENGES_PATH = "/app/src/plugins/challenges.md"
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")


# Messages
MSG_URL_CHANGED = f"## <:online:1155558498097168454>Aplicación reiniciada\nLa aplicación **{NGROK_APP_NAME}** está online otra vez .\nURL: " + "**{url}**"
MSG_NO_CHALLENGES_AVAILABLE = f"## Falta de retos semanales\nNo hay retos semanales disponibles en la base de datos. Habría que cargar más... O meteme una integración con ChatGPT y me manejo solo!"