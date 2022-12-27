
# FileNotFoundError
# PermissionError
# IsDirectoryError

import os

# Try 1
# try:
#     open("/etc/init.d/")
# except Exception as e:
#     print(e)

# Try 2:

# print(os.path.exists("/Users/kbehera"))

# print(os.path.isfile("/Users/kbehera"))

# print(os.path.isdir("/Users/kbehera"))
filename = "/Users/kbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/Python_Automation/math.py"

if os.path.exists(filename) and os.path.isfile(filename):
    print("File exists")
else:
    print("File does not exist")
