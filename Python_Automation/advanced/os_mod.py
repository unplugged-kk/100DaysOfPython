import os
print(os.getcwd())
os.chdir("/Users/kishore/Desktop")
print(os.listdir())
# os.mkdir("Python_Script_Created_Dir")  #creating single directory
# os.makedirs("Python_Script_Created_Dir/xyz/abc")  # creating nested directory
# os.removedirs("Python_Script_Created_Dir/xyz")
print(os.getpid())
path = "/Users/kishore/Desktop"
print(os.path.basename(path))
print(os.path.dirname(path))

cmd = "date"
rt = os.system(cmd)  # used to execute os command
if rt == 0:
    print("The CMD executed successfully.")
else:
    print("The CMD failed")
