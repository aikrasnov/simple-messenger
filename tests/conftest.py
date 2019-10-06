import pytest

from src.routes.messages import message_app


@pytest.fixture
def client():
    client = message_app.test_client()
    yield client
