import boto3

# aws_mgmt_con = boto3.session.Session(profile_name="syler")
# ec2_con_re = aws_mgmt_con.resource(service_name="ec2", region_name="us-east-1")
# ec2_con_cli = aws_mgmt_con.client(
#     service_name="ec2", region_name="us-east-1")

# the script is getting executed by iam  role we have created in aws console and attached to a ec2 instance. here boto3 is using default session.

ec2_con = boto3.resource(service_name="ec2", region_name="us-east-1")

for each_instance in ec2_con.instances.all():
    print(each_instance.id, each_instance.state)
