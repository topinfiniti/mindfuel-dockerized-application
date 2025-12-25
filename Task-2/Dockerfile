FROM python:3.11-slim

WORKDIR /app

RUN apt-get update

ENV PYTHONDONOTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --no-cache-dir -r  requirements.txt

COPY src/ ./src
COPY .env .env

CMD ["python", "src/main.py"]