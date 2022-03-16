import threading
import time 
from threads_function import *

class  neuron(threading.Thread):
    def __init__(self, func=None):
        super().__init__()
        assert func is not None
        self.func = func
        
    def run(self):
        self.func()


t_func = [
    affect.count10, affect.alter_bool, affect.reading
]
ts = []
for f in t_func:
    ts.append(neuron(f))
    
for t in ts:
    t.start()
    
# time.sleep(10)

# for t in ts:
#     t.terminate()
    
    
# for t in ts:
#     print(t.is_alive())