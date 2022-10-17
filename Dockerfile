FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/requirments.txt

RUN pip install --no-chache-dir --upgrade -r /code/requirements.txt

COPY app.py /code/app.py

COPY /html /code/html
