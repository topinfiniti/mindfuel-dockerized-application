# 📦 MindFuel – Dockerized Quote Delivery Service

This repository contains two tasks demonstrating how to containerize a Python-based email quote delivery service and run it as a multi-container application using Docker and Docker Compose.

The project fetches inspirational quotes, stores logs, connects to a relational database, and delivers emails to active subscribers.

---
## 📁 Repository Structure
<pre>
├── Task-1/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src/
        ├── main.py
│   │   ├── active_subscriber.py
│   │   ├── extract_quote.py
│   │   ├── send_email.py
│   │   ├── database.py
│   ├── logs/
│   ├── .env
│   └── README.md

├── Task-2/
│   ├── docker-compose.yml        # Docker Compose file
│   ├── Dockerfile                # Python app container definition
│   ├── requirements.txt          # Python dependencies
│   ├── src/                      # Source folder for Python code
│   │   ├── main.py
│   │   ├── active_subscriber.py
│   │   ├── extract_quote.py
│   │   ├── send_email.py
│   │   ├── database.py
│   │   └── init.sql              # Database initialization script
│   └── .env                      # Environment variables
│
└── README.md
</pre>
---
## ✅ Task 1: Containerize the Python Email Delivery Service
### 🎯 Objective
    Package the Python quote-delivery service into a portable, reproducible Docker image and publish it to a container registry.

### 🔧 Requirements Implemented

    •   Lightweight Python base image

    •   Python dependencies installed via requirements.txt

    •   Environment variables loaded using .env

    •   Application code copied into the container

    •   Clear entrypoint to start the application

    •   Image built, tested, and published to a registry
---
### 🐳 Dockerfile Overview
#### The Dockerfile:

    •   Uses python:3.11-slim

    •   Installs required system and Python dependencies

    •   Copies application source code

    •   Loads environment variables

    •   Starts the quote delivery service automatically

### 🛠️ Build the Image Locally
    docker build -t mindfuel-app:1.0 .

### ▶️ Run the Container    
    docker run --env-file .env mindfuel-app:1.0

### ✔️ Verified Behavior

    •   Quotes are fetched successfully

    •   Database connection is established

    •   Emails are sent to subscribers

    •   Logs are written to the logs/ directory

### 🌍 Published Image

    docker tag mindfuel-app:1.0 olusegun1992/mindfuel-app:1.0
    docker push olusegun1992/mindfuel-app:1.0


### ⬇️ Pull and Run from Registry
    docker pull olusegun1992/mindfuel-app:1.0
    docker run --env-file .env olusegun1992/mindfuel-app:1.0
---
## Logs

![App logs showing successful quote delivery](images/Task-1%20logs-screenshot.jpeg)
---
## ✅ Task 2: Multi-Container Setup With Docker Compose

### 🎯 Objective
    Run the Python application, database and pgadmin together using Docker Compose.

### 🔧 Requirements Implemented
#### Services Defined

    •   App – Python quote delivery service

    •   Db – PostgreSQL database

    •   pgadmin - Web-based PostgreSQL administration and monitoring tool

### 🧩 compose.yml Features

    •   Multiple services defined (app, postgres database, pgadmin)

    •   Ports mapped for external access

    •   Persistent database storage using Docker volumes

    •   Environment variables loaded securely from .env

    •   Service dependencies defined using depends_on

## 📦 Volumes
    •   Database data is persisted using a Docker-managed volume

    •   SQL initialization handled via init.sql

---
## 🚀 Commands

### ▶️ Start the Full Stack
        docker compose up --build

###  🐳 Check running containers
        docker compose ps

###  📜 View logs for the app
        docker logs task-2-app-1

### ✔️ Verification Checklist

    •   Entire stack starts successfully

    •   App automatically connects to the database

    •   Database initializes correctly

    •   Quotes are fetched

    •   Emails are delivered

    •   Logs are generated without errors

### 🛑 Stop the Stack + volumes
    docker compose down -v
---

### 🖼️ Architecture Diagram
            +-------------------+
            |    Python App     |
            |  (task-2-app-1)   |
            +---------+---------+
                      |
                      | connects via host "postgres"
                      |
            +---------v---------+
            |   PostgreSQL DB   |
            | (task-2-postgres) |
            +---------+---------+
                      |
                      | managed via host "postgres"
                      |
            +---------v---------+
            |      pgAdmin      |
            | (task-2-pgadmin)  |
            +-------------------+
---

### 🧠 Notes
    Postgres only runs init.sql on first database creation. Use docker compose down -v to reset volumes if you need to re-run initialization.

    Retry logic in the app ensures stable DB connections during startup.

    Secrets are managed via .env for security and flexibility.   
---
## Logs

![App logs showing successful quote delivery](images/Task-2%20logs-screenshot.jpeg)
---