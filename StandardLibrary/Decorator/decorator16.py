'''Enforcing an Arugment Signature on *args and **kwargs

Problem
You've written a function or method that uses *args and **kwargs,so that 
it can be general purpose, but you would also like to check the passes arguments
to see if they match a specific function calling signature.

Solution
For any problem whre you want to manipute functino calling 
signaures, you should use the signaure features found inthe 
inspect module. Two classes signature "Signature" and "Parameter".
are of particular interest here. Here is an interactive exampe of creating
function signaure.
'''


# from inspect import Signature, Parameter
# # Make a signature for a func(x, y=42, *, x=None)
# parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
#          Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
#          Parameter('z', Parameter.KEYWORD_ONLY, default=None)]
# sig = Signature(parms) 
# # print(sig)

# '''Once you have a signaure object, you can easily bind it to *args, and **kwargs using 
# the signature's "bind()" method'''
# def func(*args, **kwargs):
#     bound_values = sig.bind(*args, **kwargs)
#     for name,value in bound_values.arguments.items():
#         print(name,value)
        
'''More concrete example of enforcing function signature.
This this code, a base class has defined an extremely
general-purpose version of __init__(), but subclasses
are expected to suppy an expected signaure.'''
        
from inspect import Signature, Parameter
def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)

class Structure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs) -> None:
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name,value in bound_values.arguments.items():
            setattr(self,name,value)
# Example use 
class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')
class Point(Structure):
    __signature__ = make_sig('x', 'y')