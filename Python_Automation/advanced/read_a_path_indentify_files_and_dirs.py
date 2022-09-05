from asyncore import poll3
import os
import sys
path = input("Enter your directory path: ")

if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print("Please provide a valid path")
    sys.exit()
# This script will work for only 3 items in the directory it will not work for more than 3 items. we need it to work dynamically.
# p1 = os.path.join(path, df_l[0])
# p2 = os.path.join(path, df_l[1])
# p3 = os.path.join(path, df_l[2])

# if os.path.isfile(p1):
#     print(f"{p1} is a file")
# else:
#     print(f"{p1} is a directory")

# if os.path.isfile(p2):
#     print(f"{p2} is a file")
# else:
#     print(f"{p2} is a directory")

# if os.path.isfile(p3):
#     print(f"{p3} is a file")
# else:
#     print(f"{p3} is a directory")

# below code works Dynamically

list_file_dir = os.listdir(path)
print("all the files and directories", list_file_dir)

for each_file_or_dir in list_file_dir:
    f_d_p = os.path.join(path, each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f"{f_d_p} is a file)")
    else:
        print(f"{f_d_p} is a directory")
