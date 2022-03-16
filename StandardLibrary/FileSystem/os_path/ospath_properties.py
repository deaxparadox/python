import os.path as op 
import time 

print("File:{!r:>20}".format(__file__))
print("Access time:         {}".format(op.getatime(__file__)))
print("Modified time:    {}".format(op.getmtime(__file__)))
print("Change time:     {}".format(op.getctime(__file__)))
print("Size:                    {}".format(op.getsize(__file__)))