# Peckis backend

ML backend that you can train to recognize your doodles.

## Running

You need poetry and all the dependencies installed. Tensorflow 2.0.0rc1 should
be installed via `pip` or else [it fails](https://github.com/sdispater/poetry/issues/1330):

```
poetry run pip install tensorflow==2.0.0rc1
```

Execute `run.sh`.

Launch https://github.com/mseimys/peckis-ui frontend to do some experiments.

## Retraining

Run the following command to retrain the model:

```
poetry run python -m models.numbers
```
