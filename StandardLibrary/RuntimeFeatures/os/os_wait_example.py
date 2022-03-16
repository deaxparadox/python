import os 
import sys 
import time 

for i in range(2):
    print("PARENT {}: Forking".format(os.getpid(), i))
    worker_pid = os.fork()
    # print(worker_pid)
    if not worker_pid:
        print("WORKER {}: Starting".format(i))
        time.sleep(2+i)
        print("WORKER {}: Finishing".format(i))
        sys.exit(1)

for i in range(2):
    print("PARENT: Waiting for {}".format(i))
    done = os.wait()
    
    print("PARENT: Child done:", done)
    