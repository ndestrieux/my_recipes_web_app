FROM python:3.10.8-bullseye

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./deployment/dev/start/start.sh /start
RUN sed -i "s/\r$//g" /start
RUN chmod +x /start

COPY ./deployment/dev/celery/start_worker.sh /start_worker
RUN sed -i "s/\r$//g" /start_worker
RUN chmod +x /start_worker

WORKDIR /app
