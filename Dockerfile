FROM python:3.11.9-slim-bullseye

ARG POETRY_VERSION=1.8.2
ARG POETRY_DOWNLOAD=https://install.python-poetry.org
ARG PROJECT_URL=https://github.com/WEBBsava/simple_calculator_2024.git
ENV PATH="$PATH:/root/.local/bin"
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests -y \
        curl \
        git \
        bash \
    && ln -sf /bin/bash /bin/sh \
    && curl -sSL $POETRY_DOWNLOAD | python3 - --version $POETRY_VERSION
    

ENV POETRY=/root/.local/bin/poetry

WORKDIR /app
RUN git clone $PROJECT_URL
WORKDIR /app/simple_calculator_2024

RUN git checkout main \
    && poetry install

CMD ["run", "pytest"]