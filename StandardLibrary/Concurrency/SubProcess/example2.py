import os 

print(os.getpid())
pid = os.fork()


if pid:
    print("Child process id:", pid)
else:
    print("I am the child")