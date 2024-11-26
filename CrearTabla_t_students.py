import boto3

# Crear un cliente de DynamoDB
dynamodb = boto3.client('dynamodb')

for stage in ['dev', 'test', 'prod']:
    import boto3

    # Crear un cliente de DynamoDB
    dynamodb = boto3.client('dynamodb')


    response = dynamodb.create_table(
    TableName=f'{stage}_t_students',
        AttributeDefinitions=[
            {'AttributeName': 'tenant_id', 'AttributeType': 'S'},
            {'AttributeName': 'student_id', 'AttributeType': 'S'},
            {'AttributeName': 'student_email', 'AttributeType': 'S'},
            {'AttributeName': 'creation_date', 'AttributeType': 'S'},
        ],
        KeySchema=[
            {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
            {'AttributeName': 'student_id', 'KeyType': 'RANGE'}
        ],
        GlobalSecondaryIndexes=[
            {
                'IndexName': 'student_email_index',
                'KeySchema': [
                    {'AttributeName': 'student_email', 'KeyType': 'HASH'},
                    {'AttributeName': 'tenant_id', 'KeyType': 'RANGE'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
            }
        ],
        LocalSecondaryIndexes=[
            {
                'IndexName': 'creation_date_index',
                'KeySchema': [
                    {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
                    {'AttributeName': 'creation_date', 'KeyType': 'RANGE'}
                ],
                'Projection': {'ProjectionType': 'ALL'},
            }
        ],
        BillingMode='PAY_PER_REQUEST'  # On-Demand mode
    )

    print("Tabla `t_students` creada:", response)
