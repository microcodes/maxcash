from datetime import datetime


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