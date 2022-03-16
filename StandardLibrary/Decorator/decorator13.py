'''USING A METACLASS TO CONTROL INSTANCE CREATION

PROBLEM 
You want to change the way in which instances are created in order to implment
singleton, caching, or other similar features.

SOLUTION
As Python progrmammers know, if you define a class, you call it like afunction
to create instances'''

# class Spam:
#     def __init__(self, name) -> None:
#         self.name = name 
        
# a = Spam('Guido')
# b = Spam('Diana')

'''If you want to customize this step, you can do it by defining a metaclass 
and reimplementing its __call__() method in some way. To illustrate, suppose that 
you didn't want anyone creating instances at all:'''


# class NoInstances(type):
#     def __call__(self, *args, **kwargs):
#         raise TypeError("Can't instantiate directly")
    
# # Example 
# class Spam(metaclass=NoInstances):
#     @staticmethod 
#     def grok(x):
#         print("Spam.grok")
        
        
"""Now, suppose you want to implement the singleton pattern (i.e., a class where
only one instance is ever created). That is also relatively straightforward"""
# class Singleton(type):
#     def __init__(self, *args, **kwargs):
#         self.__instance = None
#         super().__init__(*args, **kwargs)
        
#     def __call__(self, *args, **kwargs):
#         if self.__instance is None:
#             self.__instance = super().__call__(*args, **kwargs)
#             return self.__instance
#         else:
#             return self.__instance
    
# Example
# using this class only one instance will get created
# class Spam(metaclass=Singleton):
#     def __init__(self):
#         print("Creating Spam")
        
        
'''Finally, suppose you want to create cached instances, '''
# import weakref

# class Cached(type):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.__cache = weakref.WeakValueDictionary()
        
#     def __call__(self, *args):
#         if args is self.__cache:
#             return self.__cache[args]
#         else:
#             obj = super().__call__(*args)
#             self.__cache[args] = obj 
#             return obj 
        
# # Example 
# class Spam(metaclass = Cached):
#     def __init__(self, name):
#         print("Creating Spam({!r})".format(name))
#         self.name = name


'''if you didn't use a metaclass, you might have to hide the classes behind some 
kind of extra factory function.'''
class _Spam:
    def __init__(self):
        print("Creating Spam")
_spam_instance = None 
def Spam():
    global _spam_instance 
    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance