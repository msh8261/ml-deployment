from flask import Flask 

from static.scripts.app import get_logger


_logger = get_logger(logger_name = __name__)


def create_app(*, config_object) -> Flask:
	""" create a flask app instance."""

	flask_app = Flask('ml_api')
	flask_app.config.from_object(config_object)

	#important bluebprints
	_logger.debug('Application instance created')

	return flask_app