from flask import request

from src.messengers import SERVICES_DICT
from src.utils.flask_helper import create_app

message_app = create_app(__name__)


@message_app.route("/services/<string:service>", methods=["POST"])
def send_message(service):
    messenger_instance = SERVICES_DICT[service]
    data = request.get_json()
    validation_error = messenger_instance.validate(data)

    if validation_error is not None:
        return message_app.make_response(({"validation errors": validation_error}, 400))

    internal_error = messenger_instance.send_message(**data)

    if internal_error is not None:
        return message_app.make_response(({"sending errors": internal_error}, 503))

    return message_app.make_response(
        {"message": f"message sent to {messenger_instance.name}"}
    )


@message_app.route(f"/services/<string:service>", methods=["GET"])
def get_description(service):
    return SERVICES_DICT[service].json_schema


@message_app.route("/services/", methods=["GET"])
def services_list():
    return message_app.make_response({"available": list(SERVICES_DICT.keys())})
