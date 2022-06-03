import boto3
import datetime
aws_mgmt_con = boto3.session.Session(profile_name="syler")
ec2_con_re = aws_mgmt_con.resource(service_name="ec2", region_name="us-east-1")
sts_console = aws_mgmt_con.client(service_name="sts", region_name="us-east-1")
response = sts_console.get_caller_identity()
syler_acc_id = response['Account']
today = datetime.datetime.now()
# we are convering it to string only for if operation as ebs_snaps.start_time.strftime("%Y-%m-%d %H:%M:%S") is a str type
start_time = str(datetime.datetime(
    today.year, today.month, today.day, 11, 19, 43))  # used 11(H) ,19(M), 43(S) here as my snapshots are created at this time . you can use any time
print(start_time)

# The script is useful for checking if the snapshots are created at required time or not

for ebs_snaps in ec2_con_re.snapshots.filter(OwnerIds=[syler_acc_id]):
    if ebs_snaps.start_time.strftime("%Y-%m-%d %H:%M:%S") == start_time:
        print(ebs_snaps.id, ebs_snaps.start_time.strftime("%Y-%m-%d %H:%M:%S"))
