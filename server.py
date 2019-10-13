from flask import Flask
from gevent.pywsgi import WSGIServer

from src.routes.services import init_routes
from src.utils.logger import InterceptHandler, logger

message_app = Flask(__name__)
message_app.logger.addHandler(InterceptHandler())


@message_app.route("/static/<path:path>")
def static_file(path):
    logger.debug(path)
    return message_app.send_static_file(path)


init_routes(message_app)

if __name__ == "__main__":
    PORT = 80
    logger.info(f"Running server on {PORT}")
    http_server = WSGIServer(("", PORT), message_app)
    http_server.serve_forever()
