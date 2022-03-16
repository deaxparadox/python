#In[]:
"""
- getaddrinfo() converts the basic address of a service into a list of typles
with all of the information necessary to make a connection.
- Each tuple may contain different network families or protocols.
"""

def socket_getaddrinfo():
    import socket 
    
    def get_constants(prefix):
        """Create a dictionary mappign socket module
        constants to their names.
        """
        return {getattr(socket, n): n 
                for n in dir(socket)
                if n.startswith(prefix)
        }
        
    families = get_constants('AF_')
    types = get_constants("SOCK_")
    protocols = get_constants("IPPROTO_")
    
    for response in socket.getaddrinfo("www.python.org", 'http'):
        # Unpack the response tuple.
        family, socktype, proto, canonname, sockaddr = response
        
        print("Family       :", families[family])
        print("Type         :", type[socktype])
        print("Protocol     :", protocols[proto])
        print("Canonical name:", canonname)
        print("Socket adderss:", sockaddr)
        print()
             
socket_getaddrinfo()


# %%
def socket_getaddrinfo_extra_args():
    import socket 
    
    def get_constants(prefix):
        """Create a dictionary mappign socket module
        constants to their names.
        """
        return {getattr(socket, n): n 
                for n in dir(socket)
                if n.startswith(prefix)
        }
        
    families = get_constants('AF_')
    types = get_constants("SOCK_")
    protocols = get_constants("IPPROTO_")
    
    responses = socket.getaddrinfo(
        host='www.python.org',
        port='http',
        family=socket.AF_INET,
        type=socket.SOCK_STREAM,
        proto=socket.IPPROTO_TCP,
        flags=socket.AI_CANONNAME,
    )
    
    for response in responses:
        # Unpack the response tuple.
        family, socktype, proto, canonname, sockaddr = response
        
        print("Family       :", families[family])
        print("Type         :", type[socktype])
        print("Protocol     :", protocols[proto])
        print("Canonical name:", canonname)
        print("Socket adderss:", sockaddr)
        print()
             
socket_getaddrinfo_extra_args()

