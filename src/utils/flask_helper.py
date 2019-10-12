import logging

from flask import Flask

from src.utils.logger import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):  # pragma: no cover
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


def create_app(name: str) -> Flask:
    app = Flask(name)
    app.logger.addHandler(InterceptHandler())
    return app
