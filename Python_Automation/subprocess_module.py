import subprocess
command = ["ls", "-altrh"]
sp = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE,
                      stderr=subprocess.PIPE, universal_newlines=True)
rt = sp.wait()
out, err = sp.communicate()
print(out)
print(err)
