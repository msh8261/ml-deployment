import pytest

from static.scripts.app import create_app
from static.scripts.config import TestingConfig

app = create_app(config_object=TestingConfig)



app.testing = True


@pytest.fixture
def app():
    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client