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

## Deployment

Create a docker network:

```
docker network create peckis
```

Build tensorflow/serving docker image and run it:

```
docker build -t serving -f Dockerfile.serving .
docker run --rm -it --network peckis --name peckis-serving serving
```

Build and run workers and api:

```
docker build -t peckis .
docker run --rm -it -p 5000:5000 --network peckis -e SERVING_HOST=http://peckis-serving:8501 peckis
```

Build and run peckis UI:

```
docker build --build-arg GUESS_API="http://localhost:5000/guess" -t peckis-ui .
docker run --rm -it -p 3000:80 peckis-ui
```
