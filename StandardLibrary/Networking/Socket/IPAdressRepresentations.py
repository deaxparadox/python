#In[]:
"""
- Network programs written in C use the data type struct sockaddr to represent
IP addresses as bianry values (instead of the string addesses usually found in 
Python programs). 
- To convert IPv4 addresses between the Python representation and the C representation, use inet_aton() and inet-ntoa().

"""

def socket_address_packing():
    import binascii, socket, struct
    import sys 
    
    for string_address in ['192.168.1.1', '127.0.0.1']:
        packed = socket.inet_aton(string_address)
        print("Original :", string_address)
        print("Packed   :", binascii.hexlify(packed))
        print("Unpacked :", socket.inet_ntoa(packed))
        print()
        
socket_address_packing()

"""The 4 bytes in the packed format can be passed to C libraries, transmitted
safely over the network, or saed to a database compactly"""
    
# %%
"""The related functions inet_pton() and inet_ntop() work with both IPv4 and IPv6
addresses, producing the appropriate format based on the address family parameter
passed in."""

def socket_ipv6_address_packing():
    import binascii, socket, struct, sys 
    string_address = '2002:ac10:10a:1234:21e:52ff:fe74:40e'
    packed = socket.inet_pton(socket.AF_INET6, string_address)
    print("Original :", string_address)
    print("Packed   :", binascii.hexlify(packed))
    print("Unpacked :", socket.inet_ntop(socket.AF_INET6, packed))

socket_ipv6_address_packing()
# %%

# %%

# %%
