import _thread as thread
import time

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        mutex.acquire()   # request thread access
        print('[%s] => %s' %(myId, i))
        mutex.release()   # release thread

mutex = thread.allocate_lock() # global lock object
for i in range(5):
    thread.start_new_thread(counter, (i, 5))    # each thread loops 5 times

time.sleep(6)
print("Main thread exiting")
