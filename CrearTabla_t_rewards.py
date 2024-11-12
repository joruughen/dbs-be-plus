import boto3

# Crear un cliente de DynamoDB
dynamodb = boto3.client('dynamodb')


response = dynamodb.create_table(
    TableName='t_rewards',
    AttributeDefinitions=[
        {'AttributeName': 'tenant_id', 'AttributeType': 'S'},
        {'AttributeName': 'reward_id', 'AttributeType': 'S'},
        {'AttributeName': 'student_id', 'AttributeType': 'S'},
        {'AttributeName': 'experience', 'AttributeType': 'N'},
        {'AttributeName': 'activity_id', 'AttributeType': 'S'}
    ],
    KeySchema=[
        {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
        {'AttributeName': 'reward_id', 'KeyType': 'RANGE'}
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

print("Tabla `t_rewards` creada:", response)
