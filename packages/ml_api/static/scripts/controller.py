from flask import request, jsonify, Blueprint
import os
from werkzeug.utils import secure_filename

from static.scripts.app import create_DB
from static.scripts.config import RedisConfig


from static.scripts.config import get_logger, UPLOAD_FOLDER
from static.scripts import _version as api_version
from static.scripts import __version__ as _version


redis = create_DB(config_object= RedisConfig)

_logger = get_logger(logger_name=__name__)


pred_app = Blueprint('pred_app', __name__)


@pred_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'


@pred_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})




@pred_app.route('/', methods=['GET'])
def hello_world():
	if request.method == 'GET':
	    redis.set('last_page_visited_3', 'account3')
	    return 'Hello, World!'

@pred_app.route('/visitor', methods=['GET'])
def visitor():
	if request.method == 'GET':
	    redis.incr('visitor')
	    visitor_num = redis.get('visitor').decode("utf-8")
	    return "Visitor: %s" % (visitor_num)

@pred_app.route('/visitor/reset', methods=['GET'])
def reset_visitor():
	if request.method == 'GET':
	    redis.set('visitor', 0)
	    visitor_num = redis.get('visitor').decode("utf-8")
	    return "Visitor is reset to %s" % (visitor_num)












