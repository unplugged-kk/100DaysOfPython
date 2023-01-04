import boto3

aws_client = boto3.client('ec2')

# response = aws_client.stop_instances(
#     InstanceIds=["i-044c40ed5b45c69d6"])

response = aws_client.start_instances(
    InstanceIds=["i-044c40ed5b45c69d6"])
