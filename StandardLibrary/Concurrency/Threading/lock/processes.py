from threading import Thread
import multiprocessing
import os 
import time 

class loop:
    l_break = None
    def __init__(self):
        self.test=None
    
    @staticmethod
    def just():
        print("i am just a staic")
    
    @classmethod
    def sleep(cls, s: int = 0) -> None:
        # print(cls.l_break)
        s = 0
        time.sleep(s)

def neuron_p(func):
    import threading, time 
    def wraper(*args, **kwargs):
        print(f"{time.asctime()} : {func.__name__}")
        multiprocessing.Process(target=func, args=args, kwargs=kwargs).start()
    return wraper

def neuron_t(func):
    import threading, time 
    def wraper(*args, **kwargs):
        print(f"{time.asctime()} : {func.__name__}")
        threading.Thread(target=func, args=args, kwargs=kwargs).start()
    return wraper

@neuron_t
def breaker(*args, **kwargs):
    for i in range(10):
        loop.sleep(0.3)
    print(f"{os.getpid()} : breaker applied")
    loop.l_break=True
    
@neuron_p
def table1(*args, **kwargs):
    try: 
        # table1 start as process 
        # breaker is executed as thread of it process
        breaker()
    except:
        print("breaker not loaded")
    for i in range(1,15):
        if loop.l_break:
            break
        print(os.getpid(),":", i)
        loop.sleep(1)

@neuron_p
def table2(*args, **kwargs):
    try: 
        # table2 start as process 
        # breaker is executed as thread of it process
        breaker()
    except:
        print("function not loaded")
    n=2
    count=0
    while count!=15:
        if loop.l_break:
            break
        print(os.getpid(),":", 2*count)
        count+=1
        loop.sleep(1)

    
      
table1()
table2(2,3,4,name="nitish", last="kushwaha")