import multiprocessing,time 

def worker():
    name=multiprocessing.current_process().name 
    print(name,'Starting')
    time.sleep(2)
    print(name,'Exiting')

def my_service():
    # get the current process name 
    name=multiprocessing.current_process().name 
    print(name,'Starting')
    time.sleep(3)
    print(name,'Exiting')

def main():
    service=multiprocessing.Process(
        name='my_service',
        target=my_service,
    )
    worker_1=multiprocessing.Process(
        name='my_service',
        target=my_service
    )
    worker_2=multiprocessing.Process(
        target=worker
    )
    worker_1.start()
    worker_2.start()
    service.start()

if __name__=="__main__":
    main()