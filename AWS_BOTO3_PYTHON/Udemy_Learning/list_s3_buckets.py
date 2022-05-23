import boto3

aws_mgmt_console = boto3.session.Session(profile_name="acg")
s3_console = aws_mgmt_console.resource("s3")

for bucket in s3_console.buckets.all():
    print(bucket.name)
