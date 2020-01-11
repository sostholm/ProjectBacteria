FROM python:alpine

COPY ./src/ /app/

WORKDIR app

RUN pip install -r requirements.txt

CMD ["python3", "-u", "./app.py"]