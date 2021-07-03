from socket import *
import sys

#Server would be running on the same host as Client
serverName = 'localhost'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = input("Please type Subscribe\n")

clientSocket.sendto(message.encode(), (serverName, serverPort))

#wait for the reply from the server
receivedMessage, serverAddress = clientSocket.recvfrom(2048) 

if (receivedMessage.decode() == "Subscription Successful"): 
    # wait for 10 back to back messages from the server
    for i in range(10):
        receivedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(receivedMessage.decode())

#prepare to exit. Send Unsubscribe message to server
message='Unsubscribe'
clientSocket.sendto(message.encode(), (serverName, serverPort))
clientSocket.close()
