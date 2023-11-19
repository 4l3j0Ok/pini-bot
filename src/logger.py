import logging
import config


logging.basicConfig(
    encoding = "utf-8",
    level = config.LOG_LEVEL,
    format = "MODULE: %(filename)s | LINE: %(lineno)d - %(levelname)s: %(message)s",
    datefmt = "%d/%m/%Y %H:%M:%S"
)

logger = logging.getLogger()
