import subprocess
try:
    output = subprocess.check_output(
        'echo to stdout; echo to stderr 1>&2',
        # check=True,
        shell=True,
        stderr=subprocess.STDOUT,
    )
except subprocess.CalledProcessError as err:
    print("ERROR:", err)
else:
    print("Have {} bytes in stdout: {!r}".format(
        len(output),
        output.decode('utf-8')
    ))