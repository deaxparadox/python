'''Defining a Metaclas that takes optional arguments 

Problem 
You want to define a metaclass that allows class definitions to suppy optoinal arguments
possible to control or configure aspects of processing during type creation.

Solution
When defining classes, Python allows a metaclass to be specified using the metaclass keyword
argument in the class statement.'''

from abc import ABCMeta, abstractmethod
from multiprocessing import synchronize

class IStream(metaclas=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass 
    
    @abstractmethod
    def write(self, data):
        pass 
    
    
'''In custon metaclasses, additional keyword arguments can be supplied, like this'''
# class Spam(metaclass=MyMeta, debug=True, synchronize=True):
#     ...

'''To support such keyword arguments in a metaclas, make sure you define them on the __prepare__(), 
__new__(), and __init__() methods using keyword-only arguments, like this'''
class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        # Custom processing 
        ...
        return super().__prepare__(name, bases)
    
    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        ...
        return super().__new__(cls, name, bases, ns)
    
    # Required 
    def __init__(self, name, bases, ns, *, debug=False, syhnchronize=False):
        # Custom procesing 
        ...
        super().__init__(name, bases, ns)