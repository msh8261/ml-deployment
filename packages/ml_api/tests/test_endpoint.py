import pytest
import json

from static.scripts.app import create_app
from static.scripts.config import TestingConfig
from static.scripts import _version as api_version
from static.scripts import __version__ as _version

from static.scripts.app import create_DB
from static.scripts.config import RedisConfig


app = create_app(config_object=TestingConfig)


redis = create_DB(config_object= RedisConfig)
visitor_num = redis.get('visitor').decode("utf-8")


app.testing = True


def test_endpoint():
	tester = app.test_client()
	response1 = tester.get('/health', content_type='html/text')
	response2 = tester.get('/version', content_type='html/text')
	response3 = tester.get('/', content_type='html/text')
	response4 = tester.get('/visitor', content_type='html/text')
	response5 = tester.get('/visitor/reset', content_type='html/text')
	assert response1.status_code == 200
	assert response2.status_code == 200
	assert response3.status_code == 200
	assert response4.status_code == 200
	assert response5.status_code == 200



def test_endpoint_data():
	tester = app.test_client()
	response1 = tester.get('/health', content_type='html/text')
	response2 = tester.get('/version', content_type='html/text')
	response3 = tester.get('/', content_type='html/text')
	response4 = tester.get('/visitor', content_type='html/text')
	response5 = tester.get('/visitor/reset', content_type='html/text')
	assert response1.data == b'ok'
	response_json_version = json.loads(response2.data)
	assert response_json_version['model_version'] == _version
	assert response_json_version['api_version'] == api_version
	assert response3.data == b'Hello, World!'

	string = 'Visitor: {}'.format(int(visitor_num)+1)
	# string with encoding 'utf-8'
	arr = bytes(string, 'utf-8')
	assert response4.data == arr
	assert response5.data == b'Visitor is reset to 0'

