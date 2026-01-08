FROM python:3.14.2-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=abegify.settings.prod


# Set work directory
WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc libpq-dev build-essential pkg-config default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/
