import threading
import multiprocessing
import time 

class Test(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(threading.current_thread().name, "started")
        for i in range(15):
            if i == 10:
                break
            print(threading.current_thread().name, i)
            time.sleep(1)
        print(threading.current_thread().name, "ended")
        
for i in range(3):
    Test(name=f"function_{i}").start()
    # threading.Thread(
    #     target=run,
    #     name=f"function_{i}"
    # ).start()    
    time.sleep(2)