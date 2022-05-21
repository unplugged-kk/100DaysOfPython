import subprocess

completed = subprocess.run(["ls", "-altrh"], capture_output=True, text=True)
other_script = subprocess.run(
    ["python3", "other.py"], capture_output=True, text=True)
print(type(completed))
print("args", completed.args)
print("returncode", completed.returncode)
print("stderr", completed.stderr)
print("stdout", completed.stdout)
print(other_script)
