"""
uses mutexes to know when threads are done in parent/main thread
instead of time.sleep; lock stdout to avoid comingled prints;
""" 

import _thread as thread
stdoutmutex = thread.allocate_lock()  #thread.allocate_lock() creates lock obj
# Signalling mutex
exitmutexes = [thread.allocate_lock() for i in range(10)] 

def counter(myId, count):
    for i in range(count):
        stdoutmutex.acquire()
        print('[%s] => %s' % (myId, i))
        stdoutmutex.release()
    exitmutexes[myId].acquire()    # Lock

for i in range(10):
    thread.start_new_thread(counter, (i, 100))

for mutex in exitmutexes:                   # Waits until all 
    while not mutex.locked(): pass
print('Main thread exiting.')
