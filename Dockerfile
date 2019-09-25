FROM python:3.6-slim

RUN apt-get update
RUN apt-get install -y --no-install-recommends supervisor curl libglib2.0-0 libsm6 libxrender1 libxext6 build-essential python-dev
RUN pip install poetry
ENV LANG C.UTF-8

WORKDIR /app
ADD pyproject.toml poetry.lock ./
RUN poetry install --no-interaction
RUN poetry run pip install tensorflow==2.0.0b1

ADD . .
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 5000
CMD ["/usr/bin/supervisord"]
