import boto3
s3 = boto3.resource('s3')
s3.meta.client.upload_file('D:\sample1.txt', 'shreyairukullabucket', 'sample1.txt')