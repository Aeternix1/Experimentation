"""

passed in mutex object shared by all threads instead of globals;
use with context manager statement for auto acquire/release;
sleep calls added to avoid busy loops and simluate real work
"""

import _thread as thread
import time

stdoutmutex = thread.allocate_lock()        # create lock
numthreads = 5                              # 5 threads

# Create 5 exit mutexes
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]

def counter(myId, count, mutex):            # shared object passed in
    for i in range(count):
        time.sleep(1 / (myId+1))            # diff fractions of second
        with mutex:                         # auto acquire/realease: with
            print('[%s] => %s' % (myId, i))
        exitmutexes[myId].acquire()         # global: signal main thread

for i in range(numthreads):         
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes): time.sleep(0.25)
print('Main thread exiting.')
