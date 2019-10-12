from abc import ABC, abstractmethod
from typing import Optional

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.utils.logger import logger
from src.utils.text_helper import TextHelper


class BaseMessanger(ABC):
    """All messanger should use this class as base."""

    text_helper = TextHelper()
    logger = logger

    @property
    @abstractmethod
    def name(self):
        """Name is used for build API endpoints."""

    @property
    @abstractmethod
    def json_schema(self):
        """Schema is used for body validation.

        https://pypi.org/project/jsonschema/
        """

    @abstractmethod
    def send_message(self, *args, **kwargs) -> Optional[str]:
        """Each messanger should implement its own method for send messages.

        If third party errors occurs while sending it need to be returning as string.
        """

    def validate(self, data: dict) -> Optional[str]:
        try:
            validate(data, self.json_schema)
        except ValidationError as error:
            return str(error)
