import os
import json
import boto3

def sentences_embeddings(sentences):

  client = boto3.client(
    service_name = 'sagemaker-runtime', 
    region_name = os.environ.get('REGION_NAME'),
    aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')
  )

  data = { "inputs": sentences }

  response = client.invoke_endpoint(
      EndpointName= os.environ.get('ENDPOINT_NAME'),
      ContentType='application/json',
      Body=json.dumps(data).encode('utf-8')
  )

  return json.loads(response['Body'].read())