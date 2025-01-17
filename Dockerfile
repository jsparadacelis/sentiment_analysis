
FROM python:3.9

WORKDIR /code
 
COPY ./requirements.txt /code/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./app /code/app
 
CMD ["fastapi", "run", "app/entrypoints/fastapi_app.py", "--port", "80"]