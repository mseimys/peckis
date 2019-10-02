# Peckis backend

ML backend that you can train to recognize your doodles.

## Running

You need poetry and all the dependencies installed. Tensorflow 2.0 should
be installed via `pip` since [poetry can't handle it](https://github.com/sdispater/poetry/issues/1330):

```
poetry install
poetry run pip install tensorflow
```

### Train a model for serving

```
poetry run python -m models.numbers
```

A folder `serving` should appear in root directory. To serve this model via
Tensorflow Serving container run `serving.sh`.

### Workers and API

Run celery workers via `workers.sh`.
Execute `run.sh` to start Flask API.

### Web frontend

Launch https://github.com/mseimys/peckis-ui frontend to do some experiments.
