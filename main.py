from fastapi import FastAPI
from tasks import task1, task2, task3, task4
from os import environ as env


from celery.canvas import chain, chord


app = FastAPI()

@app.post("/process")
def process(input_string: str):
    # Chain task1, task2, and task3 together and execute them in sequence
    result = chain(task1.s(input_string), task2.s(), task3.s())()

    # Wait for the chain to complete, with a timeout of 10 seconds
    result.wait(timeout=10)
    return result.result    

@app.post("/process_complex")
def process_complex(input_string: str):
    result = chain(task1.s(input_string),
          # Use the chord function to execute task2 and task3 in parallel
          # Both tasks use the output from task1 as the input
          chord([task2.s(), task3.s()], task4.s()),
    )()
    result.wait(timeout=10)
    return result.result
    