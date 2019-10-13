import logging
import os

from loguru import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):  # pragma: no cover
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


log_level = os.environ.get("LOG_LEVEL", None)
log_level = log_level if log_level is not None else "INFO"
logger.add(
    "main.log", rotation="1 day", retention="2 days", compression="zip", level=log_level
)
