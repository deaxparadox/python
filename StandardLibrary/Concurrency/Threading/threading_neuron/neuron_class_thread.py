from threading import Thread
from multiprocessing import Process
from typing import Callable, Union, Any, Mapping
import os, time
import neuron_class_thread
from neurons import main
import random
import numpy


def table(i, sleep=None):
    assert sleep is not None
    print(Thread().name, "started")
    for j in range(10):
        print(Thread().name,sleep,i*j)
        time.sleep(sleep)
    print(Thread().name, "terminated")

def eq_dist():
    return [float("{:.2f}".format(x)) for x in numpy.linspace(0,1,10)]
    
ed = eq_dist()
def sleep():
    return random.choice(ed)
    
def main():
    ts = []
    for  i in range(2,5):
        ts.append(
            Thread(
                target=table,
                args=(i,sleep()),
                name=table.__name__,
            )
        )
    for p in ts:
        p.start()
        
    for p in ts:
        if p.is_alive():
            pass 
        else:
            p.join()
        
if __name__ == "__main__":
    main()