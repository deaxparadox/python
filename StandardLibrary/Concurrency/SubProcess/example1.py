import subprocess
import argparse

def arg():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='file')
    return parser.parse_args()
args = arg()

file = "for.sh"
cmd = [
    ['gnome-terminal', '--', 'bash', args.file]
]

for c in cmd:
    subprocess.Popen(
        c
    )