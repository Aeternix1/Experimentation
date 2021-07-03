"""
Client: send data to the server and print the server's reply 
""" 

import sys 
from socket import * 
serverHost = 'localhost'
serverPort = 50007

message = [b'Hello network world Hello network world Hello Network World'] 

if len(sys.argv) > 1:                                   # If we want to 
    serverHost = sys.argv[1]                            # specify a server
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:]) 

sockobj = socket(AF_INET, SOCK_STREAM)       # make a TCP socket object
sockobj.connect((serverHost, serverPort))    # connect to a server Host + Port

for i in range(1, 10):
    for line in message:                         
        sockobj.send(line)                       # send line to server over socket
        data = sockobj.recv(1024)                # receive line from server
        print('Client received:', data)           
        

sockobj.close()                              # closed socket send EOF to server

