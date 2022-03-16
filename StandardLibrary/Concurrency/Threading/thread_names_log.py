import logging
from os import name 
from threading import Thread
import threading
import time 

def worker():
    logging.debug("Starting")
    time.sleep(0.2)
    logging.debug('Exiting')

def my_service():
    logging.debug("Starting")
    time.sleep(0.3)
    logging.debug('Exiting')

def log():
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(levelname)s] (%(threadName)-10s) %(message)s',
    )

def start():
    log()

    t = Thread(name="my_service", target=my_service)
    w = threading.Thread(name='worker', target=worker)
    w2 = threading.Thread(target=worker)    # Use default name 

    w.start()
    w2.start()
    t.start()


if __name__=="__main__":
    start()