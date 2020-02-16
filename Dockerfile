FROM python:alpine

COPY ./src/ /app/
COPY requirements.txt /app/

WORKDIR app

RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc and-build-dependencies \
    && rm -rf /var/lib/apt/lists/* \
    && pip install cryptography \
    && apt-get purge -y --auto-remove gcc and-build-dependencies

RUN pip install -r requirements.txt

CMD ["python3", "-u", "./app.py"]