FROM python:3.10.8-bullseye

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY ./requirements.txt /app
RUN pip install -r requirements.txt

COPY ./deployment/dev/start.sh /scripts
RUN sed -i "s/\r$//g" /scripts
RUN chmod +x /scripts

ENTRYPOINT ["/scripts"]
