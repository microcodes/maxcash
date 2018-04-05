from flask import Flask
from celery import Celery

from app.extensions import db, migrate, login_manager, mail
from app.util import make_celery

#from config import app_config
import celeryconfig

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.cfg')

celery = make_celery(app)
celery.config_from_object(celeryconfig)     

db.init_app(app)
migrate.init_app(app)
mail.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in'

from app import models

from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .dashboard import dash as dash_blueprint
app.register_blueprint(dash_blueprint)

"""
def create_app(config_name='production'):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.cfg')
	db.init_app(app)
	migrate.init_app(app, db)
	mail.init_app(app)
	login_manager.init_app(app)
	login_manager.login_view = 'auth.sign_in'

	from app import models

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	from .dashboard import dash as dash_blueprint
	app.register_blueprint(dash_blueprint)

	return app
"""	