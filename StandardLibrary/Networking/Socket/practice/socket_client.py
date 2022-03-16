import socket, sys 
import argparse
import struct
from module.convert import ByteToStr, StrToByte


def Arg():
    parser = argparse.ArgumentParser()
    parser.add_argument("message",
                        action="store", type=str,
                        default="This is the deaxparadox.")
    return parser.parse_args()



def client():
    argu = Arg()
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print("connecting to {} port {}".format(*server_address))
    sock.connect(server_address)

    try:
        # Send data.
        msg_str = argu.message
        message = StrToByte(msg_str)
        print('sending {!r}'.format(message))
        sock.sendall(message)
        
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print("received {!r}".format(data))
    finally:
        print('closing socket')
        sock.close()
        
        
if __name__=="__main__":
    client()