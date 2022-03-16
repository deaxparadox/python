"""processes are spawned by creating a 'Process' object and then calling its 'start()'
method. """

from multiprocessing import Process
def f(name):
    print("hello", name)
    
if __name__=="__main__":
    p = Process(target=f, args=('bod',))
    p.start()
    p.join()