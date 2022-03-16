import socketserver

class EchoRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # Echo the data back to the client
        data = self.request.recv(1024)
        self.request.send(data)
        return
    
def main():
    import socket, threading
    
    address = ('localhost', 0)      # Let the kernel assign a port
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address        # What port was assigned ?
    
    t = threading.Thread(target=server.serve_forever)
    t.setDaemon(True)       # Don't hang on exit
    t.start()
    
    # Connect to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    
    # Send the data.
    message = 'Hello, world'.encode()
    print("Sending : {!r}".format(message))
    len_sent = s.send(message)
    
    # Receive a response
    response = s.recv(1024)
    print("Received: {!r}".format(response))
    
    # Clean up.
    server.shutdown()
    s.close()
    server.socket.close()
    
    
if __name__ == "__main__":
    main()