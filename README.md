# Celery - FastAPI demo

## Installation

```bash
# install rabbitmq + redis
sudo apt-get update
sudo apt-get install rabbitmq-server redis-server

# then start it
sudo systemctl start rabbitmq-server
sudo systemctl start redis-server

# install python deps
pip install -r requirements.txt
```

## How-to-run

1. Start celery tasks

```bash 
celery -A tasks worker --loglevel=debug
```

2. Start FastAPI

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

3. Call

call simple pipeline that includes three sequential tasks
```bash
 curl --location --request POST 'localhost:8080/process?input_string=hello'
```

call complex pipeline that run task1 first, then task2 and task3 in parallel, finally, run task3 to merge the output of task2 and task3.
```bash
 curl --location --request POST 'localhost:8080/process_complex?input_string=hello'
```
