#import os
from app import db, create_app, celery
from app.models import User

#config_name = os.getenv('FLASK_CONFIG')
app = create_app('production')
app.app_context().push()

"""
db.drop_all()

db.create_all()

user_1 = User(email='mjhdaais@gmail.com',
			phone='07065385493', 
	        password='mjhd',
	        bank_name='First Bank', 
	        acc_no='3036040428', 
	        acc_name='Abdulwahab Abdullateef',
	        role='crtr',
	        stock=2000,
	        status='seller')

user_2 = User(email='maim@gmail.com',
			phone='07035948710', 
	        password='maim',
	        bank_name='Ecobank', 
	        acc_no='0306040191', 
	        acc_name='Maimuna Abdullateef',
	        role='intx',
	        status='seller')

user_3 = User(email='husna@gmail.com',
			phone='08198447511', 
	        password='husn',
	        bank_name='UBA', 
	        acc_no='07145670911', 
	        acc_name='Hussaina Abdullateef')

user_4 = User(email='illiyas@gmail.com',
			phone='07067491101', 
	        password='illi',
	        bank_name='FCMB', 
	        acc_no='0145934191', 
	        acc_name='Illiyasu Abdullateef')

user_5 = User(email='hasna@gmail.com',
			phone='09067011243', 
	        password='hasn',
	        bank_name='Zenith Bank', 
	        acc_no='0711110124', 
	        acc_name='Hassana Abdullateef')

user_6 = User(email='ummi@gmail.com',
			phone='07065303011', 
	        password='ummi',
	        bank_name='Diamond Bank', 
	        acc_no='1110756341', 
	        acc_name='Fatima Abdullateef')

db.session.add_all([user_1, user_2, user_3, user_4, user_5, user_6])
db.session.commit()
"""

@app.shell_context_processor
def make_shell_context():
	return {
	'db': db, 
	'User': User
	}