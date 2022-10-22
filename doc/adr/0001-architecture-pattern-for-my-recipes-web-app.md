# 1. Architecture pattern for My Recipes web app

Date: 2022-10-18

## Status

Proposed

## Context

My Recipes web app will be split in several components to ensure its functionality

## Decision

The base of the web app will be built with Python (Django), the other technologies that will be used are as follows:
- postgreSQL: for the database
- MongoDB: for keeping track of the mails sent from the app
- Celery: will take care of sending the mails
- Redis: as broker for Celery
- Apache: for the webserver
- Nginx: for proxy
