import socket, sys 

# Create a TCP/IP socket.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server
# given by the caller.
server_address = (sys.argv[1], 10000)
print("connecting to {} port {}".format(*server_address))
sock.connect(server_address)

try:
    message = b'This is the message. It will be repeated.'
    print("sending {!r}".format(message))
    sock.sendall(message)
    
    amount_recevied = 0
    amount_expected = len(message)
    while amount_recevied < amount_recevied:
         data = sock.recv(16)
         print("received {!r}".format(data))
         
finally:
    sock.close()