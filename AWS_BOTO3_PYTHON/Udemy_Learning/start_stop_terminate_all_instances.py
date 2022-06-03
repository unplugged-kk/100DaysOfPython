from re import L
import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")
ec2_con_re = aws_mgmt_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cli = aws_mgmt_con.client(
    service_name="ec2", region_name="us-east-1")


all_instance_ids = []  # empty list

for instance_id in ec2_con_re.instances.all():  # gathering all instances from the aws console
    all_instance_ids.append(instance_id.id)


waiters = ec2_con_cli.get_waiter('instance_running')
ec2_con_re.instances.start()
print("Starting all instances")
waiters.wait(InstanceIds=all_instance_ids)
print("All instances are up and running ")
