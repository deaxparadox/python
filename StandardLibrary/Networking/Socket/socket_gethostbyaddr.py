"""When the address of a server is available, use the gethostbyaddr()
to do a "reverse" lookup for the name."""

import socket 
hostname, aliases, addreses = socket.gethostbyaddr('10.9.0.10')
print("Hostname: ", hostname)
print("Aliases : ", aliases)
print("Addresses: ", addreses)

"""
- the return value is a type containing the full hostname, 
any aliases, and all IP addresses associated with the name.
"""
