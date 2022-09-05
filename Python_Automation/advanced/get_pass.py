import getpass
# db_pass = getpass.getpass() #without prompt
db_pass = getpass.getpass(prompt="Enter database password: ")
print(f"the entered password is {db_pass}")
print(getpass.getuser())  # it checks the login user from os
