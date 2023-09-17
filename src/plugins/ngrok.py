import config
import requests
from logger import logger


async def get_public_url():
    try:
        api_tunnels_url = config.NGROK_URL + config.NGROK_TUNNELS_PATH
        logger.info(f"Haciendo GET a {api_tunnels_url}")
        response = requests.get(api_tunnels_url)
        logger.info(f"Response: {response}")
        tunnels = response.json().get("tunnels", {})
        for tunnel in tunnels:
            if tunnel.get("name") == config.NGROK_TUNNEL_NAME:
                url = tunnel.get("public_url")
                logger.info("URL publica de Ngrok obtenida.")
        return url
    except Exception as ex:
        logger.exception(ex)
        raise ex
