from multiprocessing import Process, Lock 

def f(l, i):
    l.acquire()
    try:
        print("Hello wordl", i)
    finally:
        l.release()
        
if __name__ == "__main__":
    lock = Lock()
    
    for num in range(10):
        Process(target=f, args=(lock, num)).start()


# def f(i):
#     print("Hello wordl", i)
        
# if __name__ == "__main__":
#     lock = Lock()
    
#     for num in range(10):
#         Process(target=f, args=(num,)).start()