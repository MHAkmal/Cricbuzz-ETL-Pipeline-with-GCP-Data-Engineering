from googleapiclient.discovery import build

def trigger_df_job(cloud_event, environment):

    service = build('dataflow', 'v1b3')
    project = 'my-data-engineer-project'

    template_path = 'gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery'

    template_body = {
        "jobName": "bq-load",       # Provide a unique name for the job
        "parameters": {
        "javascriptTextTransformGcsPath": "gs://cricbuzz-metadatas/udf.js",
        "JSONPath": "gs://cricbuzz-metadatas/bq.json",
        "javascriptTextTransformFunctionName": "transform",
        "outputTable": "my-data-engineer-project:cricbuzz_dataset.icc_odi_batsman_ranking",
        "inputFilePattern": "gs://cricbuzz-ranking-data/batsmen_rankings.csv",
        "bigQueryLoadingTemporaryDirectory": "gs://dataflow-metadatas",
        }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)