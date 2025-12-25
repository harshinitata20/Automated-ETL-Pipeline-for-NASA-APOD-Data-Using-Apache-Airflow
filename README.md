### Project Overview: 
Automated ETL Pipeline for NASA APOD Data Using Apache Airflow

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Apache Airflow to ingest data from an external API and store it in a PostgreSQL database.
The pipeline extracts daily astronomy data from NASA APOD API, processes it, and loads it into a relational database for further analysis or visualization.

The entire workflow is containerized using Docker, ensuring a reproducible and isolated runtime environment.

🧩 Key Components
🔹 Workflow Orchestration (Airflow)

Airflow is used to define, schedule, and monitor the ETL process.

A DAG (Directed Acyclic Graph) manages task dependencies and ensures reliable execution.

The pipeline follows a clear Extract → Transform → Load structure.

🔹 Data Source (NASA APOD API)

The API provides daily astronomy metadata such as:

Image title

Explanation

Image URL

Date

Data is fetched using Airflow’s SimpleHttpOperator.

🔹 Data Storage (PostgreSQL)

A PostgreSQL database stores the processed data.

The database runs inside a Docker container with persistent volumes.

Airflow’s PostgresHook and PostgresOperator are used for database interaction.

The target table is automatically created if it does not already exist.

🔄 ETL Workflow
1️⃣ Extract

Data is fetched daily from the NASA APOD API using HTTP requests.

The response is received in JSON format.

2️⃣ Transform

The raw JSON response is processed using Airflow’s TaskFlow API (@task).

Relevant fields (title, explanation, URL, date) are extracted and formatted to match the database schema.

3️⃣ Load

The transformed data is inserted into PostgreSQL.

Schema management is handled programmatically within the DAG.

☁️ Deployment
🔸 Local Deployment

Airflow and PostgreSQL run as Docker services using Docker Compose.

Enables easy local development and testing.

🔸 Astro Cloud Deployment

The project is deployable on Astronomer Astro Cloud, providing:

Managed Airflow infrastructure

Scalable execution

Centralized monitoring and logging

🔸 AWS Deployment

The pipeline can be deployed on Amazon Web Services, using:

EC2 or ECS for Airflow execution

RDS for PostgreSQL

S3 for logs and backups

Supports production-grade scalability and reliability.

🎯 Project Outcomes

Automated, scheduled API data ingestion

Clean ETL separation using Airflow best practices

Containerized, cloud-deployable architecture

Production-ready workflow suitable for real-world data engineering use cases
