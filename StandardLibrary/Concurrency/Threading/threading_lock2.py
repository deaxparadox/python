import threading
import time 

class Pop(object):
    plist = [x for x in range(10)]
    tlist = []
    cthread = None
    
    def __init__(self) -> None:
        self.lock = threading.Lock()
    
    def locked(self, name=None, i=0):
        if i == 0:
            print(name, "I am the first thread")
            if self.cthread is None:
                self.cthread = i
        
        while self.cthread is None:
            print(name, "number not assgined")
            time.sleep(1)
        
        while self.cthread != i:
            print(name, "waiting for my number")
            time.sleep(1)
        
        
        # self.tlist.append(name)             # registering threads 
        
        while self.lock.locked():
            time.sleep(1)
            # ...
        
        self.remove(name)
    
    def remove(self, name=None,i=0):
        self.lock.acquire();
        print(name, "lock acquired")
        try:
            item =self.plist.pop()
            print(f"Removed item {item}")
        finally:
            self.lock.release()
            print(name, "lock released")
            
            # increat thread number
            self.cthread+=1

class opt:
    p = Pop()
    
    @staticmethod
    def rsleep(x=1):
        time.sleep(x)

def worker(c,i):
    tname = threading.current_thread().name
    c.locked(name=tname, i=i)


def main():
    rev = [x for x in range(10)]
    for i in rev[::-1]:
        t = threading.Thread(
            name=f"[Thread  {i}]",
            target=worker,
            args=(opt.p,i,),
        )
        t.start()

if __name__ == "__main__":
    main()