from boto3.session import Session
import boto3

ACCESS_KEY = 'ABC'
SECRET_KEY = 'XYZ'

session = Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

# session is authenticated and can access the resource in question 
session.resource('s3')
s3.Bucket('bucket_name')
s3.download_file('k.png','/Users/username/Desktop/k.png')