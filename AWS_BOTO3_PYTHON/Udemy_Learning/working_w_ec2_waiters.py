import boto3

aws_mgmt_console = boto3.session.Session(profile_name="syler")
ec2_con_cli = aws_mgmt_console.client(
    service_name="ec2", region_name="us-east-1")
ec2_con_re = aws_mgmt_console.resource(
    service_name="ec2", region_name="us-east-1")

instance_id = input("Please enter EC2 instance Id: ")
instance_ob = ec2_con_re.Instance(instance_id)
print(f"Starting {instance_id} ......")
instance_ob.start()

# The while block is called as waiter , in stead of using this long logic we can use boto3 waiter

# while True:
#     instance_obj = ec2_con_re.Instance(instance_id)
#     print("The current status of EC2 instance is: ",
#           instance_obj.state['Name'])
#     if instance_obj.state['Name'] == "running":
#         break
#     print("Waiting for EC2 server to come up")
#     time.sleep(5)

# boto3 waiter !!

# Resource waits for 200 secs (40 checks after 5 sec)
instance_ob.wait_until_running()

print(f"The EC2 instance {instance_id} is Up & running now !!")
