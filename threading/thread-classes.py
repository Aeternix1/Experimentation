"""

thread class instances with state and run() for thread's action;
uses higher-level Java-like threading module object join method (not
mutexes or shared global vars) to know when threads are done in main parent
thread; see library manual for more details on threading;
"""

import threading

class Mythread
