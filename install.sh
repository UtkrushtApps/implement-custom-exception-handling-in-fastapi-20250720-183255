#!/usr/bin/env bash
set -euo pipefail

if ! command -v docker &> /dev/null
then
    echo "Docker not found. Please install Docker before running this script."
    exit 1
fi

echo "Building Docker images..."
docker-compose build

echo "Starting containers..."
docker-compose up -d

echo "Waiting for API to become available..."
TRIES=20
until curl -s http://localhost:8000/docs &> /dev/null; do
  ((TRIES--)) || { echo "API did not start in time"; docker-compose logs; exit 1; }
  sleep 2
done

echo "API is up!"
