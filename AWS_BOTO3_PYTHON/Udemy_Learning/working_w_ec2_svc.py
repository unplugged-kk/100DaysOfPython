from pprint import pprint
import boto3

aws_mgmt_console = boto3.session.Session(profile_name="syler")

# Using Client

ec2_con_cli = aws_mgmt_console.client(
    service_name="ec2", region_name="us-east-1")

# This way also works

# ec2_responses = ec2_con_cli.describe_instances()

# for ec2_response in ec2_responses['Reservations']:
#     for instance in ec2_response['Instances']:
#         print("Instance ID: " + instance['InstanceId'])
#         print(instance['LaunchTime'])
#         print(instance['Monitoring'])

ec2_responses = ec2_con_cli.describe_instances()['Reservations']

for each_item in ec2_responses:
    for item in each_item['Instances']:
        print("The Image id is: {}\nThe Instance Launch time is: {}\nThe Instance Id is : {}".format(
            item['ImageId'], item['LaunchTime'], item['InstanceId']))

ec2_vol = ec2_con_cli.describe_volumes()['Volumes']

for vol in ec2_vol:
    print("The Volume Iops is: {}\nThe Volume id is: {}\nThe Volume Size is: {}".format(
        vol['Iops'], vol['VolumeId'], vol['Size']))
