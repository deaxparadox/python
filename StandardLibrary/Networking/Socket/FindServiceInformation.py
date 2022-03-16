#In[]:
"""
- each socket address includes an integer port number.
- only one socket at a time can use a port at that address.

- The combination of IP address, protocol, and port number 
uniquely identifies a communication channel and ensures that messages sent through
a socket arrive at the correct destination.
"""
# %%
"""
- The post numbers for network services with standardized names can be looked 
up with getservbyname().
"""
def socket_getservbyname():
    import socket 
    from urllib.parse import urlparse

    URLS = [
        'http://www.python.org',
        'https://www.mybank.com',
        'ftp://prep.ai.mit.edu',
        'gopher://gopher.micro.umn.edu',
        'smtp://mail.example.com',
        'imap://mail.example.com',
        'imaps://mail.example.com',
        'pop3://pop.example.com',
        'pop3s://pop.example.com',
    ]

    for url in URLS:
        parsed_url = urlparse(url)
        port = socket.getservbyname(parsed_url.scheme)
        print("{:>6} : {}".format(parsed_url.scheme, port))

socket_getservbyname()

# %%
"""To reverse the service port lookup, use getservbyport()"""
def socket_getservbyport():
    """"""
    import socket 
    from urllib.parse import urlunparse
    for port in [80, 443, 21, 70, 25, 143, 993, 110, 995]:
        url = '{}://example.com/'.format(socket.getservbyport(port))
        print(url)
socket_getservbyport()
"""The reverse loopup is usefull for constructing URLs to services from
arbitrary address."""

# %%
"""To retrieve the number assigned to a transport protocol, use getprotobyname()"""

def socket_getprotobyname():
    import socket 
    
    def get_constants(prefix):
        """Create a dictionary mapping socket module constants to their
        names"""
        return {getattr(socket, n): n for n in dir(socket) if n.startswith(prefix)}
    
    protocols = get_constants("IPPROTO_")
    
    for name in ['icmp', 'udp', 'tcp']:
        proto_num = socket.getprotobyname(name)
        const_name = protocols[proto_num]
        print('{:>4} -> {:2d} (socket.{:<12} = {:2d})'.format(
            name, proto_num, const_name, getattr(socket, const_name)
        ))
socket_getprotobyname()

"""The values for protocol numbers are standardized, and defined as constants
in socket with the prefix IPROTO_"""

    
# %%

# %%
