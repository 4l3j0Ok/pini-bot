import os


# General
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
ADMIN_CHANNEL_ID = int(os.environ.get("ADMIN_CHANNEL_ID"))
LOGGER_CHANNEL_ID = int(os.environ.get("LOGGER_CHANNEL_ID"))
ADMIN_ROLES_IDS = [
    int(role) for role in os.environ.get("ADMIN_ROLES_IDS", "").split(",")
]
ENABLED_PLUGINS = os.environ.get("ENABLED_PLUGINS", "").split(",")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
TESTING = os.environ.get("TESTING") == "True"
APP_PATH = os.path.dirname(os.path.abspath(__file__))

# Commands
PREFIX = os.environ.get("PREFIX", "!")

# Challenges plugin
WEEKLY_CHALLENGES_CHANNEL_ID = int(os.environ.get("WEEKLY_CHALLENGES_CHANNEL_ID"))
WEEKLY_CHALLENGE_DAYS = [
    int(day) for day in os.getenv("WEEKLY_CHALLENGE_DAYS", "0,1,2,3,4,5,6").split(",")
]
WEEKLY_CHALLENGE_HOUR = int(os.getenv("WEEKLY_CHALLENGE_HOUR", "12"))
WEEKLY_CHALLENGE_INTERVAL = int(os.getenv("WEEKLY_CHALLENGE_INTERVAL", "1"))
FIND_CHALLENGES_PATH = f"{APP_PATH}/../challenges/new"
PROCESSED_CHALLENGES_PATH = f"{APP_PATH}/../challenges/processed"
INITIAL_CHALLENGES_PATH = f"{APP_PATH}/plugins/challenges.md"
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")


# Messages
MSG_NO_CHALLENGES_AVAILABLE = "## Falta de retos semanales\nNo hay retos semanales disponibles en la base de datos. Habría que cargar más... O meteme una integración con ChatGPT y me manejo solo!"
