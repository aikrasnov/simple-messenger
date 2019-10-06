from flask import Flask

message_app = Flask(__name__)


@message_app.route("/messages/", methods=["POST"])
def messages():
    return "Hello"
