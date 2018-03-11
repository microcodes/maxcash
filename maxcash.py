import os
from app import db, create_app, celery
from app.models import User

#config_name = os.getenv('FLASK_CONFIG')
config_name = 'development'
app = create_app(config_name)
app.app_context().push()

@app.shell_context_processor
def make_shell_context():
	return {
	'db': db, 
	'User': User
	}