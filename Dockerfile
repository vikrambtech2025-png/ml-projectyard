ARG BASE_IMAGE=ghcr.io/ashishsahu1/ml-project-yard/base:latest
FROM ${BASE_IMAGE}

WORKDIR /app

COPY --chown=app:app requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=app:app . .

EXPOSE 7860

HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
  CMD python -c "import urllib.request,sys; urllib.request.urlopen('http://127.0.0.1:7860/', timeout=3); sys.exit(0)" || exit 1

CMD ["python", "app.py"]
