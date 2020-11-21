from static.scripts.app import create_app
from static.scripts.config import DevelopmentConfig, ProductionConfig


app = create_app(config_object= DevelopmentConfig)


if __name__ == '__main__':
    app.run()
