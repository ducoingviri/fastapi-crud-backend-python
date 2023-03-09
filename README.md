# CRUD Foundations for Backend Apps using FastAPI on Python

This is a backend application which implements CRUD operations using different
approaches over the REST APIs. 

## The Environment

1. Python 3.6.8
2. Pip 21.3.1
3. FastAPI 0.83.0
4. Pydantic 1.9.2

## Management Instructions

To create the project, create a virtual environment, and activate it:
```
mkdir todos && cd todos
python3 -m venv venv
source venv/bin/activate
```

To close the virtual environment (optional):
```
deactivate
```

To install necessary packages:
```
pip install fastapi
pip install uvicorn
pip install pydantic
```

To save installed packages in a file for future use (if you install more packages then, re-run this command to update the file):
```
pip freeze > requirements.txt
```

To install packages (optional):
```
pip install -r requirements.txt
```

To upgrade pip utility (optional):
```
pip install --upgrade pip
```

To run the application:
```
uvicorn api:app --port 8000 --reload
```

# Testing

## With Swagger UI

Open the following URL in a browser:
```
http://127.0.0.1:8000/docs
```

## With ReDoc

Open the following URL in a browser:
```
http://127.0.0.1:8000/redoc
```

## With cURL

### Without model validation

Root API:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/' \
  -H 'accept: application/json'
```

Todo Store API:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"id" : 1, "item_name": "red flower"}'
```

Todo Index API:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/todo' \
  -H 'accept: application/json'
```

### With model validation using Pydantic

User Store API:
```
curl -X 'POST' \
  'http://127.0.0.1:8000/user' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "username": "optimus"
}'
```

User Index API:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/user' \
  -H 'accept: application/json'
```

### With path parameter

User Show API:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/user/3' \
  -H 'accept: application/json'
```

User Destroy API:
```
curl -X 'DELETE' \
  'http://127.0.0.1:8000/user/5' \
  -H 'accept: application/json'
```

### With path parameter and request body

User Update API:
```
curl -X 'PUT' \
  'http://127.0.0.1:8000/user/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 2,
  "username": "joker"
}'
```
