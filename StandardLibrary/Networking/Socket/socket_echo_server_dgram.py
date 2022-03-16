"""it simple needs ot use bind() to associate its socket with a port,
and then wait for individual messages."""

import socket, sys 

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port.
server_address = ("localhost", 10000)
print("starting up on {} port {}".format(*server_address))
sock.bind(server_address)

while True:
    print("\nwaiting to receive message")
    data, address = sock.recvfrom(4096)
    
    print("received {} bytes from {}".format(
        len(data), address
    ))
    print(data)
    
    if data:
        sent = sock.sendto(data, address)
        print("sent {} bytess back to {}".format(sent, address))
        
"""
- Messages are read from the socket using recvfrom, which returns the data,
as well as the address ofthe client from which it was sent.
"""