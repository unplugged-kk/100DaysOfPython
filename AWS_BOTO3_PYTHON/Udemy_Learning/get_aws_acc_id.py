import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")

# Get aws Account ID

sts_console = aws_mgmt_con.client(service_name="sts", region_name="us-east-1")

response = sts_console.get_caller_identity()

# the O/P is dictionary it can be accessed via .get() method or using  the key in []
print(response.get('Account'))
print(response['Account'])
