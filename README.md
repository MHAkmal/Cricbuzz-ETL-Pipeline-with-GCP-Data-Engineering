# Cricbuzz-ETL-Pipeline-with-GCP-Data-Engineering
The Data Engineer's core task is to deliver data from various resources to OLAP databases such as data warehouse or data lake using ETL or ELT concept. Here we will create an end-to-end ETL pipeline using Google Cloud Platform and Cricbuzz API

## Architecture
![cricbuzz etl architecture](https://github.com/MHAkmal621/Cricbuzz-ETL-Pipeline-with-GCP-Data-Engineering/assets/110396432/a2b73c89-83a4-4b7b-b68f-6e4e178ef910)

## Extract Data
### Python and Cricbuzz API
The first thing to do is create a code in python to interact with Cricbuzz API from RapidAPI website and store it in a CSV file.

### Cloud Composer
Cloud Composer function in this project to create an automation and triggerer in apache airflow so the extracted data will automatically pushed to Google Cloud Storage.

## Transform Data
### Cloud Function
Once the data stored in GCS, we create a function to trigger a job in Dataflow.

## Load Data
### Dataflow.
The Dataflow will receive a trigger from Cloud Function and start a job that was already defined before in Cloud Function to transform and load the data to BigQuery.

## Analytics & Dashboard
### BigQuery
the transformed data from GCS then stored to Bigquery and ready for analytical process.

### Looker Studio
Finally, the analytical-ready data from Bigquery connected to Looker studio and ready for dashboarding.

<img width="602" alt="cricbuzz dashboard" src="https://github.com/MHAkmal621/Cricbuzz-ETL-Pipeline-with-GCP-Data-Engineering/assets/110396432/2831ed12-3145-40fc-a81c-823410cb8f45">
