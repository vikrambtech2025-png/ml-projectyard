# ML-ProjectYard

Production-ready Gradio application for the **ML-ProjectYard** machine learning project.

## Overview

| Attribute | Value |
|---|---|
| Task type | other |
| Model family | torch |
| Dataset | Not required (see project). |

> Part of [ML-ProjectYard](https://github.com/ashishsahu1/ML-ProjectYard) — 163
> independently deployed ML services, each with its own container, CI/CD and UI.

## Quickstart

```bash
# 1. install dependencies
pip install -r requirements.txt

# 2. fetch the dataset (requires a Kaggle credential for some datasets)
python scripts/fetch_data.py

# 3. train / export the model
python scripts/train.py

# 4. launch the interactive UI
python app.py
```

Open http://127.0.0.1:7860

## Docker

```bash
docker build -t ml-projectyard .
docker run --rm -p 7860:7860 ml-projectyard
```

The image runs as a non-root user with a healthcheck on the Gradio endpoint.

## Tests

```bash
python -m unittest discover -s tests -t .
```

## Project layout

```
app.py                 # Gradio UI (entrypoint)
src/                   # config, model registry, io utilities
scripts/               # fetch_data / train / predict
tests/                 # smoke tests
Dockerfile             # production image
requirements.txt
```

## Deploy

Single-host: see the Dockerfile. Kubernetes/Compose orchestration and the GHCR
pipeline live in the [monorepo `deploy/`](https://github.com/ashishsahu1/ML-ProjectYard/tree/main/deploy).
