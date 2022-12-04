import boto3

iam = boto3.client('iam')

created_user = iam.create_user(
    UserName='CarlosSalazar',
    Tags=[
        {
            'Key': 'Env',
            'Value': 'Test'
        }
    ]
)
print(created_user)