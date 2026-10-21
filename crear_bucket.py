import boto3, json

def lambda_handler(event, context):
    body = json.loads(event['body']) if isinstance(event.get('body'), str) else event
    bucket = body['bucket']
    s3 = boto3.client('s3')
    # En us-east-1 NO se usa CreateBucketConfiguration
    s3.create_bucket(Bucket=bucket)
    return {'statusCode': 200, 'mensaje': f'Bucket {bucket} creado'}
