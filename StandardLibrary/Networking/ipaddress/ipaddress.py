import binascii


def ipaddress_addreses():
    import binascii, ipaddress

    ADDRESSES=[
        '10.9.0.6'
        # or ipv6 addresses
    ]
    for ip in ADDRESSES:
        addr=ipaddress.ip_address(ip)
        print("{!r}".format(addr))
        print('  IP version:{}'.format(addr.version))
        print('  is private:{}'.format(addr.is_private))
        print(' packed from:{}'.format(binascii.hexlify(addr.packed)))
        print('     integer:{}'.format(int(addr)))
        print()


def ipaddress_networks():
    import ipaddress
    NETWORKS=[
        '10.9.0.0/24'
        # or ipv6 network address
    ]
    for n in NETWORKS:
        net=ipaddress.ip_network(n)
        print('{!r}'.format(net))
        print('        is private:{}'.format(net.is_private))
        print('         broadcast:{}'.format(net.broadcast_address))
        print('        compressed:{}'.format(net.compressed))
        print('      with netmask:{}'.format(net.with_netmask))
        print('     with hostmask:{}'.format(net.with_hostmask))
        print('     num addresses:{}'.format(net.num_addresses))


def ipaddress_network_iterate():
    import ipaddress
    NETWORKS=[
        '10.9.0.0/24'
        # ipv6 addres
    ]
    for n in NETWORKS:
        net=ipaddress.ip_network(n)
        print('{!r}'.format(net))
        print(zip(range(3),net))
        for i,ip in zip(range(3),net):
            print(ip)
        print()

def ipaddress_network_iterate_hosts():
    import ipaddress
    NETWORKS=[
        '10.9.0.0/24'
        # ipv6 addres
    ]
    for n in NETWORKS:
        net=ipaddress.ip_network(n)
        print('{!r}'.format(net))
        for i,ip in zip(range(3),net.hosts()):
            print(ip)
        print()


def ipaddress_network_membership():
    import ipaddress 
    NETWORKS=[
        ipaddress.ip_network('10.9.0.0/24')
        # ipv6 address
    ]
    ADDRESSES=[
        ipaddress.ip_address('10.9.0.6'),
        ipaddress.ip_address('10.7.0.31')
    ]
    for ip in ADDRESSES:
        for net in NETWORKS:
            if ip in net:
                print('{}\nis on {}'.format(ip,net))
        else:
            print("{}\nis not an known network".format(ip))
        print()

def ipaddress_interfaces():
    import ipaddress
    ADDRESS=[
        '10.9.0.6/24'
        # ipv6 addres
    ]
    for ip in ADDRESS:
        iface=ipaddress.ip_interface(ip)
        print('{!r}'.format(iface))
        print('netwok:\n    {}'.format(iface.network))
        print('ip:\n    {}'.format(iface.ip))
        print('IP with prefixlen:\n    {}'.format(iface.with_prefixlen))
        print('netmask:\n    {}'.format(iface.with_netmask))
        print('hostmask:\n    {}'.format(iface.with_hostmask))



if __name__ == "__main__":
    pass