# Real-Time Streaming Pipeline with Spark, Kafka, and Airflow
An End-to-End Data Engineering Project for Streaming, Processing, and Storing Real-Time Data


This project demonstrates a real-time data streaming pipeline built using **Apache Kafka** for ingestion, **Apache Spark Structured Streaming** for real-time processing, and **Apache Airflow** for orchestration. The entire architecture runs on Docker using Docker Compose.

## Architecture Overview

1. **Kafka** receives continuous data streams (simulated producer).
2. **Spark Structured Streaming** consumes data from Kafka, applies transformations, and optionally writes results to a sink (e.g., console, file, or database).
3. **Airflow** schedules and manages the execution of the pipeline using DAGs.
4. **Docker Compose** sets up all services in isolated containers.


