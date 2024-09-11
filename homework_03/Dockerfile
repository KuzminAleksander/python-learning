FROM python:3.9-buster
ENV POETRY_VIRTUALENVS_CREATE=false

COPY . /app
WORKDIR /app
RUN set -xe \
    && apt-get update && apt-get install -y \
        curl \
        build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && /root/.local/bin/poetry install \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
