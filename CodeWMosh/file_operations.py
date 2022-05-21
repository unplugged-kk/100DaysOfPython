from pathlib import Path
from time import ctime

path = Path("/Users/kishorekumarbehera/Desktop/Tools/SYLER_GITHUB/100DaysOfPython/CodeWMosh/module/ecommerce/shopping/sales.py")

# path.exists()
# path.rename("sales_demo.py")
# path.unlink()

print(path.stat())
print(ctime(path.stat().st_ctime))
