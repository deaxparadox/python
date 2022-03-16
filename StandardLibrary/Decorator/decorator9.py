'''Defining Decorators As Classes

You want to wrap functions with a decorator, but the result is going to be a 
callable instance. You need your decorator to work both inside and outside 
class definitions

To define a decorator as an instance, you need to make sure it implements 
the __call__() and __get__() methos.'''

'''METHOD1
import types 
from functools import wraps 

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0
        
    def __call__(self, *args, **kwargs):
        self.ncalls+=1
        return self.__wrapped__(*args, **kwargs)
    
    def __get__(self, instance, cls):
        if instance is None:
            return self 
        else:
            return types.MethodType(self, instance)


@Profiled
def add(x,y):
    return x+y

class Spam:
    @Profiled
    def bar(self,x):
        print(self,x)
'''

'''METHOD2
'''
import types 
from functools import wraps 

def profiled(func):
    ncalls=0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls+=1
        return func(*args, **kwargs)
    wrapper.ncalls=lambda: ncalls 
    return wrapper 

# Example 
@profiled
def add(x,y):
    return x+y
    
    
if __name__ == "__main__":
    add(3,4)
    print(add.ncalls())
