import pytest
import json

from static.scripts.app import create_app
from static.scripts.config import TestingConfig
from static.scripts import _version as api_version
from static.scripts import __version__ as _version


app = create_app(config_object=TestingConfig)


app.testing = True


def test_endpoint():
	tester = app.test_client()
	response1 = tester.get('/health', content_type='html/text')
	response2 = tester.get('/version', content_type='html/text')
	assert response1.status_code == 200
	assert response2.status_code == 200


def test_endpoint_data():
	tester = app.test_client()
	response1 = tester.get('/health', content_type='html/text')
	response2 = tester.get('/version', content_type='html/text')
	assert response1.data == b'ok'
	response_json = json.loads(response2.data)
	assert response_json['model_version'] == _version
	assert response_json['api_version'] == api_version
