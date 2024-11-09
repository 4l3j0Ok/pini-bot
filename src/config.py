import os


# General
TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
ADMIN_CHANNEL_ID = int(os.environ.get("ADMIN_CHANNEL_ID"))
LOGGER_CHANNEL_ID = int(os.environ.get("LOGGER_CHANNEL_ID"))
ENABLED_PLUGINS = os.environ.get("ENABLED_PLUGINS", "").split(",")
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
TESTING = os.environ.get("TESTING") == "True"

# Challenges plugin
WEEKLY_CHALLENGES_CHANNEL_ID = int(os.environ.get("WEEKLY_CHALLENGES_CHANNEL_ID"))
WEEKLY_CHALLENGE_DAYS = [
    int(day) for day in os.getenv("WEEKLY_CHALLENGE_DAYS", "0,1,2,3,4,5,6").split(",")
]
WEEKLY_CHALLENGE_HOUR = int(os.getenv("WEEKLY_CHALLENGE_HOUR", "12"))
FIND_CHALLENGES_PATH = "/app/challenges/new"
PROCESSED_CHALLENGES_PATH = "/app/challenges/processed"
INITIAL_CHALLENGES_PATH = "/app/src/plugins/challenges.md"
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = int(os.getenv("MONGO_PORT"))
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")


# Messages
MSG_NO_CHALLENGES_AVAILABLE = "## Falta de retos semanales\nNo hay retos semanales disponibles en la base de datos. Habría que cargar más... O meteme una integración con ChatGPT y me manejo solo!"
