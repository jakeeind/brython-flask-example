__version__ = "0.0.1"

from flask import Flask


from . import models
from . import views


def create_app():
    app = Flask(__name__)
    app.config.from_object("myApp.default_settings")
    app.config.from_envvar("MYAPP_SETTINGS", silent=True)

    # models.init_db(app)
    views.register_blueprint(app)

    return app
