FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt .

COPY . .

RUN pip install -r requirements.txt

ENV TOKEN <token-value>

CMD ["python3", "lan9000.py"]
