import boto3
import sys
aws_mgmt_console = boto3.session.Session(profile_name="syler")

ec2_con_re = aws_mgmt_console.resource(
    service_name="ec2", region_name="us-east-1")
ec2_con_cli = aws_mgmt_console.client(
    service_name="ec2", region_name="us-east-1")

while True:
    print("The script performs following actions in ec2 instance")
    print("""
    1. start
    2. stop 
    3. reboot
    4. exit
    """)
    opt = int(input("Enter your Option: "))
    if opt == 1:
        instance_id = input('Enter your EC2 Instance Id: ')
        instance_obj = ec2_con_re.Instance(instance_id)
        instance_obj.start()
        print(f"Starting {instance_id} instance ......")
    elif opt == 2:
        instance_id = input('Enter your EC2 Instance Id: ')
        instance_obj = ec2_con_re.Instance(instance_id)
        instance_obj.stop()
        print(f"Stopping {instance_id} instance .....")
    elif opt == 3:
        instance_id = input('Enter your EC2 Instance Id: ')
        instance_obj = ec2_con_re.Instance(instance_id)
        instance_obj.reboot()
        print(f"Rebooting {instance_id} instance .....")
    elif opt == 4:
        print("Thank your for using the script")
        sys.exit()
    else:
        print("Your Option is Invalid , Try Valid Options")
