import paramiko
import os

password = os.environ.get('BASTION_PASS')

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname="syler-bastion.eastasia.cloudapp.azure.com",
            username="kishore", password=password) .  # key_filename=ssh.key_filename can also be used here instead of password

stdin, stdout, stderr = ssh.exec_command("free -m")
print(stdout.readlines())
ssh.close
