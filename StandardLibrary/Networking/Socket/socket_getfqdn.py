"""
- Use getfqdn() to conver ta parital name to a fully qualified domain
name.
"""

import socket 
for host in ['apu', 'pymotw.com']:
    print("{:>10} : {}".format(host, socket.getfqdn(host)))
    
"""The name returned will not necessarily will not match the input argument
in any way if the input is an alias, as www"""