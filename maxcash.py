#import os
from app import db, create_app, celery
from app.models import User
from app.util import insert_users

#config_name = os.getenv('FLASK_CONFIG')
app = create_app('production')
app.app_context().push()

#insert_users(db, User)

@app.shell_context_processor
def make_shell_context():
	return {
	'db': db, 
	'User': User
	}