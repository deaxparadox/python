import os 
import signal 
import time 
import sys 

pid = os.getpid()
received = False

def signal_usrl(signum, frame):
    "Callback invoked when a signal is received"
    global received
    received = True
    print("CHILD {:>6}: Recevied USR1".format(pid))
    sys.stdout.flush()
    
print("CHILD {:>6}: Setting up signal handler".format(pid))
sys.stdout.flush()
signal.signal(signal.SIGUSR1, signal_usrl)
print("CHILD {:>6}: Pausing to wait for signal".format(pid))
sys.stdout.flush()
time.sleep(1)

if not received:
    print("CHILD {:>6}: Never recevied signal".format(pid))