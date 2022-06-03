import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")
ec2_con_re = aws_mgmt_con.resource(service_name="ec2", region_name="us-east-1")
sts_console = aws_mgmt_con.client(service_name="sts", region_name="us-east-1")
response = sts_console.get_caller_identity()
syler_acc_id = response['Account']
print(syler_acc_id)

f_size = {"Name": "volume-size", "Values": ['1']}

# filtering ebs snapshots using snapshot size and account id ownership type. because snapshot.all() gives o/p as all snapshots (public, private,Own Snapshots)

for ebs_snaps in ec2_con_re.snapshots.filter(OwnerIds=[syler_acc_id], Filters=[f_size]):
    print(ebs_snaps)
