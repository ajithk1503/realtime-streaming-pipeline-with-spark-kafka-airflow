# Real-Time Streaming Pipeline with Spark, Kafka, and Airflow
An End-to-End Data Engineering Project for Streaming, Processing, and Storing Real-Time Data

This project implements a real-time streaming pipeline using **Apache Kafka** for ingestion, **Apache Spark Structured Streaming** for real-time processing, **Apache Airflow** for orchestration, and **Apache Cassandra** as the final data sink. **Zookeeper** is used for managing Kafka, and **PostgreSQL** is used by Airflow for metadata storage.

All services are containerized using Docker and orchestrated via Docker Compose for seamless local development and deployment.

## Architecture Overview

1. **Kafka** receives continuous data streams from a producer.
2. **Zookeeper** coordinates Kafka brokers.
3. **Spark Structured Streaming** consumes Kafka messages, processes them, and writes the results to **Cassandra**.
4. **Airflow** schedules and orchestrates the streaming job using DAGs, and stores metadata in **PostgreSQL**.
5. **Docker Compose** sets up and manages all the services.



