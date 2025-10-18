FROM python:3.13.9-alpine3.22

WORKDIR /app

COPY discord/requirements.txt .

COPY discord/ .

RUN pip install -r requirements.txt

RUN apt-get update

RUN apt-get install ffmpeg -y

ENV TOKEN <token-value>

CMD ["python3", "lan9000.py"]
