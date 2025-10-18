FROM python:3.9-slim-buster

WORKDIR /app

COPY discord/requirements.txt .

COPY discord/ .

RUN pip install -r requirements.txt

RUN RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    apt-get install ffmpeg -y


ENV TOKEN <token-value>

CMD ["python3", "lan9000.py"]
