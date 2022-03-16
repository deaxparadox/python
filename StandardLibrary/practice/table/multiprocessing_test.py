''''counting the table from 1 to 10 using the multiprocessing'''

import multiprocessing
import time 

class hold:
    _count = 10
    
def count():
    return hold()._count

class process(multiprocessing.Process):
    def __init__(self, x) -> None:
        super().__init__()
        self.x = x
        self.name = f"{process.__name__+str(x)}"
        
    def run(self):
        for i in range(1,count()+1):
            print(self.name, i*self.x)
            time.sleep(1)


def main():
    for i in range(1,count()+1):
        process(i).start()

if __name__ == "__main__":
    main()
    
    '''
    real	0m10.161s
    user	0m0.136s
    sys	0m0.053s

    '''