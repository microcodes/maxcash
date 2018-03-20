from datetime import datetime
from werkzeug.security import generate_password_hash


now = datetime.utcnow()
date_format = "%m-%d-%Y %H:%M:%S"

todays_date = str(now.month) + '-' + str(now.day) + '-' + str(now.year)
todays_dt   = str(now.month) + '-' + str(now.day) + '-' + str(now.year) + \
			  ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

def date_diff(then, now):
	time1  = datetime.strptime(then, date_format)
	time2  = datetime.strptime(now, date_format)

	diff = time2 - time1
	days = diff.days
	days_to_hours = days * 24
	diff_btw_two_times = (diff.seconds) / 3600
	overall_hours = days_to_hours + diff_btw_two_times

	return int(overall_hours)


def insert_users(db, User):
	
	db.drop_all()
	db.create_all()

	user_1 = User(email='mjhdaais@gmail.com',
				phone='07065385493', 
		        password=generate_password_hash('mjhd'),
		        bank_name='First Bank', 
		        acc_no='3036040428', 
		        acc_name='Abdulwahab Abdullateef',
		        role='crtr',
		        stock=2000,
		        status='seller')

	user_2 = User(email='maim@gmail.com',
				phone='07035948710',
				password=generate_password_hash('maim'),
		        bank_name='Ecobank', 
		        acc_no='0306040191', 
		        acc_name='Maimuna Abdullateef',
		        role='intx',
		        status='seller')

	user_3 = User(email='husna@gmail.com',
				phone='08198447511',
				password=generate_password_hash('husn'), 
		        bank_name='UBA', 
		        acc_no='07145670911', 
		        acc_name='Hussaina Abdullateef')

	user_4 = User(email='illiyas@gmail.com',
				phone='07067491101',
				password=generate_password_hash('illi'), 
		        bank_name='FCMB', 
		        acc_no='0145934191', 
		        acc_name='Illiyasu Abdullateef')

	user_5 = User(email='hasna@gmail.com',
				phone='09067011243',
				password=generate_password_hash('hasn'), 
		        bank_name='Zenith Bank', 
		        acc_no='0711110124', 
		        acc_name='Hassana Abdullateef')

	user_6 = User(email='ummi@gmail.com',
				phone='07065303011',
				password=generate_password_hash('ummi'), 
		        bank_name='Diamond Bank', 
		        acc_no='1110756341', 
		        acc_name='Fatima Abdullateef')

	db.session.add_all([user_2, user_2, user_3, user_4, user_5, user_6])
	db.session.commit()