import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	pass


class DevelopmentConfig(Config):
	SECRET_KEY = 'i-a-place-holder-guest'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'maxcash.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = True
	#CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
	#CELERY_BROKER_URL = 'pyamqp://'


class ProductionConfig(Config):
	pass


class TestingConfig(Config):
	pass


app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
	'testing': TestingConfig
}