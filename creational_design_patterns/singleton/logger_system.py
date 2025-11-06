"""
Design logger system

Imagine you have a Logger that writes logs to a file. You only want one instance of it, and it should be created only when first used.

"""

import threading
import time 

class Logger:
    _instance= None
    _lock = threading.Lock()

    def __init__(self):
        time.sleep(1)
        print("Logger initialized")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            with cls._lock:
                print("lock obtained.....")
                if cls._instance is None:
                    cls._instance = cls()
            
        return cls._instance
    
    def log(self,msg):
        print(f"[LOG] {msg}")

    
# ---- Client Code ----
def worker(name):
    logger = Logger.get_instance()
    logger.log(f"Worker {name} is logging")
        

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


non_thread = Logger.get_instance()
non_thread.log("logging non thread object")