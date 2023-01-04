import boto3
ec2 = boto3.resource("ec2")
instance = ec2.Instance('i-044c40ed5b45c69d6')
# print((dir(instance)))
print("stopping the instance")
instance.stop()
instance.wait_until_stopped()
print("EC2 instance stopped")
