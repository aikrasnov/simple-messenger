from typing import Dict, List

from .base_messanger import BaseMessanger
from .telegram.telegram import Telegram

SERVICES: List[BaseMessanger] = [Telegram()]

# TODO: replace with TypedDict https://www.python.org/dev/peps/pep-0589/
SERVICES_DICT: Dict[str, BaseMessanger] = {
    service.name: service for service in SERVICES
}
