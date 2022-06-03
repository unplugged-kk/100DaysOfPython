from cgi import print_arguments
from logging import Filter
import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")
ec2_con_cli = aws_mgmt_con.client(service_name="ec2", region_name="us-east-1")

# The script removed unused and untagged volumes

# we can find volumes with tags via filter but for volumes without tags we can't find it via filter

# ebs_untagged = {"Name:": "tag:Name", "Values": ['']}
# ebs_unused = {"Name": "status", "Values": ['available']}

# for each_vol in ec2_con_cli.volumes.filter(Filters=[ebs_unused]):
#     if not each_vol.tags:
#         print(each_vol.id, each_vol.state, each_vol.tags)
#         print("Deleting Unused and Untagged Volumes")
#         each_vol.delete()

# print("Deleted all unused untagged volumes. ")

for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    # print(each_item)
    if not "Tags" in each_item and each_item['State'] == 'available':
        print(each_item['VolumeId'])
        print("Deleting Untagged and Available Volumes")
        ec2_con_cli.delete_volume(VolumeId=each_item['VolumeId'])
        print("Deleted Untagged and Unused Volumes")
