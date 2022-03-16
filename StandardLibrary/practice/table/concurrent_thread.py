from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import time

def table(x):
    for i in range(1,11):
        print(x*i)
        time.sleep(1)
        
# with ThreadPoolExecutor(max_workers=10) as executor:
    # for i in range(1,11):
    #     executor.submit(table, i)

with ProcessPoolExecutor(max_workers=10) as executor:
    for i in range(1,11):
        executor.submit(table, i)