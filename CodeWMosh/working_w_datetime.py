from datetime import datetime
import time

dt = datetime(2018, 1, 2)
dt = datetime.now()
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())

print(f"{dt.year}/{dt.month}")
