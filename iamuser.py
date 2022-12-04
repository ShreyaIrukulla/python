import boto3

iam_con=boto3.resource('iam')
for each_iam_user in iam_con.users.all():
    print(each_iam_user.name)