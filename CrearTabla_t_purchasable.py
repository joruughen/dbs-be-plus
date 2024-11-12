import boto3

# Crear un cliente de DynamoDB
dynamodb = boto3.client('dynamodb')


response = dynamodb.create_table(
    TableName='t_purchasable',
    AttributeDefinitions=[
        {'AttributeName': 'tenant_id', 'AttributeType': 'S'},
        {'AttributeName': 'store_type', 'AttributeType': 'S'},
        {'AttributeName': 'product_id', 'AttributeType': 'S'},
        {'AttributeName': 'price', 'AttributeType': 'N'}
    ],
    KeySchema=[
        {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
        {'AttributeName': 'store_type', 'KeyType': 'RANGE'}
    ],
    GlobalSecondaryIndexes=[
        {
            'IndexName': 'store_type_index',
            'KeySchema': [
                {'AttributeName': 'store_type', 'KeyType': 'HASH'},
                {'AttributeName': 'product_id', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'},
        }
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'price_index',
            'KeySchema': [
                {'AttributeName': 'tenant_id', 'KeyType': 'HASH'},
                {'AttributeName': 'price', 'KeyType': 'RANGE'}
            ],
            'Projection': {'ProjectionType': 'ALL'},
        }
    ],
    BillingMode='PAY_PER_REQUEST'
)

print("Tabla `t_purchasable` creada:", response)
