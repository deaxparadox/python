import subprocess 

complete = subprocess.run("echo $HOME", shell=True)
print("returncode:", complete.returncode)