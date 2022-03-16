import socket, sys, time 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the  server is listening 
server_address = ("localhost", 10000)
print("connecting to {} port {}".format(*server_address), file=sys.stderr)
sock.connect(server_address)
time.sleep(1)
messages = [
    'Part one of the message.',
    'Part two of the message.',
]
amount_expected = len(''.join(messages))
try:
    # SEnd data
    for message in messages:
        data = message.encode()
        print("sending {!r}".format(data), file=sys.stderr)
        sock.sendall(data)
        time.sleep(1.5)
    # look for the reponse
    amount_received = 0
    
    while amount_received<amount_expected:
        data = sock.recv(16)
        amount_received+=len(data)
        print("received {!r}".format(data), file=sys.stderr)
finally:
    print("closing socket", file=sys.stderr)
    sock.close()