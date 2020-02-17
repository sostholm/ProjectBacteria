FROM python:latest

COPY ./src/ /app/
COPY requirements.txt /app/

WORKDIR app

RUN apt-get update 

RUN pip install -r requirements.txt

CMD ["python3", "-u", "./app.py"]