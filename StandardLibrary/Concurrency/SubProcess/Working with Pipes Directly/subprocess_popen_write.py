import subprocess 
print("write:")
proc = subprocess.Popen(
    ['cat', '-'],
    stdin=subprocess.PIPE,
)

def add_encode(data: str = None):
    add = input('Enter some data: ')
    add_nl = add+'\n'
    return add_nl.encode('utf-8')

# proc.communicate('stdin: to stdin\n'.encode('utf-8'))

proc.communicate(
    input=add_encode()
)