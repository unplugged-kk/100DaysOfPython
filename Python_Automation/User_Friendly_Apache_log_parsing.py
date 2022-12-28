import re
import csv
from collections import Counter
import argparse


my_parser = argparse.ArgumentParser(description="Reading the log file")
my_parser.add_argument(
    "logfile", help='Please provide a log file to parse', type=argparse.FileType('r'))  # for positional arguments we can use like --logfile
args = my_parser.parse_args()

# use the correct one . this re for matching differs
logreg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
# logfile = "access.log"

with args.logfile as f:
    fread = f.read()  # reading the file and stroring it
    # finding the ips present in the code.
    ip_list = re.findall(logreg, fread)
    with open("ipcount.csv", "w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow("IP_ADDRESS", "COUNT")
    for k, v in Counter(ip_list).items():
        fwritercsv.writerow([k, v])
