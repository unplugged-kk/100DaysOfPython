import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")

ec2_con_cli = aws_mgmt_con.client(service_name="ec2")
ec2_con_re = aws_mgmt_con.resource(service_name="ec2")

# print(dir(ec2_con_re))
# print(dir(ec2_con_re.meta))
# print(dir(ec2_con_re.meta.client))
for region in ec2_con_re.meta.client.describe_regions()['Regions']:
    print(region['RegionName'])
