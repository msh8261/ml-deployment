from flask import request, jsonify, Blueprint

import os
from werkzeug.utils import secure_filename

from static.scripts.config import get_logger, UPLOAD_FOLDER
from static.scripts import _version as api_version
from static.scripts import __version__ as _version



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















