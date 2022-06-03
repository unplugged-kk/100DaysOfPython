import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")
ec2_con_cli = aws_mgmt_con.client(service_name="ec2", region_name="us-east-1")
ec2_con_re = aws_mgmt_con.resource(service_name="ec2", region_name="us-east-1")

np_servers = []

f1 = {"Name": "tag:Name", "Values": ['Non_Prod']}

for instances in ec2_con_re.instances.filter(Filters=[f1]):
    np_servers.append(instances.id)

print(np_servers)

print("#################################")
# if we want to start perticular instances then there is no option in resource we need to use client object

np_server_ids = []

for each_item in ec2_con_cli.describe_instances(Filters=[f1])['Reservations']:
    for each_in in each_item['Instances']:
        # This line not required just to verify the instance ids are getting collected or not
        print(each_in['InstanceId'])
        np_server_ids.append(each_in['InstanceId'])

print("**********************************")

print(np_server_ids)

# Best practice  is using waiters with client object , client waiters can wait upto 10 mins if instances are taking more time we have to handle with exceptions
waiters = ec2_con_cli.get_waiter('instance_running')
ec2_con_cli.start_instances(InstanceIds=np_server_ids)
print("Starting all instances with ids: ", np_server_ids)
waiters.wait(InstanceIds=np_server_ids)
print("All Non Prod instances are up and running ")
