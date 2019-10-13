from src.utils.logger import InterceptHandler
from src.utils.text_helper import TextHelper


def test_hide_sensitive_data():
    assert TextHelper.hide_sensitive_data("foobar") == "**obar"


def test_loguru_handler():
    assert InterceptHandler()
