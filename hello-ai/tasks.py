import datetime

import celery
from celery import Celery
from celery.signals import task_postrun

app = Celery('tasks', broker='amqp://guest:guest@localhost/', backend='redis://localhost:6379/0')




@app.task
def add(x, y):
    return x + y

@app.task
def div(request_id, x, y):
    return x + y


if __name__ == '__main__':
    result = add.delay(30, 42)
    print(result)
