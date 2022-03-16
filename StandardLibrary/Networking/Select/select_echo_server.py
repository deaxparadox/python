'''
- creating a non-blocking TCP/IP socket and configuring it to listen on an address.
'''

import select, socket, sys, queue


# Create a TCP/IP socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Bind the socket to the port.
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address), file=sys.stderr)
server.bind(server_address)

# Listen for incoming connection
server.listen(5)

'''
- The arguments to select() are three lists containing communication channels to 
monitor. 
- The first is a list of the objects to be checked for incoming data to  be read,
the second contains objects that will receive outgoing data when there is room in their
buffers, and the third includes those objects that may have an error (usually
combination of the input and output channel objects.)
- The next step is to set up the lists containig input sources and output destinations
to be passed to select().
'''

# Socket from which we expect to read.
inputs = [server]

# Socket to which we expect to write.
outputs = []

'''
- Connections are added to and removed from these lists by the server main loop.
- Since this version of the server will wait for a socket to become writable before sending any
data (instead of immediately sending the reply), each output connection needs a queue to act as
a buffer for the data to be send through it.
'''

# Outgoing message queues (socket:Queue)
message_queues = {}

# The main portion of the server program loops, calling select() to block and wait for network activity.
while inputs:
    # wait for at least one of the sockets to be 
    # ready for processing.
    print("waiting for the next event", file=sys.stderr)
    readable, writable, exceptional = select.select(inputs, outputs, inputs)
    
    '''
    - The "readable" socket represent three possible cases
    - If the socket is the main "server" socket, then the "readable" condition
    means it is ready to accept another incoming connection.
    - In addition to adding the new connection to the list of inputs to monitor, 
    this section sets the client cocket to not block.
    '''
    
    # Handle inputs,.
    for s in readable:
        if s is server:
            # A "readable" socket is ready to accept a connection.
            connection, client_address = s.accept()
            print(" connection from", client_address, file=sys.stderr)
            connection.setblocking(0)
            inputs.append(connection)
            
            # Give the connection a queu for data
            # we want to send.
            message_queues[connection] = queue.Queue()
        
        else:
            '''
            - The next case is an established connection with a client that has send data.
            - The data is read with recv(), then placed on the queue so it can be sent through
            the socket and back to the client.
            '''
            data = s.recv(1024)
            if data:
                # A readable client socket has data.
                print(" received {!r} from {}".format(data, s.getpeername()), file=sys.stderr)
                message_queues[s].put(data)
                # Add output channel for response.
                if s not in outputs:
                    outputs.append(s)
                    
            else:
                """
                - A readable socket that returns no data from recv() is from a client that has disconnected,
                and the stream is ready to be closed.
                """
                # Interpret empty result as closed connection.
                print(' closing', client_address, file=sys.stderr)
                # stop listening for input on the connection.
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                s.close()
                
                # Remove message queue.
                del message_queues[s]
                
    
    '''
    - There are few cases for writable connections.
    - IF the queue holds dadta intended for a connection, the next message is sent.
    - Otherwise, the connection isremoved from the list of output connections so that
    the next time through the loop select() does not indicate that the socket is ready 
    to send data.
    '''
    
    # Handle output
    for s in writable:
        try:
            next_msg = message_queues[s].get_nowait()
        except queue.Empty:
            # No messages waiting, so stop checking
            # for writability 
            print(' ', s.getpeername(), 'queue empty', file=sys.stderr)
            
        else:
            print(' sending {!r} to {}'.format(next_msg, s.getpeername()), file=sys.stderr)
            s.send(next_msg)
            
    '''
    - Finally, sockets in the exceptional lists are closed.
    '''
    # Handle "exceptional conditions."
    for s in exceptional:
        print("exception condition on", s.getpeername(), file=sys.stderr)
        # step listening for input on the connection.
        inputs.remove(s)
        if s in outputs:
            outputs.remove(s)
        s.close()
        
        # Remove message queue
        del message_queues[s]