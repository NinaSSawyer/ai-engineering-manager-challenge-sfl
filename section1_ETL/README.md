# Section 1 – Database Configuration & Python ETL #

This section provisions a PostgreSQL database using Docker and implements a Python ETL pipeline to ingest, transform, and load the provided Excel dataset.

## Tools & Technologies ##

- PostgreSQL (Docker)
- Python 3.10
- pandas
- SQLAlchemy
- docker-compose
- openpyxl

## Getting Started ##

### 1. Launch the Database ###

Use Docker Compose to start the PostgreSQL container.

```
bash
docker-compose up -d

This will start a database on localhost:5432 with the following credentials:

    User: nina

    Password: password123

    Database: challenge_db
```

### 2. Run the ETL Script ###

```
pip install -r requirements.txt
python etl_pipeline.py
```

This script performs the following:
1. Loads and cleans the provided Excel dataset
2. Performs basic transformations
3. Loads the result into a PostgreSQL table named chemberta_dataset

### 3. Notes ###

The .env file is used to manage DB credentials.

The database schema will be created automatically if it doesn't exist.

**Files**
* etl_pipeline.py – Main ETL process
* docker-compose.yml – PostgreSQL container configuration
* requirements.txt – Python dependencies
