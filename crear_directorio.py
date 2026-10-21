import boto3, json

def lambda_handler(event, context):
    body = event.get('body', event)
    if isinstance(body, str):
        body = json.loads(body)
    bucket = body['bucket']
    directorio = body['directorio'].rstrip('/') + '/'
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=directorio)
    return {'statusCode': 200, 'mensaje': f'Directorio {directorio} creado en {bucket}'}
