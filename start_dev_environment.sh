#!/bin/sh

docker compose -f docker-compose-dev.yml --env-file ./.env/.dev up -d --build