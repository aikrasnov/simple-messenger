import traceback

import requests

from src.messengers.base_messanger import BaseMessanger


class TelegramParseMode:
    markdown = "Markdown"
    HTML = "HTML"


class Telegram(BaseMessanger):
    timeout = 5
    TOKEN_PLACEHOLDER = "<bot_token>"
    send_message_handler = (
        f"https://api.telegram.org/bot{TOKEN_PLACEHOLDER}/sendMessage"
    )
    NAME = "telegram"
    json_schema = {
        "type": "object",
        "required": ["text", "bot_token", "chat_id"],
        "properties": {
            "text": {"type": "string"},
            "bot_token": {"type": "string", "pattern": "^[0-9A-Za-z:_]+$"},
            "chat_id": {"type": "number"},
            "parse_mode": {
                "type": "string",
                "enum": [TelegramParseMode.markdown, TelegramParseMode.HTML],
            },
        },
    }

    @property
    def name(self):
        return self.NAME

    def send_message(
        self,
        bot_token: str,
        chat_id: int,
        text: str,
        parse_mode: TelegramParseMode = None,
    ):
        body = {"chat_id": chat_id, "text": text}

        if parse_mode is not None:
            body.update({"parse_mode": parse_mode})

        try:
            self.logger.info(
                f"Send message to {self.name} with params: "
                f"bot_token={self.text_helper.hide_sensitive_data(bot_token)} "
                f"chat_id={self.text_helper.hide_sensitive_data(str(chat_id))} "
                f"text={self.text_helper.hide_sensitive_data(text)} "
                f"parse_mode={parse_mode}"
            )
            response = requests.post(
                self.send_message_handler.replace(self.TOKEN_PLACEHOLDER, bot_token),
                timeout=self.timeout,
                json=body,
            )
            self.logger.info(f"Telegram response: {response.status_code}")
        except Exception as error:
            self.logger.error(
                f"Error occured {error}, traceback: {traceback.format_exc()}"
            )
            return str(error)

        if response.status_code != 200:
            return (
                f"Telegram response {response.status_code}, with text: {response.text}"
            )
