#!/bin/sh

docker compose -f docker-compose.yml --env-file ./.env/.prod up -d --build