import socket, sys 

messages = [
    'This is message',
    'It will be send',
    'parts.',
]

server_address = ('localhost', 10000)

# Create a TCP/IP socket.
socks = [
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
    socket.socket(socket.AF_INET, socket.SOCK_STREAM),
]

# Connect the socket to the prot where the server is listening.
print("connecting to {} port {}".format(*server_address), file=sys.stderr)

for s in socks:
    s.connect(server_address)
    
'''
- Next, it sends one piece of the message at a time via each socket and 
reads all responses avaiable after writing new data.
'''

for message in messages:
    outgoing_data = message.encode()
    
    # Send messages on both sockets.
    for s in socks:
        print("{}: sending {!r}".format(s.getsockname(), outgoing_data), file=sys.stderr)
        s.send(outgoing_data)
    
    # Read responses on both sockets.
    for s in socks:
        data = s.recv(1024)
        print("{}: recevied {!r}".format(s.getsockname(), data), file=sys.stderr)
        
        if not data:
            print("closing socket", s.getsockname(), file=sys.stderr)
            s.close()