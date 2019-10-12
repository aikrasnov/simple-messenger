from src.utils.flask_helper import InterceptHandler, create_app
from src.utils.text_helper import TextHelper


def test_hide_sensitive_data():
    assert TextHelper.hide_sensitive_data("foobar") == "**obar"


def test_flask_helper():
    assert create_app("foobar") is not None


def test_loguru_handler():
    assert InterceptHandler()
