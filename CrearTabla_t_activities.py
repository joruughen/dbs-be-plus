import boto3

# Crear un cliente de DynamoDB
dynamodb = boto3.client('dynamodb')


response = dynamodb.create_table(
    TableName='t_activities',
    AttributeDefinitions=[
        {'AttributeName': 'tenant_id', 'AttributeType': 'S'},
        {'AttributeName': 'activity_id', 'AttributeType': 'S'},
        {'AttributeName': 'student_id', 'AttributeType': 'S'},
        {'AttributeName': 'activity_type', 'AttributeType': 'S'}
    ],
    KeySchema=[
        {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
        {'AttributeName': 'activity_id', 'KeyType': 'RANGE'}
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'student_id_index',
            'KeySchema': [
                {'AttributeName': 'student_id', 'KeyType': 'HASH'},
                {'AttributeName': 'activity_id', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'},
        }
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'activity_type_index',
            'KeySchema': [
                {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
                {'AttributeName': 'activity_type', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'},
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print("Tabla `t_activities` creada:", response)
