import os
import argparse

# File with dir join
# dir_name = "/Users/kbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/Python_Automation"
# for dirpath, dirnames, filenames in os.walk(dir_name):
#     for file in filenames:
#         print(os.path.join(dirpath, file))

# Finding a perticular file in the directory

# dir_name = "/Users/kbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/Python_Automation"
# for dirpath, dirnames, filenames in os.walk(dir_name):
#     for file in filenames:
#         if file == "os_walk.py":
#             print(os.path.join(dirpath, file))

my_parser = argparse.ArgumentParser(
    description='Reading the Dir path to find the file')
my_parser.add_argument("pathname", help='Please enter the directory path')
my_parser.add_argument(
    "filesearch", help='Please enter the filename to search')

args = my_parser.parse_args()

for dirpath, dirnames, filenames in os.walk(args.pathname):
    for file in filenames:
        if file == args.filesearch:
            print(os.path.join(dirpath, file))
