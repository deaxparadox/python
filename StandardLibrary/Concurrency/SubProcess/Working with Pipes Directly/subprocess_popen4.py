import subprocess

print("popen4")
proc = subprocess.Popen(
    'cat -; echo "to stderr" 1>&2',
    shell=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
msg = 'through stdin to stdout'.encode('utf-8')
stdout_value, stderr_value = proc.communicate(msg)
print("combined output:", repr(stdout_value.decode('utf-8')))
print("stderr value        :", repr(stderr_value.decode('utf-8')))