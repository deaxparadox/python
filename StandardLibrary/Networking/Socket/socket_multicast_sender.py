"""
- The modified echo client in the next example will send a message to a 
multicast group, then report all of the reponses it receives. Since it has
no way of know how many responses to expect, it uses a timeout vallue for
the socket to avoid blocking indefinitely while waiting for an answer.

- The socket also needs to be configured with a time-to-line (TTL) for the 
messages.
- The TTL controls how many networks will receive the packet.
- Set the TTL with the IP_MULTICAST_TTL option and setsockopt().
- The default 1, means that the packets are not forwarded by the router
beyond the current network segment.
- The TTL value can range up to 255 and should be packed into a single byte.
"""

import socket, struct, sys 

message = b'very important data'
multicast_group = ('224.3.29.71', 10000)

# Create the datagram socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block @
# indefinitely when trying to receive data.
sock.settimeout(0.2)

# Set the time-to-live for messages to 1 so they do not 
# go past the local network setment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:
    # send data to the multicast group
    print('sending {!r}'.format(message))
    sent = sock.sendto(message, multicast_group)
    
    # Look for responses from all recipients.
    while True:
        print("waiting to receive")
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break 
        else:
            print('recevied {!r} from {}'.format(
                data, server
            ))
finally:
    print('closing socket')
    sock.close()
    
'''
The rest of the sender loks like the UDP echo client, except thta it expects
multiple responses. It uses a loop to call recvfrom() untill it timeout.
'''

