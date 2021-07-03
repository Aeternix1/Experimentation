import socket 
from _thread import *
import threading

print_lock = threading.Lock()

# thread function
def threaded (c):
    while True:
        
        #receive data from client
        data = c.recv(1024)
        if not data: 
            print('Bye') 
            print_lock.release()
            break
    
        # reverse the given string from client
        data = data[::-1]

        # send back reversed string to client
        c.send(data)
    
    #close connection
    c.close() 

def Main():
    host = ""

    # reverse a port on your computer
    port = 15001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port))
    
    # put socket into listening mode
    s.listen(5) 
    print("socket is listening")

    # connection with the client
    while True:
        c, addr = s.accept() 

        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
        
        # start a new thread and return its identifier
        start_new_thread(threaded, (c,))

if __name__ == '__main__':
    Main()
