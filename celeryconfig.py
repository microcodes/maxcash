#from datetime import timedelta
from celery.schedules import crontab


accept_content    = ['json']
task_serializer   = 'json'
result_serializer = 'json'
timezone          = 'Africa/Lagos'

beat_schedule = {
    'every-1-hour': {
        'task': 'app.tasks.profit',
        'schedule': 5.0
    },
    'every-1-hour': {
    	'task': 'app.tasks.re_sell',
    	'schedule': 5.0
    }
}