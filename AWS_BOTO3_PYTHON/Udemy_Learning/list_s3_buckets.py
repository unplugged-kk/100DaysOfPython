import boto3

aws_mgmt_console = boto3.session.Session(profile_name="syler")
# s3_console = aws_mgmt_console.resource("s3")
s3_console_re = aws_mgmt_console.resource(
    service_name="s3", region_name="us-east-1")

for bucket in s3_console_re.buckets.all():
    print(bucket.name)
