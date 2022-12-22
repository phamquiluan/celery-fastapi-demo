from celery import Celery

celery_app = Celery("tasks",
    backend='redis://localhost:6379/0',
    broker="amqp://guest:guest@localhost:5672")

@celery_app.task
def task1(input_string):
    result = input_string + " by task 1"
    return result

@celery_app.task
def task2(input_string):
    result = input_string + " by task 2"
    return result

@celery_app.task
def task3(input_string):
    result = input_string + " by task 3"
    return result

@celery_app.task
def task4(input_strings):
    return input_strings[0] + " + " + input_strings[1]