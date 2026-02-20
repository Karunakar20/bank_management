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
