"""You've written a decorator, but when you
apply it to a function, important metadata
such as the name, doc string, annotations, and 
calling signature are lost."""

import time 
from functools import wraps 

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        
        return result 
    return wrapper