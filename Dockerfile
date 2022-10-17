FROM python:3.9

COPY requirements.txt requirments.txt

RUN pip install --no-chache-dir --upgrade -r requirements.txt

COPY app.py app.py

COPY /html /html
