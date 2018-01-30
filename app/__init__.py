from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)
r = app.config['REDIS_DB_URI']

from app import routes