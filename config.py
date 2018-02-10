import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
	#REDIS_URL = 'redis://:123@localhost:6379/0'
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-a-place-holder-guest'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
		'sqlite:///' + os.path.join(basedir, 'maxcash.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False