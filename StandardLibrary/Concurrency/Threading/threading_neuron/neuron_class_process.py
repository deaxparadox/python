from threading import Thread
from multiprocessing import Process
from typing import Callable, Union, Any, Mapping
import os, time
import neuron_class_thread
import random
import numpy
import asyncio

# class neuron(Process):
#     def __init__(self,
#                  func = None
#                  ) -> None:
#         super().__init__()
#         self.func = func
        
#     def run(self):
#         print("[P] Started: ", os.getpid(), os.getppid())
#         main()
#         print("[P] Terminated: ", os.getpid(), os.getppid())

    
# def process():
#     for i in range(1):
#         neuron().start()
        
# def main():
#     process()

def table(i, sleep=None):
    assert sleep is not None
    print(Process().name, "started")
    neuron_class_thread.main()
    # for j in range(10):
    #     # print(Process().name,sleep,i*j)
    #     time.sleep(sleep)
    print(Process().name, "terminated")

def eq_dist():
    return [float("{:.2f}".format(x)) for x in numpy.linspace(0,1,10)]
    
ed = eq_dist()
def sleep():
    return random.choice(ed)
    

def main():
    ps = []
    for  i in range(2,3):
        ps.append(
            Process(
                target=table,
                args=(i,sleep()),
                name=table.__name__
            )
        )
    for p in ps:
        p.start()
        
    for p in ps:
        if p.is_alive():
            pass 
        else:
            p.join()
        
if __name__ == "__main__":
    # main()
    # neuron().start()
    main()