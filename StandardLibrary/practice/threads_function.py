import time 
import threading


def message(string: str = None):
    print(string)

class affect(object):
    state_global = None
    break_all = False

    # max cycles 20 sec
    # after 20 sec breaker is applied
    def count10():
        message("break counter started")
        for _ in range(10):
            time.sleep(1
                    )
        message("break counter ended")
        affect.break_all = True

    def reading():
        message('reading started')
        while True:
            if affect.break_all:
                break
            if affect.state_global:
                print('global state: ', affect.state_global)
            else:
                print('global state: ', affect.state_global)
            time.sleep(1)
        message("reading ended")
    
    def alter_bool():
        message("alter_bool started")
        c = 0
        while True:
            if affect.break_all:
                break
            if (c % 3) == 0 and (c%2) == 0:
                affect.state_global = True
                print(c, affect.state_global)
            if (c % 3) == 0 and (c%2) != 0:
                affect.state_global = False
                print(c, affect.state_global)
            c+=1
            time.sleep(1)
        message('alter_bool ended')    


class extra(object):
    def __init__(self) -> None:
        pass
    
    def count(self, x, i):
        return x*i

    

class always(extra):
    _x = 3
    def __init__(self) -> None:
        pass
    
    @staticmethod    
    def table1():
        while True:
            if affect.break_all:
                break
            time.sleep(1)
            
    @staticmethod        
    def table2():
        while True:
            if affect.break_all:
                break
            time.sleep(1)
            
    def table3(self):
        c = 0
        while True:
            if affect.break_all:
                break
            self.count(self._x, c)   
            c+=1
            time.sleep(1)
            

        
