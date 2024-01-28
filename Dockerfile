FROM python:3.8-slim

WORKDIR /app

RUN apt update && apt install -y curl && apt-get -y install libpq-dev gcc

COPY requirements.txt /app
RUN pip3 install -r requirements.txt

HEALTHCHECK --interval=30s --timeout=10s --start-period=30s \
    CMD curl --fail http://localhost:8002/health || exit 1