from flask import Flask 
import redis

from static.scripts.config import get_logger


_logger = get_logger(logger_name = __name__)


def create_app(*, config_object) -> Flask:
	""" create a flask app instance."""

	flask_app = Flask('ml_api')
	flask_app.config.from_object(config_object)

	# import blueprints
	from static.scripts.controller import pred_app
	flask_app.register_blueprint(pred_app)
	_logger.debug('Application instance created')

	return flask_app



def create_DB(*, config_object):
	redis_ = redis.Redis(config_object.host, config_object.port, config_object.db)
	redis_.set('last_page_visited_2', 'account2')
	return redis_