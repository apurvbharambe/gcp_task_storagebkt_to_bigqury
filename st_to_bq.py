from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    #put project_id
    project = "apurvaproject-419411"   

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
    "jobName": "bq-load-automated",  # Provide a unique name for the job
    "parameters": {
        "inputFilePattern": "gs://user101/titanic.csv",
        "JSONPath": "gs://user101/dataflow.json",
        "outputTable": "apurvaproject-419411:user_dataset.usertable",
        "bigQueryLoadingTemporaryDirectory": "gs://user101",
        "javascriptTextTransformGcsPath": "gs://user101/dataflow.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)

