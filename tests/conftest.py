import pytest
from sanic_testing import TestManager

from app.config import config
from main import create_app


# Fixture to create and configure the Sanic application
@pytest.fixture(scope='session')
def test_app():
    app = create_app(configs=config)
    TestManager(app)
    return app

# Fixture to provide the Sanic test client for making HTTP requests in tests
@pytest.fixture
def test_http_client(test_app):
    return test_app.test_client
