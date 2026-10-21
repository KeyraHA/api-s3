import boto3, json

def lambda_handler(event, context):
    body = event.get('body', event)
    if isinstance(body, str):
        body = json.loads(body)
    bucket = body['bucket']
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket)
    return {'statusCode': 200, 'mensaje': f'Bucket {bucket} creado'}
