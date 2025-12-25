# Automated ETL Pipeline for NASA APOD Data

**Apache Airflow · PostgreSQL · Docker · Astro Cloud · AWS**

---

## Overview

This project implements a production-ready **ETL (Extract, Transform, Load) pipeline** using **Apache Airflow** to ingest data from an external API and store it in a relational database. The pipeline extracts daily astronomy data from the **NASA APOD API**, transforms the response, and loads structured records into **PostgreSQL** for analysis and reporting.

The entire workflow is containerized using Docker, ensuring a reproducible and isolated execution environment. The pipeline is deployable both locally and on cloud platforms such as Astro Cloud and AWS.

---

## Architecture

```
NASA APOD API
      ↓
Apache Airflow (DAG)
      ↓
Transform (TaskFlow API)
      ↓
PostgreSQL Database
```

---

## Tech Stack

* Apache Airflow
* PostgreSQL
* Docker & Docker Compose
* Python
* Astro Cloud
* Amazon Web Services (AWS)

---

## ETL Workflow

### Extract

* Fetches data from the NASA APOD API using Airflow's `SimpleHttpOperator`
* Receives structured JSON responses containing astronomy metadata

### Transform

* Processes raw JSON data using Airflow's **TaskFlow API (`@task`)**
* Extracts and formats relevant fields such as title, explanation, image URL, and date

### Load

* Loads transformed data into PostgreSQL using Airflow's `PostgresHook`
* Automatically creates the target table if it does not already exist

---

## Project Structure

```
airflow-etl-nasa-apod/
├── dags/
│   └── nasa_apod_etl_dag.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── sql/
│   └── create_table.sql
├── requirements.txt
├── .env.example
└── README.md
```

---

## Deployment

### Local (Docker)

* Runs Airflow and PostgreSQL using Docker Compose
* Suitable for local development and testing

```bash
docker-compose up -d
```

Access the Airflow UI at:

```
http://localhost:8080
```

---

### Astro Cloud

* Fully compatible with **Astronomer Astro Cloud**
* Provides managed Airflow infrastructure, scalability, and centralized monitoring

---

### AWS

* Deployable on **Amazon Web Services**
* Typical setup includes:

  * EC2 or ECS for Airflow execution
  * RDS for PostgreSQL
  * S3 for logs and backups

---

## Use Cases

* Automated daily API data ingestion
* Analytical dataset creation
* Learning production-grade Airflow workflows
* Foundation for scalable data engineering pipelines

---

## Future Enhancements

* Data quality validation
* Incremental loading logic
* Failure alerting and monitoring
* Multi-layer data modeling

---

## License

This project is intended for educational and portfolio use.

---
