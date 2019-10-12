from loguru import logger

logger.add("main.log", rotation="1 day", retention="2 days", compression="zip")
