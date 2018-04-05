from datetime import datetime
from celery import Celery


now = datetime.utcnow()

todays_date = str(now.month) + '-' + str(now.day) + '-' + str(now.year)
todays_dt   = str(now.month) + '-' + str(now.day) + '-' + str(now.year) + \
			  ' ' + str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)

def date_diff(then, now):
    date_format = "%m-%d-%Y %H:%M:%S"
    time1  = datetime.strptime(then, date_format)
    time2  = datetime.strptime(now, date_format)
    
    diff = time2 - time1
    days = diff.days
    days_to_hours = days * 24
    diff_btw_two_times = (diff.seconds) / 3600
    overall_hours = days_to_hours + diff_btw_two_times

    return int(overall_hours)


def make_celery(app):
    celery = Celery(app.import_name, backend=app.config['CELERY_RESULT_BACKEND'],
                    broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery 	