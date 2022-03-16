import os
import pathlib 
import argparse

def __option():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='path')
    parser.add_argument('--path', dest='path')
    parser.add_argument('--pattern', dest="pattern")
    return parser.parse_args()

def __main_check(option=None):
    try:
        assert option.path is not None 
        assert option.pattern is not None 
        return option
    except:
        exit(1)

def main():
    option = __main_check(__option())
    
    

    count: int = 0
    p = pathlib.Path(option.path)
    for f in p.rglob(option.pattern):
        print(f)
        count+=1
        
    print(f"\n{count} files found")
        
if __name__ == "__main__":
    main()