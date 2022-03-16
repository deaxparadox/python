'''
- The echo server example presentedther uses the application data in the SelectorKey
to register a callback function to be invoked on the new event.
- The main loop gets the callback from the key and passes the socket and event mask to 
it.
- As the server starts, it registers the accept() function to be called for read events 
on the main server socket.
- Accepting the connection produces an new socket, which is then registered with the read() 
function as a callback for read events.
'''

import selectors, socket

mysel = selectors.DefaultSelector()
keep_running = True 

def read(connection, mask):
    "Callback for read events"
    global keep_running
    
    client_address = connection.getpeername()
    print('read({})'.format(client_address))
    data = connection.recv(1024)
    if data:
        # A readable client socket has data.
        print('     received {!r}'.format(data))
        connection.sendall(data)
    else:
        # Interpret empty result as closed connection.
        print("     closing")
        mysel.unregister(connection)
        connection.close()
        # Tell the main loop to stop.
        keep_running = False 
        
def accept(sock, mask):
    "Call back for new connection"
    new_connection, addr = sock.accept()
    print("     accept({})".format(addr))
    new_connection.setblocking(False)
    mysel.register(new_connection, selectors.EVENT_READ, read)
    
server_address = ('localhost', 10000)
print("starting up on {} port {}".format(*server_address))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.bind(server_address)
server.listen(5)

mysel.register(server, selectors.EVENT_READ, accept)

while keep_running:
    print('waiting for I/O')
    for key,mask in mysel.select(timeout=1):
        callback = key.data
        callback(key.fileobj, mask)

print('shutting down')
mysel.close()

'''
- If read() does not receive any data from the socket, it interprets the read 
event as the other side of the connection being closed instead of sending data.
- Consequently, it removes the socket from the selector and closes it.
- Because it is only a example program, this server also shuts itself down after 
it has finished communicating with a single client.
'''