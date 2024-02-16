import os
from celery import Celery
from time import sleep
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_django.settings')

app = Celery('celery_django')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task(name="addition_task")
def add(a,b):
    sleep(20)
    return a+b

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


## method 2 of periodic task
# app.conf.beat_schedule = {
#       "clear_session_cache_in_every_10s" : {
#         "task" : "celery_home.tasks.clear_session_cache",
#         "schedule" : 10,
#         "args" : (1111 ,)
#     }
# }
    
app.conf.beat_schedule = {
      "cotrab_scheduling" : {
        "task" : "celery_home.tasks.crontab_scheduling_task",
        "schedule" : crontab(minute='*/1') ,
        "args" : ("hello world",)
    }
}