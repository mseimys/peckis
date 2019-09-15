#!/bin/sh -e
poetry run celery -A workers.celery worker --pool=solo --loglevel=info
