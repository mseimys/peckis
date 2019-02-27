FROM python:3.6-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends curl libglib2.0-0 libsm6 libxrender1 libxext6 build-essential python-dev
RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
ENV LANG C.UTF-8
WORKDIR /app

ADD pyproject.toml poetry.lock ./
RUN $HOME/.poetry/bin/poetry install --no-interaction

ADD . .
CMD $HOME/.poetry/bin/poetry run ./run.sh
