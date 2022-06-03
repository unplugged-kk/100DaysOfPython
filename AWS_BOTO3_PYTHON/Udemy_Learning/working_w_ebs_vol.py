from logging import Filter
import boto3

aws_mgmt_con = boto3.session.Session(profile_name="syler")
ec2_con_re = aws_mgmt_con.resource(service_name="ec2", region_name="us-east-1")

# The script removed unused and untagged volumes

# we can find volumes with tags via filter but for volumes without tags we can't find it via filter

# ebs_untagged = {"Name:": "tag:Name", "Values": ['']}
ebs_unused = {"Name": "status", "Values": ['available']}

for each_vol in ec2_con_re.volumes.filter(Filters=[ebs_unused]):
    if not each_vol.tags:
        print(each_vol.id, each_vol.state, each_vol.tags)
        print("Deleting Unused and Untagged Volumes")
        each_vol.delete()

print("Deleted all unused untagged volumes. ")
