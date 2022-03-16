'''
- The first step when establing a multicast receiver is to craete the UDP socket.
- After the regular socket is created and bounded to a port, it can be added to 
the multicast group by using setsockopt() to change the IP_ADD_MEMBERSHIP option.
- THe option value is the 8-byte packed representation of the multicast group address, 
followed by thenetwork interface on which the server should listen for the traffic, 
identified by its IP address. 
- In this case, therecevier listens on all interface using INADDR_ANY
'''

import socket, struct, sys 

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket 
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address.
sock.bind(server_address)

# Tell the operating system to add the socket to 
# the multicast group on all interfaces
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL',group, socket.INADDR_ANY)
sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)

# Receive/responed loop
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(1024)
    print('recevied {} bytes from {}'.format(
        len(data), address
    ))
    print(data)
    
    print("sending acknowledgement to", address)
    sock.sendto(b'ack', address)
    
'''The main loop for the receiver is just like regular UDP echo server.'''