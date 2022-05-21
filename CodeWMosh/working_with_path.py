from pathlib import Path
path = Path("module/ecommerce/shopping/sales.py")

path.exists()
path.is_dir()
path.is_file()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.absolute)
