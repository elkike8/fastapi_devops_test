FROM python:3.9

COPY requirements.txt requirments.txt

RUN pip install fastapi
RUN pip install uvicorn
RUN pip install Jinja2

COPY app.py app.py

COPY /html /html

EXPOSE 80

CMD [ "uvicorn", "app:app" ]