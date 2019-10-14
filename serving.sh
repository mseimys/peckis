#!/bin/bash -e
docker run -it --rm -p 8501:8501 -v "$(pwd)/serving:/models" -e MODEL_NAME=number tensorflow/serving
