"""
thread basics: start 5 copies of a function running in parallel
uses time.sleep so that the main thread doesn't die too early
this kills all other threads on some platform

""" 

import _thread as thread
import time

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %d' % (myId, i))

for i in range(5):
    thread.start_new_thread(counter, (i, 5))

time.sleep(6)
print("Main thread exiting")
