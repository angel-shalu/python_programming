FROM python:3.10-slim

WORKDIR /app

# system deps for opencv and general utilities
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# default command is to run both services via docker-compose (override per service)
CMD ["/bin/bash", "-c", "echo 'Container ready; use docker-compose to run services' && sleep infinity"]
