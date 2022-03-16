import socket, sys 

def socket_echo_server():
    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to the post.
    server_address = ('localhost', 10000)
    print("starting up on {} port {}".format(*server_address))
    sock.bind(server_address)
    
    # Listen for imcoming connections.
    sock.listen(1)
    
    while True:
        # Wait for a connection
        print("waiting for a connection")
        connection, client_address = sock.accept()
        try:
            print("connection from", client_address)
            
            # Receive the data in small chunks and retransmit it.
            while True:
                data = connection.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print("sending data back to the client")
                    connection.sendall(data)
                else:
                    print("no data from", client_address)
                    break 
                
        finally:
            # Clean up the connection 
            connection.close()
            
    """
    - Calling listen() puts the socket into server mode, and accept()
    waits for an incomming connection.
    - The integer argument is the number of connections the system should queue up in the 
    background before rejecting new clients.
    
    - accept() returns an open connection between the server and the client, along 
    with the client's address.
    - The connection is actually a different socket on another port (assigned by kernel)
    - Data is read from the connection with recv() and transmitted with sendall().
    
    - When communication with a client ends, the connection needs to be cleaned up using 
    close().
    - used a try:finally block to ensure that close() is always called, even in the even of an
    error.
    """


if __name__=="__main__":
    socket_echo_server()