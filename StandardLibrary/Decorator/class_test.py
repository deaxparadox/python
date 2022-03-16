class class_test:
    __last__ = "Kushwaha"
    name = "Nitish"
    _future = '7328'
    __aim = 'KMI'
    
    def __init__(self) -> None:
        print("this is the initiate method ")
        _passion1 = 'programming'
        _passion2 = 'electricity'
        
        self.__current = None
        
    def fprint(self, x=None):
        return x 
    
    '''return private variable value'''
    def aim(self):
        return self.__aim
    
    @property
    def current(self):
        return self.__current
    @current.setter
    def current(self, value):
        self.__current = value
    @current.deleter
    def current(self):
        del self.__current

    
    '''cannot access class variable
    or instance variable '''
    @staticmethod
    def smethod(x):
        return x
    
    '''can only access class vairable'''
    @classmethod
    def cmethod(cls, x):
        print(cls.name)
        print(cls.__aim)
        print(cls._passion1)
    
    
def func1():
    return 'this is func1.'

def func2():
    return 'this is func2.'

def func3():
    return 'this is func3.' 

flist = [func1, func2, func3]
def fcall(func : str = None, flist: list = flist) -> str:
    # execpt func, flist
    for f in flist:
        if f.__name__ == func:
            return f()
            
def instance():
    return class_test()

            
if __name__ == "__main__":
    pt = class_test()
    print(pt.current)
    pt.current = "AI"
    print(pt.current)
    del pt.current
    try:
        print(pt.current)
    except: 
        pt.current = None
        print(pt.current)
    pt.current = "Electricity"
    print(pt.current)
    del pt.current 
    # print(pt.current)
    pt.current = None 