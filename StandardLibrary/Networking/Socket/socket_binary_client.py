'''
- Sockets transmit streams of bytes.
- Those bytes can contains text messages encoded as bytes, or they can be
made up of binary data that has been packed into a buffer with struct to
prepare it for transmission
- This client program encodes an integer, a string of two characters, and a
floating-point value into a sequence of bytes that can be passed to the socket
for transmission.
'''

import binascii, socket, struct, sys

# Create a TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
sock.connect(server_address)

values = (1, b'ab', 2.7)
packer = struct.Struct('I 2s f')
packed_data = packer.pack(*values)

print('values =', values)

try:
    # Send data.
    print("sending {!r}".format(binascii.hexlify(packed_data)))
    sock.sendall(packed_data)
finally:
    print("closing socker")
    sock.close()
    
'''
- The floating point value loses some precision as it is packed and unpacked, but otherwise
the data is trasmitted as expected.
- One thing to keep in mind is that depending on the value of the integer, it 
may be more efficient to convert it to text and then transmit that data, instead of 
using struct.
- The integer uses 1 bytes when represented as a string, but 4 bytes when packed
into the structure.
'''