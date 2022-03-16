'''Applying Decoratos to class and static Methods

You want to apply a decorator to a class or static method

Applying decorators to class and static methods is straightforward , 
but make sure that your decorators are applied before @classmethod
and @staticmethod
'''

import time 
from functools import wraps

# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return r
    return wrapper

# Class illustrating application of the decorator to different kinds od methods 
class Spam:
    @timethis 
    def instance_method(self,n):
        print(self, n)
        while n>0:
            n-=1
            
    @classmethod
    @timethis 
    def class_method(cls, n):
        print(cls, n)
        while n>0:
            n-=1
            
    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n>0:
            n-=1
            
            
from abc import ABCMeta, abstractmethod
class A(metaclas=ABCMeta):
    @classmethod
    @abstractmethod
    
    def method(cls):
        pass
"""in ths code, the order if @classmethod and @abstractmethod matters.
If you flip the two decorators around, everything breaks."""