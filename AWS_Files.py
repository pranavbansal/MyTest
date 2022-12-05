from fileinput import filename
import boto3
#login into the awscli using terminal 
s3 = boto3.resource("s3")
bucket = s3.bucket("nameofthebucket")
# upload file
bucket.upload_file(key="filename",filename="./path/filename")
#download file
bucket.download_file(key="filename",filename="./path/filename")


