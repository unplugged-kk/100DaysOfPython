
# Manual Steps to see/list all iam users:
# ========================================
#   step1: Get AWS Management Console
#   Step2: Get IAM Console
#          Options: Users, Groups, roles......
# ========================================
import boto3

aws_mgmt_console = boto3.session.Session(profile_name="syler")
iam_console = aws_mgmt_console.resource('iam')

for user in iam_console.users.all():
    print(user.name)
