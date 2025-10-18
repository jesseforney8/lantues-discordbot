FROM python:3.12-slim

WORKDIR /app

COPY discord/requirements.txt .

COPY discord/ .

RUN pip install -r requirements.txt

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        ca-certificates \
    && rm -rf /var/lib/apt/lists/*


ENV TOKEN <token-value>

CMD ["python3", "lan9000.py"]
