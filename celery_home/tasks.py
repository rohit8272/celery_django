from celery import shared_task
from time import sleep

@shared_task
def sub(x , y):
    sleep(15)
    return x-y

@shared_task
def clear_session_cache(id):
    print(f'session cache cleared {id}')
    return id

@shared_task
def crontab_scheduling_task(message):
    print({message})
    return message