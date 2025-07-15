from celery import Celery
import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
celery = Celery('tasks', broker=REDIS_URL)

@celery.task
def add(x, y):
    return x + y
