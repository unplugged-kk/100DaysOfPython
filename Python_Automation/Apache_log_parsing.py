import re
import csv
from collections import Counter
# use the correct one . this re for matching differs
logreg = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
logfile = "access.log"

with open(logfile) as f:
    fread = f.read()  # reading the file and stroring it
    # finding the ips present in the code.
    ip_list = re.findall(logreg, fread)
    with open("ipcount.csv", "w") as f:
        fwritercsv = csv.writer(f)
        fwritercsv.writerow("IP_ADDRESS", "COUNT")
    for k, v in Counter(ip_list).items():
        fwritercsv.writerow([k, v])
