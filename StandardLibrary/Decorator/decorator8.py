'''Defnining Decorators As Part of a Class

You want to define a decorator inside a class definition and apply it to 
other functions or methods.'''

from functools import wraps 

class A:
    # Decorator as an instance method 
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 1")
            return func(*args, **kwargs)
        return wrapper 
    
    # Decorator as a class method 
    @classmethod 
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator2 ")
            return func(*args **kwargs)
        return wrapper