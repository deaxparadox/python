'''
- The socketpair() function is usefull for setttign up UDS socketsfor 
interprocess communication under Unix.
- It creates a pair of connected sockets that can be used to communicate 
between a parent process and a child process after the child is forked.
'''

import socket, os 

parent, child = socket.socketpair()

pid = os.fork()

if pid:
    print("in parent, sending message")
    child.close()
    parent.sendall(b'ping')
    response = parent.recv(1024)
    print("response from child:", parent)
    parent.close()
    
else:
    print('in child, waiting for message')
    parent.close()
    message = child.recv(1024)
    print("message from parent:", message)
    child.sendall(b'pong')
    child.close()
    
'''
- By default, a UDS socket is created.
- Alternatively, the caller can pass address family, socket type, 
and even protocol options to speciy how the sockets sockets should
be created.
'''