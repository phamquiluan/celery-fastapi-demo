from fastapi import FastAPI
from tasks import task1, task2, task3
from os import environ as env


from celery import chain


app = FastAPI()

@app.post("/process")
def process(input_string: str):
    # Chain task1, task2, and task3 together and execute them in sequence
    result = chain(task1.s(input_string), task2.s(), task3.s())()

    # Wait for the chain to complete, with a timeout of 10 seconds
    result.wait(timeout=10)
    return result.result    
