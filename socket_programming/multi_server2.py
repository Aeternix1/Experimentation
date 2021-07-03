from socket import *
import threading
import time
import datetime as dt

#Server will run on this port
serverPort = 12000
t_lock=threading.Condition() 
#Will store clients info in this list
clients=[]
#Communicate with clients after every second
UPDATE_INTERVAL = 1
timeout=False

# Function run after a connection is made
def recv_handler():
    global t_lock
    global clients
    global clientSocket
    global serverSocket
    print("Server is ready for service") 

    while(1): 
        message, clientAddress = serverSocket.recvfrom(2048)
        message = message.decode()
        with t_lock:
            currtime = dt.datetime.now()
            date_time = currtime.strftime("%d/%m/%Y, %H:%M:%S")
            print("Received request from", clientAddress[0], "listening at",
                clientAddress[1], ':', message, 'at time ', date_time) 
            if(message == "Subscribe"):
                clients.append(clientAddress)
                serverMessage="Subscription Successful"
            elif(message == "Unsubscribe"):
                if(clientAddress in clients):
                    clients.remove(clientAddress)
                    serverMessage="Subscription removed"
                else: 
                    serverMessage="You are not currently subscribed"
            else: 
                serverMessage = "Unknown command, send subscribe or unsubscribe\
                     only"
            serverSocket.sendto(serverMessage.encode(), clientAddress)
            t_lock.notify()

def send_handler():
    global t_lock
    global clients
    global clientSocket
    global serverSocket
    global timeout

    # go through the list of subscribed clients and send them the current time
    # after every one second
    while(1):
        with t_lock:
            for i in clients:
                currtime = dt.datetime.now() 
                date_time = currtime.strftime("%d/%m/%Y, %H:%M:%S")
                message = "Current time is " + date_time 
                clientSocket.sendto(message.encode(), i)
                print("Sending time to", i[0], "listening at", i[1], 'at time',
                        date_time)
            t_lock.notify()
        time.sleep(UPDATE_INTERVAL)

#Two sockets are being used, one for sending and one for receiving
clientSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('localhost', serverPort))

# Start recv as a thread
recv_thread=threading.Thread(name="RecvHandler", target=recv_handler) 
# Set recv to non-block (runs in the background)
recv_thread.daemon = True 
# Run the thread
recv_thread.start() 

send_thread=threading.Thread(name="SendHandler", target=send_handler)
send_thread.daemon=True
send_thread.start()

#this is the main thread
while True:
    time.sleep(0.1)

