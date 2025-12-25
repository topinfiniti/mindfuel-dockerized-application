FROM python:3.11-slim

#Prevent python from writting pycahe file
ENV PYTHONDONOTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

#update the package list
RUN apt-get update

COPY requirements.txt .

#Install python dependencies

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src

COPY .env .env

CMD ["python", "src/main.py"]