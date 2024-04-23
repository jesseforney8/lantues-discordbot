FROM python:3.8-slim-buster

COPY requirements.txt .

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENV TOKEN <token-value>

CMD ["python3", "lan9000.py"]
