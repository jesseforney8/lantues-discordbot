FROM python:3.8-slim-buster

WORKDIR /app

COPY discord/requirements.txt .

COPY discord/ .

RUN pip install -r requirements.txt

ENV TOKEN <token-value>

CMD ["python3", "lan9000.py"]
