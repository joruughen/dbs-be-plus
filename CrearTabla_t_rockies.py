import boto3

# Crear un cliente de DynamoDB
dynamodb = boto3.client('dynamodb')


response = dynamodb.create_table(
    TableName='t_rockies',
    AttributeDefinitions=[
        {'AttributeName': 'tenant_id', 'AttributeType': 'S'},
        {'AttributeName': 'student_id', 'AttributeType': 'S'},
        {'AttributeName': 'level', 'AttributeType': 'N'},
        {'AttributeName': 'experience', 'AttributeType': 'N'}
    ],
    KeySchema=[
        {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
        {'AttributeName': 'student_id', 'KeyType': 'RANGE'}
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'level_index',
            'KeySchema': [
                {'AttributeName': 'level', 'KeyType': 'HASH'},
                {'AttributeName': 'tenant_id', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'},
        }
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'experience_index',
            'KeySchema': [
                {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
                {'AttributeName': 'experience', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'},
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print("Tabla `t_rockies` creada:", response)
