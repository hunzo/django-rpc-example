FROM python:3.10-slim

RUN apt update -y && apt upgrade -y 

# Install python package
RUN python3 -m venv /opt/venv
ENV Path="/opt/venv/bin:$PATH"


COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache --upgrade pip && \
    /opt/venv/bin/pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 

WORKDIR /app

COPY . /app
