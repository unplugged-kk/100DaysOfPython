from pathlib import Path
from zipfile import ZipFile

# Creating zip file
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("module").rglob("*.*"):
#         zip.write(path)

# Reading zip file

with ZipFile("files.zip", "r") as zip:
    print(zip.namelist())
    info = zip.getinfo("module/ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_type)
    zip.extractall("extract")
