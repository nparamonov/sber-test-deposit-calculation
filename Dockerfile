FROM python:3.12-slim as base

RUN apt-get update \
    && apt-get -y install curl \
    && apt-get clean all \
    && rm -rf /var/lib/apt/lists/*

# Пользователь без root прав
RUN addgroup --system app && adduser --system --group app


# --- builder ---
FROM base as builder

ENV \
	POETRY_VERSION=1.8.2 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /app

COPY poetry.lock pyproject.toml ./

RUN poetry install --without tests --no-root && rm -rf $POETRY_CACHE_DIR


# --- runtime ---
FROM base as runtime

USER app

WORKDIR /app

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    LOG_LEVEL=INFO

COPY --from=builder ${VIRTUAL_ENV} ${VIRTUAL_ENV}

COPY src ./src

HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
    CMD curl --fail http://127.0.0.1:8000/service/ping || exit 1

EXPOSE 8000

ENTRYPOINT ["uvicorn", "src.main:deposit_calculation_app.app", \
            "--loop", "uvloop", \
            "--no-server-header", \
            "--host", "0.0.0.0", \
            "--port", "8000"]
