'''Using decorators to patch class definitions

PROBLEM
You want to inspect or write portions of a class definitions to alter its
behavior, but without using inheritance or metaclasses.

SOLUTION
This might be a perfect use for a class decorator. For example, here is 
a class decorator that writes the __getattribute__ special method
to perform logging.'''


def log_getattribute(cls):
    # Get the original implementation
    orig_getattribute = cls.__getattribute__
    
    # Make a new definition
    def new_getattribute(self, name):
        print("getting:", name)
        return orig_getattribute(self, name)
    
    # Attach to the class and return 
    cls.__getattribute__ == new_getattribute
    return cls

# Example use 
@log_getattribute
class A:
    def __init__(self, x) -> None:
        self.x = x 
    def spam(self):
        pass 
    
if __name__ == "__main__":
    a = A(42)
    print(a.x)
    print(a.spam())

