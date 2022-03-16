from threading import Thread
import multiprocessing
import os 
import time 

class loop:
    l_break = None

# decorator threads
def neuron(func):
    import threading, time 
    def wraper(*args, **kwargs):
        print(f"{time.asctime()} : {func.__name__}")
        threading.Thread(target=func, args=args, kwargs=kwargs).start()
    return wraper

@neuron
def breaker(*args, **kwargs):
    for i in range(10):
        time.sleep(0.7)
    print("Countdown over applying break")
    loop.l_break=True
    
@neuron
def table1(*args):
    for i in range(1,15):
        if loop.l_break:
            break
        print(os.getpid(), i)
        time.sleep(1)
        

@neuron
def table2(*args, **kwargs):
    n=2
    count=0
    while count!=15:
        if loop.l_break:
            break
        print(os.getpid(), 2*count)
        count+=1
        time.sleep(1)

    
      
table1()
table2(2,3,4,name="nitish", last="kushwaha")
breaker()