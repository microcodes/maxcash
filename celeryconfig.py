from datetime import timedelta


accept_content    = ['json']
task_serializer   = 'json'
result_serializer = 'json'
timezone          = 'Africa/Lagos'

beat_schedule = {
    'every-10-seconds': {
        'task': 'tasks.print',
        # Every 10 seconds
        'schedule': timedelta(seconds=10)
    }
}