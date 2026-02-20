# bank_management
A robust, role-based banking system API built with Django, Django REST Framework, and Celery.

## Features

- **Role-Based Access Control**:
  - **Customer**: View own account, pay loans.
  - **Employee**: View customer accounts.
  - **Manager**: View all accounts, create users, apply interest.
- **Loan Management**: Issue loans (via admin/shell), pay loans via API.
- **Async Processing**: Interest application handled asynchronously using Celery and Redis.
- **Data Integrity**: Atomic transactions for critical financial operations.
- **Dockerized**: Easy deployment with Docker Compose.

## Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- Python 3.11+ and Redis (for local development)


### Installation
1.  Clone the repository:
    ```bash
    git clone <repo_url>
    ```
### Setup for backend
1.  Navigate to the project directory
     ```bash
    cd bank_management
    ```
2.  Create virtual environment (.venv)
     ```bash
    python3 -m venv .venv
    ```
3.  Activate Virtual Environment
      ```bash
    source .venv/bin/activate
    ```
4.  Install dependencies:
       ```bash
    pip install -r requirements.txt
    ```
5.  Create Migration Files
      ```bash
    python manage.py makemigrations
    ```
6.  Apply Migrations to Database
      ```bash
    python manage.py migrate
    ```
7.  Intilaize intigrations (Will create a manager)
      ```bash
    python initializer.py

8. Docker setup
   ```bash
    docker compose up -d

**Chances of issues** - Docker port conflixts
   1.check port - sudo lsof -i :6379
   2.kill port - sudo kill -9 <PID>
   
   
