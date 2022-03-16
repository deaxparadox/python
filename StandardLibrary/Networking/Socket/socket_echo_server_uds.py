
import socket, sys, os

server_address = './uds_socket'
# Make sure the socket doesnot already exit.
try:
    os.unlink(server_address)
except OSError:
    if os.path.exists(server_address):
        raise 
    
# Create a UDS socket
sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

# Bind the socket to the address
print("starting up on {}".format(server_address))
sock.bind(server_address)

# Listen for incoming connections.
sock.listen(1)

while True:
    # waiting for a connection.
    print("waiting for a connecton")
    connection, client_address = sock.accept()
    try:
        print("connection from", client_address)
        
        # Recevie the data in small chunks, and retransmit it.
        while True:
            data = connection.recv(16)
            print("recevied {!r}".format(data))
            if data:
                print("sending data back to the client.")
                connection.sendall(data)
            else:
                print("no data from", client_address)
                break
    finally:
        # clean up the connectio
        connection.close()