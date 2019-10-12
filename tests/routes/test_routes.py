import pytest

from src.messengers import SERVICES_DICT, Telegram
from src.utils.qa_utils import check_response

services_names = list(SERVICES_DICT.keys())


class TestServicesEndpoint:
    endpoint = "/services/"

    def test_services(self, client):
        response = client.get(self.endpoint)
        check_response(response, self.endpoint)
        assert response.json["available"] == services_names


@pytest.mark.parametrize("service", services_names)
class TestServicesMessangerEndpoint:
    service_placeholder = "<string:service>"
    endpoint = f"/services/{service_placeholder}"

    def test_services_messanger_info(self, client, service):
        response = client.get(self.endpoint.replace(self.service_placeholder, service))
        check_response(response)
        assert (
            response.json == SERVICES_DICT[service].json_schema
        ), f"{service} has invalid json schema"


class TestTelegramMessangerEndpoint:
    bot_token = "truefakebottoken"
    endpoint = "/services/telegram"
    telegram_endpoint = Telegram.send_message_handler.replace(
        Telegram.TOKEN_PLACEHOLDER, bot_token
    )

    @pytest.fixture
    def default_body(self):
        return {
            "chat_id": 123123123123123123,
            "bot_token": self.bot_token,
            "text": "verylongtestmessage",
        }

    @pytest.fixture(autouse=True)
    def mock_endpoint(self, mock):
        return mock.post(self.telegram_endpoint)

    def test_telegram_send_message(self, client, default_body):
        response = client.post(self.endpoint, json=default_body)
        check_response(response, self.endpoint)
        assert (
            response.json["message"] == "message sent to telegram"
        ), "Wrong response message"

    @pytest.mark.parametrize("parse_mode", ["HTML", "Markdown"])
    def test_telegram_send_message_parse_mode(self, client, parse_mode, default_body):
        default_body.update({"parse_mode": parse_mode})
        response = client.post(self.endpoint, json=default_body)
        check_response(response, self.endpoint)
        assert (
            response.json["message"] == "message sent to telegram"
        ), "Wrong response message"

    @pytest.mark.parametrize("field_to_delete", ["chat_id", "bot_token", "text"])
    def test_telegram_send_message_invalid_body(
        self, client, field_to_delete, default_body
    ):
        del default_body[field_to_delete]
        response = client.post(self.endpoint, json=default_body)
        check_response(response, self.endpoint, 400)

    @pytest.mark.parametrize("status_code", [500, 503, 403, 401, 400])
    def test_telegram_send_message_invalid_status_code(
        self, client, mock, status_code, default_body
    ):
        mock.post(self.telegram_endpoint, status_code=status_code, text="F")
        response = client.post(self.endpoint, json=default_body)
        check_response(response, self.endpoint, 503)
        assert (
            response.json["sending errors"]
            == f"Telegram response {status_code}, with text: F"
        )

    def test_telegram_send_message_telegram_timeout(self, client, mock, default_body):
        error_text = "Test error"
        mock.post(self.telegram_endpoint, exc=RuntimeError(error_text))
        response = client.post(self.endpoint, json=default_body)
        check_response(response, self.endpoint, 503)
        assert response.json["sending errors"] == error_text

    @pytest.mark.parametrize("parse_mode", ["XML", "HTML5", "JSON"])
    def test_invalid_parse_mode(self, client, parse_mode, default_body):
        default_body.update({"parse_mode": parse_mode})
        response = client.post(self.endpoint, json=default_body)
        check_response(response, self.endpoint, 400)
