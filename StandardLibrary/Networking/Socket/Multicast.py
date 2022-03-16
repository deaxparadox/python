'''
- Using multicast to deliver messages to more than one endpoint at a time
achieves bettwe efficency because the network infrastructure ensures that 
the packets are delivered to all recipients.
- Multicase messages are always sent using UDP, since TCP assumes a pair of 
communicating systems are parent.
- The addresses used for multicast, called multicast groups, are a subset of 
the regular IPv4 address range (224.0.0.0 through 230.255.255.255) that have 
been reserved for multicast traffic.
- These addresses are treated specially by network routers and switches, so 
messages sent to the group can be destributed over the Internet to all switches
that have joined the group.
'''