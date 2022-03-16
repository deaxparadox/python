import threading
import os
import time

__thread_list = []


# run neuron while True
def br(condition: bool = True):
    return condition

    
def wait(br=None):
    count = 0
    while True:
        if count==5:
            # br(False)
            return False
        time.sleep(0.3)
        count+=1
    

def _one(wait = None):
    print("Started: ", threading.current_thread().name, os.getpid())
    wait()
    print("Terminated: ", threading.current_thread().name, os.getpid())
    
def _second(wait=None):
    print("Started: ", threading.current_thread().name, os.getpid())
    wait()
    print("Terminated: ", threading.current_thread().name, os.getpid())
    
def _third(wait=None):
    print("Started: ", threading.current_thread().name, os.getpid())
    wait()
    print("Terminated: ", threading.current_thread().name, os.getpid())
    

def _add(func=None):
    assert func is not None
    __thread_list.append(
        threading.Thread(
            target=func,
            args=(wait,),
            name=func.__name__
        )
    )

    
def start():
    for t in __thread_list:
        t.start()
        
        
def main():
    _add(_one)
    _add(_second)
    _add(_third)
    
    start()

if __name__ == "__main__":
    main()