import boto3

aws_mgmt_con = boto3.session.Session(profile_name="default")
iam_con_re = aws_mgmt_con.resource(service_name="iam", region_name="us-east-1")

# List all users in IAM console
for iam_users in iam_con_re.users.all():
    print(iam_users)

# iam user details

iam_user_obj = iam_con_re.User("cloud_user")
print(iam_user_obj.user_name, iam_user_obj.user_id, iam_user_obj.policies,
      iam_user_obj.arn, iam_user_obj.create_date.strftime("%Y-%m-%d"))
