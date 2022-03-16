import multiprocessing
import time 

def table(x):
    for i in range(1,11):
        print(x*i)
        time.sleep(1)

def main():
    with multiprocessing.Pool(10) as p:
        p.map(table, range(1,11))
        
if __name__ == "__main__":
    main()