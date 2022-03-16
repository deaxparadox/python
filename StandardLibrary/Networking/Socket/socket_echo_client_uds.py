"""
- The should assume that the file system node for the socket exists, since
the server creates it by binding to the address.
"""

import socket, sys 
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening 
server_address = './uds_socket'
print("connecting to {}".format(server_address))
try:
    sock.connect(server_address)
except socket.error as msg:
    print(msg)
    sys.exit(1)
    
try:
    # Send data 
    message = b'This is the message. It will be repested.'
    print('sending {!r}'.format(message))
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print("received {!r}".format(data))
finally:
    print("closing socket")
    sock.close()