import boto3, json, base64

def lambda_handler(event, context):
    body = json.loads(event['body']) if isinstance(event.get('body'), str) else event
    bucket = body['bucket']
    directorio = body['directorio'].rstrip('/') + '/'
    nombre = body['nombre']
    contenido = base64.b64decode(body['contenido_base64'])
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=directorio + nombre, Body=contenido)
    return {'statusCode': 200, 'mensaje': f'{nombre} subido a {bucket}/{directorio}'}
