"""
- socket includes function to interface with domain name services on the network
so that a program can convert the hostname of a sersver into its numerical address.

- To find the official name of the current host, use gethostname()
"""

import socket
print(socket.gethostname())