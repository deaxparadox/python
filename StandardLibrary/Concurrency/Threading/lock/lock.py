from threading import Lock
 
class required:
    list = []
    
    def __init__(self) -> None:
        super().__init__()
        
        

def message(func):
    def wrapper(*args, **kwargs):
        print(f"starting: {func.__name__}")    
        result = func(*args, **kwargs)
        print(f"ending: {func.__name__}")
        return result
    return wrapper



def time(func):
    import time, datetime
    def wrapper(*args, **kwargs):
        print(f"{time.asctime()} : {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@time
def test():
    print("my name if nitish")
    
test()