from warnings import filters
import boto3

aws_mgmt_cli = boto3.session.Session(profile_name="syler")
ec2_con_re = aws_mgmt_cli.resource(service_name="ec2", region_name="us-east-1")


# print(ec2_con_re.instances.all())  # it will create a iterable object

# for instances in ec2_con_re.instances.all():
#     print(instances)

# for ech in ec2_con_re.instances.limit(2):  #Not much practical use case but with the value it prints the instances from top of the list
#     print(ech)

f1 = {"Name": "instance-state-name", "Values": ['running']}

for each in ec2_con_re.instances.filter(Filters=[f1]):
    print(each)

print("=========================================")

f2 = {"Name": "instance-state-name", "Values": ['running', 'stopped']}

for instance in ec2_con_re.instances.filter(Filters=[f2]):
    print(instance)

f3 = {"Name": "instance-type", "Values": ['t2.micro']}

print("***************************************")

for instance_type in ec2_con_re.instances.filter(Filters=[f3]):
    print(instance_type)

print("###################################")

# This will provide intersection of f1 and f3 filter
for server in ec2_con_re.instances.filter(Filters=[f1, f3]):
    print(server)
