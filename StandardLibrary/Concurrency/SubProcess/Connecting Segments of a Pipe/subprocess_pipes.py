import subprocess

filename = 'subprocess_pipes.py'

cat = subprocess.Popen(
    ['cat', f"{filename}"],
    stdout=subprocess.PIPE,
)
grep = subprocess.Popen(
    ['grep', '.. literalinclude::'],
    stdin=cat.stdout,
    stdout=subprocess.PIPE
)
cut = subprocess.Popen(
    ['cut', '-f', '3', '-d:'],
    stdin=grep.stdout,
    stdout=subprocess.PIPE
)
end_of_pipe = cut.stdout

print("Include files:")
for line in end_of_pipe:
    print(line.decode('utf-8').strip())