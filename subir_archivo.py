import boto3, json, base64

def lambda_handler(event, context):
    body = event.get('body', event)
    if isinstance(body, str):
        body = json.loads(body)
    bucket = body['bucket']
    directorio = body['directorio'].rstrip('/') + '/'
    nombre = body['nombre']
    contenido = base64.b64decode(body['contenido_base64'])
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucket, Key=directorio + nombre, Body=contenido)
    return {'statusCode': 200, 'mensaje': f'{nombre} subido a {bucket}/{directorio}'}
