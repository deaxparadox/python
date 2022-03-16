"""Socket: Network Communication
    - The socket module exposese the low-level C API communicating over a network
    using the BSDsocket interface. It includes the socket class, for handking the actual
    data channel, as well as function for network relatived task such as 
    task such as converting a server's name to an address and formating data to be sent 
    across the network.
"""

"""Addressing, Protocol Families and Socket Types
    - A socket is one endpoint of a communication channel used by  programs to pass 
    data back and froth locally or across the Internet. 
    - Sockets have two primary properties controlling the way they send the data:
        1. Address family:
            - Controls the OSI network layer protocol used and 
        2. Socket family
            - Controls the transport layer protocol.
            
    - Python support three address families:
        1. AF_INET
            - used for IPv4 Internet addressing.
            - IPv4 address are 4 bytes long and are usually represented by as a 
            sequence of four number, onr per octet, separated by dots.
        2. AF_INET6
            - used for IPv6 Internet addressing
            - supports 128-bit addresses, traffic shaping, and routing features not 
            available under IPv4
        3. AF_UNIX
            - is the family of Unix Domain Sockets (UDS)
            - an interprocess communication protocol available on POSIX-compliant 
            systems.
            - Implementation of UDS typically allows the operating system to pass data
            directly from process to process. without going through the network stack.
            - more efficient then using AF_INET, 
            - but because the file system is used as the namespace for addressing, UDS is 
            restricted to process on the same system.
    
    - The socket type is usually either SOCK_DGRAM for message-oriented datagram oriented 
    transport or SOCK_STREAM for stream-oriented transport.
    - Datagram sockets are most often associated with UDP, the user datagram protocol. They 
    provide unreliable delivery of individual messages. 
    - Stream-oriented sockets are associated with TCP, the tramission control protocol. They 
    provide byte streams between the client and the server, ensuring the message delivery or 
    failure notificatino through timeout management, retransmission and other features.
"""