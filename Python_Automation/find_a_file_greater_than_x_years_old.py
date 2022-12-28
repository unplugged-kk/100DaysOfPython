import os
import datetime

dir_path = "/Users/kbehera/Desktop/imp_docs"
max_age = 10
current_date = datetime.datetime.now()

for dirpath, dirnames, filenames in os.walk(dir_path):
    for file in filenames:
        comp_path = os.path.join(dirpath, file)
        file_stat = os.stat(comp_path)
        # print(file_stat)
        file_ctime = file_stat.st_ctime
        # print(file_ctime)

        file_creation_date = datetime.datetime.fromtimestamp(file_ctime)

        diff_in_days = (current_date - file_creation_date).days

        if diff_in_days > max_age:
            print(comp_path, diff_in_days)
