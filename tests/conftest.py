import pytest
import requests_mock

from src.routes.messages import message_app


@pytest.fixture
def client():
    client = message_app.test_client()
    yield client


@pytest.fixture
def mock():
    with requests_mock.Mocker() as mock_instance:
        yield mock_instance
