import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")

iam_con_res = aws_mgmt_con.resource(
    service_name="iam", region_name="us-east-1")
s3_con_res = aws_mgmt_con.resource(service_name="s3", region_name="us-east-1")
ec2_con_res = aws_mgmt_con.resource(
    service_name="ec2", region_name="us-east-1")


# list all iam users

for each_item in iam_con_res.users.all():
    print(each_item.name)


# list all ec2 servers

for each_server in ec2_con_res.instances.all():
    print(each_server)


# list all s3 buckets
for each_bucket in s3_con_res.buckets.all():
    print(each_bucket.name)
# res_s3 =
