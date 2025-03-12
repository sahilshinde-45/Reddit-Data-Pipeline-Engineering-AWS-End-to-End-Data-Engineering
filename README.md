# Reddit-Data-Pipeline-Engineering-AWS-End-to-End-Data-Engineering
📌 Overview

    This project is an ETL pipeline that extracts data from the Reddit API, processes it using Apache Airflow, and loads it into AWS S3, Athena, and Redshift for further analysis. The pipeline runs in a Dockerized environment using CeleryExecutor with      PostgreSQL as the metadata database.

🚀 Tech Stack

    Apache Airflow – Orchestrating the ETL pipeline
    CeleryExecutor – Distributed task execution
    PostgreSQL – Airflow metadata storage
    Reddit API – Data source for extraction
    AWS Glue – Data transformation
    AWS S3 – Data storage
    AWS Athena – Querying raw data
    AWS Redshift – Data warehousing

🛠️ Pipeline Workflow

    1️⃣ Extract Data – Fetches top posts from Reddit API
    2️⃣ Transform Data – Cleans and processes using AWS Glue
    3️⃣ Load Data – Saves to AWS S3 and makes it queryable with Athena
    4️⃣ Store in Redshift – Loads structured data into Redshift
    5️⃣ Schedule with Airflow – DAG runs daily using CeleryExecutor





