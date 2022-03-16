from itertools import count

class create:
    a = count(1,4)

class Count:
    def __init__(self) -> None:
        pass

    @staticmethod
    def run():
        while True:
            b = create.a.__next__()
            if b>100:
                return False
            print(b)    
            
            
def main():
    Count.run()

if __name__ == "__main__":
    main()