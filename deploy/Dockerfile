FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get upgrade -y && apt-get update -y
RUN pip install -U pip && pip install uv

COPY pyproject.toml /app/

RUN uv sync --no-dev

COPY ./.env ./deploy/entrypoint.sh /app/
COPY ./src /app/src/

ENTRYPOINT [ "sh", "./entrypoint.sh" ]
