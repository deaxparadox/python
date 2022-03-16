import threading

_threads=[]

def __init__() -> None:
    _threads=[]

def add(func=None, *args):
    t=threading.Thread(target=func, args=args)
    _threads.append(t)

def start():
    assert len(_threads)!=0
    for t in _threads:
        t.start()

def is_alive():
    assert len(_threads)!=0
    for t in _threads:
        if t.is_alive():
            print(t,"is running")
        else:
            print(t, "is terminated")
