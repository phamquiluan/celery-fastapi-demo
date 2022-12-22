# Celery - FastAPI demo

## Installation

```bash
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

```bash
 curl --location --request POST 'localhost:8080/process?input_string=hello'
```