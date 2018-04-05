#from app import db, create_app, celery
from app import app, db
from app.models import User
from instance.insert_users import insert_users

#app = create_app()
#app.app_context().push()

#insert_users(db, User)

@app.shell_context_processor
def make_shell_context():
	return {
	'db': db, 
	'User': User
	}