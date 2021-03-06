'''
- similar to server
- but it does not use bind() to attack its, socket to an address. 
- It uses sendto() to deliver its message directly to the server and
recvfrom() to receive the response.
'''

import socket, sys 
# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = b'This is the message. It will be repeated.'


try:
    # Send data.
    print("sending {!r}".format(message))
    send = sock.sendto(message, server_address)
    
    # Receive response
    print("waiting to receive")
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data))
finally:
    print("closing socket")
    sock.close()