import platform
import os


if platform.system() == "Windows":
    os.system("ls")
elif platform.system() == "Linux":
    os.system("dir")
elif platform.system() == "Darwin":
    os.system("ls -altrh")
else:
    print("Unsupported platform")
