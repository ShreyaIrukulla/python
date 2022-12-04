import boto3

iam = boto3.client('iam')

response = iam.attach_user_policy(
    UserName = 'CarlosSalazar',
    PolicyArn = 'arn:aws:iam::846457329613:policy/CarlosSalazar'
)

print(response)