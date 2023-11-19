from .db.connect import client
import config
from datetime import datetime
from logger import logger
from typing import Union
from bson.objectid import ObjectId


coll = client.pini_bot.challenges


async def get_weekly_challenge() -> Union[dict, None]:
    if coll.count_documents({}) == 0:
        save_initial_challenges()
    logger.info("Obteniendo reto semanal.")
    challenge = coll.find_one({"sent": False})
    return challenge


def save_initial_challenges():
    logger.info("Guardando los retos iniciales.")
    with open(config.INITIAL_CHALLENGES_PATH, "r") as file:
        content = file.read()
        challenges = [challenge for challenge in content.split("#") if challenge]
        data = []
        for challenge in challenges:
            challenge = f"#{challenge}"
            document = {
                "content": challenge,
                "sent": False,
                "sent_at": None
            }
            data.append(document)
        coll.insert_many(data)
    return


async def mark_challenge(challenge_id: ObjectId, sent_at: datetime = datetime.now()) -> None:
    logger.info(f"Marcando reto semanal como enviado: {challenge_id}")
    coll.update_one({"_id": challenge_id}, {"$set": {"sent": True, "sent_at": sent_at}})
    return


def get_latest_challenge_date() -> Union[datetime, None]:
    challenge = coll.find_one({"sent": True}, sort=[('sent_at', -1)])
    return challenge["sent_at"] if challenge else None


def is_weekly_challenge_time(today: datetime = datetime.today()) -> bool:
    latest_challenge_date = get_latest_challenge_date()
    logger.debug(f"Días de reto semanal: {config.WEEKLY_CHALLENGE_DAYS}")
    logger.debug(f"Último mensaje de reto semanal: {latest_challenge_date}")
    if today.weekday() in config.WEEKLY_CHALLENGE_DAYS:
        if not latest_challenge_date or latest_challenge_date.date() != today.date():
            if today.hour >= config.WEEKLY_CHALLENGE_HOUR:
                logger.info("Hoy es un día de reto semanal, y es la hora de enviar el mensaje.")
                return True
            else:
                logger.info("Hoy es un día de reto semanal, pero no es la hora de enviar el mensaje.")
                return False
        else:
            logger.info("Hoy es un día de reto semanal, pero ya se ha enviado el mensaje.")
            return False
    logger.info("Hoy no es un día de reto semanal.")
    return False
