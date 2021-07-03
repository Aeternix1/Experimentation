"""
Server side: open a TCP/IP socket on a port, listen for a message from the
client, and send an echo reply

""" 

from socket import *
myHost = ''
myPort = 50007

sockobj = socket(AF_INET, SOCK_STREAM)    # Create a socket object
sockobj.bind((myHost, myPort))            # Bind to a server port
sockobj.listen(5)                         # Listen, allow 5 pending connects  

while True:                               # Listen unless process is killed
    connection, address = sockobj.accept()  # Client connects to the socket 
    print('Server connected by', address)   # Address of the connected Device 
    while True:
        data = connection.recv(1024)        # Read next line on client socket
        if not data: break                  # Send a reply line to the client,
        connection.send(b'Echo=>' + data)   # until the EOF
    connection.close() 
    
