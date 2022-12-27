import os

for dirpath, dirnames, filenames in os.walk("/Users/kbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/Python_Automation"):
    print(dirpath)
    print(dirnames)
    print(filenames)

print(list(os.walk("/Users/kbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/Python_Automation")))
