"""UNIX DOMAIN SOCKETS
1. there are two essential difference between using a Unix domain socket
and an TCP/IP socket.
    - First, the address of the socket is a path on the file system, rather
    than a tuple contaning the server name and port.
    - Second, the node createdd in the file system to represent the socket p
    persists after the socket is closed, so it needs to be removed each time
    the server starts.
2. The socket needs to be created with address family AF_UNIX.
3. Bindings the socket and managing the incomming connections works the same 
way as with TCP/IP sockets.

"""
