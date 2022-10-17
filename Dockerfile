FROM python:3.9

COPY requirements.txt requirments.txt

RUN pip install -r requirements.txt

COPY app.py app.py

COPY /html /html