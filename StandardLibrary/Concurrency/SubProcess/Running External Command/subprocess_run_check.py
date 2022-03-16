import subprocess

# subprocess.run(['false'], check=True)
try:
    subprocess.run(['false'], check=False)
except subprocess.CalledProcessError as err:
    print("ERROR:", err)