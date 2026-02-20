# bank_management
A robust, role-based banking system API built with Django, Django REST Framework, and Celery.

## Features

- **Role-Based Access Control**:
  - **Customer**: View own account, pay loans.
  - **Employee**: View customer accounts.
  - **Manager**: View all accounts, create users, apply interest.
- **Loan Management**: Issue loans and pay loans via API.
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

### Chances of issues

1.  Check Port conflict:
    ```bash
    sudo lsof -i :6379
    ```
2.  Kill port:
    ```bash
    sudo kill -9 <PID>
    ```
### Cleary
1.  Run celery:
    ```bash
    exec celery -A banking_system worker -l info
    ```

## API Documentation

### Authentication
The API uses Session Authentication (standard Django login) or Basic Auth for simplicity in testing.

### Sample Payloads

**Login**
```json
POST /api/login/
{
    "email": "manager@bank.com",
    "password": "securepass"
}
Responce
{
    "user": {
        "email": "customer@customer.com",
        "mobile_number": "12235698",
        "customer_id": "CUST171757",
        "role": "customer",
        "is_active": true
    },
    "token": "fc0abf7bad1e7b39e10cb11e2f43d03eb9ece74b6c27e06bdf5749e92705bd3b"
}
```


**Create User (Manager)**
```json
POST /api/user/create/

headers
Authorization - Token fc0abf7bad1e7b39e10cb11e2f43d03eb9ece74b6c27e06bdf5749e92705bd3b
{
  "email": "customer@bank.com",
  "mobile_number": "9876543210",
  "role": "customer",
  "password": "pass"
}
```

**Pay Loan**
```json
POST /api/loan/pay/

headers
Authorization - Token fc0abf7bad1e7b39e10cb11e2f43d03eb9ece74b6c27e06bdf5749e92705bd3b
{
  "customer_id": "CUST123456",
  "amount": 5000
}
```

**Apply Interest (Manager)**
```json
POST account/apply/interest/

headers
Authorization - Token fc0abf7bad1e7b39e10cb11e2f43d03eb9ece74b6c27e06bdf5749e92705bd3b
{
  "interest_percent": 5.0
}
```

**Take Loan**
```json
POST /api/take/loan/

headers
Authorization - Token fc0abf7bad1e7b39e10cb11e2f43d03eb9ece74b6c27e06bdf5749e92705bd3b
{
  "customer_id": "CUST123456",
  "amount": 5000
}
```

