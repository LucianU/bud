FROM python:3.7-slim-buster

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN pip install poetry

# Copy only pyproject.toml and poetry.lock first (for better caching)
COPY pyproject.toml poetry.lock ./

# Install dependencies (use --no-root to skip installing the project itself)
RUN poetry install --no-root --with dev

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

WORKDIR /app
