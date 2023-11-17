from .db.connect import client
import config
from datetime import datetime
from logger import logger


coll = client.pini_bot.challenges


async def get_weekly_challenge():
    if coll.count_documents({}) == 0:
        save_initial_challenges()
    challenge = coll.find_one({"sent": False})
    return challenge


def save_initial_challenges():
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


async def mark_challenge(challenge_id, sent_at=datetime.now()):
    coll.update_one({"_id": challenge_id}, {"$set": {"sent": True, "sent_at": sent_at}})


def get_latest_challenge_date():
    challenge = coll.find_one({"sent": True}, sort=[('sent_at', -1)])
    return challenge["sent_at"] if challenge else None