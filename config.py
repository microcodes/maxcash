import os
import redis

basedir = os.path.abspath(os.path.dirname(__file__))
redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

class Config:
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-a-place-holder-guest'
	REDIS_DB_URI= os.environ.get('REDIS_URI') or redis_db
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
		'sqlite:///' + os.path.join(basedir, 'maxcash.db')
	SQLALCHEMY_TRACK_MODIFICATIONS = False