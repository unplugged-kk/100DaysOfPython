import boto3
from random import choice
import sys

# iam_console_re = aws_mgmt_console.resource(
#     service_name='iam', region_name="us-east-1")


def get_rand_passwd():
    len_of_password = 8
    valid_chars_for_password = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    return "".join(choice(valid_chars_for_password) for each_char in range(len_of_password))


def get_iam_client_obj():
    session = boto3.session.Session(profile_name="syler")
    iam_client = session.client(
        service_name='iam', region_name="us-east-1")
    return iam_client


def main():
    iam_client = get_iam_client_obj()
    iam_user_name = "juljul"
    passwd = get_rand_passwd()
    PolicyArn = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam_client.create_user(UserName=iam_user_name)
    except Exception as e:
        if e.response['Error']['Code'] == 'EntityAlreadyExists':
            print(f"Already Iam user with Name {iam_user_name} already exists")
            sys.exit(0)
        else:
            print("Please Verify the follwoing error and retry")
            print(e)
            sys.exit(0)
# IAM user with console login

    iam_client.create_login_profile(
        UserName=iam_user_name, Password=passwd, PasswordResetRequired=False)

# IAM User with access key
    response = iam_client.create_access_key(UserName=iam_user_name)

    print("AccessKeyId={}\nSecretAccessKey={}".format(
        response['AccessKey']['AccessKeyId'], response['AccessKey']['SecretAccessKey']))

    iam_client.attach_user_policy(UserName=iam_user_name, PolicyArn=PolicyArn)

    # Dont print password and all in actual use case store it in csv files and then share
    print("IAM User Name={} and Password={}".format(iam_user_name, passwd))
    return None


if __name__ == "__main__":
    main()
