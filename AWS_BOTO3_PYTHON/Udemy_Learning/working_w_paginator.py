import boto3

# paginator are used when we have to get more data . usually client and session have a limitation for each resources which varies.
# usually if the count is more than 200 its better to use paginators.
session = boto3.session.Session(profile_name="syler")

# Use paginator to get list of IAM users

iam_cli = session.client("iam")
paginator = iam_cli.get_paginator('list_users')
for each_page in paginator.paginate():
    # print(each_page['Users'])
    for each_user in each_page['Users']:
        print(each_user['UserName'])

# Use paginators to get list of instances

ec2_cli = session.client(service_name="ec2", region_name="us-east-1")
ec2_pag = ec2_cli.get_paginator('describe_instances')
for each_page in ec2_pag.paginate():
    for instances in each_page['Reservations']:
        for each_instance in instances['Instances']:
            print(each_instance['InstanceId'])
