import boto3

# Crear un cliente de DynamoDB
dynamodb = boto3.client('dynamodb')

for stage in ['dev', 'test', 'prod']:
    import boto3

    # Crear un cliente de DynamoDB
    dynamodb = boto3.client('dynamodb')

    # Crear la tabla t_access_tokens
    response = dynamodb.create_table(
    TableName=f'{stage}_t_access_tokens',
        AttributeDefinitions=[
            {
                'AttributeName': 'token',
                'AttributeType': 'S'  # Tipo S indica que es un string
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'token',
                'KeyType': 'HASH'  # Clave de partición
            }
        ],
        BillingMode='PAY_PER_REQUEST'  # Configuración On-Demand
    )

    print("Tabla `t_access_tokens` creada:", response)
