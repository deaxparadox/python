"""
1. The user datagram protocol (UDP works differenctly from TCP/IP. 
2. whereas TCP is a stream-oriented protocol, ensuring that all of the data is
transmitted in the right order, UDP is message-oriented protocol.

3. On the one hand, UDP does not require a long lived connection, so setting
up a UDP socket is a little simpler.
3. On the other hand, UDP messagemust fit with in a single datagram (for IPv4,
that means they  can hold only 56507 bytes because the 65535 bytes packet also
includes header information) and delivery is not guranteed as it is with TCP.)

"""

