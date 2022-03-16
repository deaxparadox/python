import threading,logging,time

def delayed():
    logging.debug('worker running')
logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s)%(message)s'
)
t1=threading.Timer(0.3,delayed)
t1.setName('t1')
t2=threading.Timer(0.3,delayed)
t2.setName('t2')
logging.debug('starting timers')
