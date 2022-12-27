import os

# File with dir join
# dir_name = "/Users/kbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/Python_Automation"
# for dirpath, dirnames, filenames in os.walk(dir_name):
#     for file in filenames:
#         print(os.path.join(dirpath, file))

# Finding a perticular file in the directory

dir_name = "/Users/kbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/Python_Automation"
for dirpath, dirnames, filenames in os.walk(dir_name):
    for file in filenames:
        if file == "os_walk.py":
            print(os.path.join(dirpath, file))
