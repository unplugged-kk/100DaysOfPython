import boto3
aws_mgmt_con = boto3.session.Session(profile_name="syler")

# iam,ec2,s3
iam_con_cli = aws_mgmt_con.client(service_name="iam", region_name="us-east-1")
ec2_con_cli = aws_mgmt_con.client(service_name="ec2", region_name="us-east-1")
s3_con_cli = aws_mgmt_con.client(service_name="s3", region_name="us-east-1")


# List all iam user using client object

response = iam_con_cli.list_users()
for each_item in response['Users']:
    print(each_item['UserName'])


# List all ec2 instance IDs using client object

ec2_response = ec2_con_cli.describe_instances()
for server in ec2_response['Reservations']:
    for instance in server['Instances']:
        print(instance['InstanceId'])

s3_response = s3_con_cli.list_buckets()
# print(s3_response)
for bucket in s3_response['Buckets']:
    print(bucket['Name'])
