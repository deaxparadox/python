'''Writing Decorators that add argument to wrapped funcitons

You  want to wrtie a decrator taht adds an ext4ra argument to the calling
signature of the wrapped function. how ever, the addeda argument can't 
interfere with the existing callign conventions of the function.

Extra arguments can be injected into the calling signature using 
keyword-only arguments.. '''

"""
from functools import wraps 

def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper

    '''
    if the @optional_debug decorator was applied to a function that 
    already had a debug argument, then it would break
    '''
"""

"""Methodified"""
from functools import wraps 
import inspect

def optional_debug(func):
    if 'debug' in inspect.getargspec(func).args:
        raise TypeError("debug argument already defined")
    
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter(
        'debug',
        inspect.Parameter.KEYWORD_ONLY,
        default=False
    ))
    wrapper.__signature__=sig.replace(parameters=parms)
    return wrapper

if __name__=="__main__":
    # @optional_debug
    # def add(x,y):
    #     return x+y
    
    # import inspect
    # print(inspect.signature(add))

    @optional_debug
    def add(x,y):
        return x+y
    
    print(inspect.signature(add))