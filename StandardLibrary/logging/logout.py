import os, sys 

# default hardcoded path for log folder 
def path():
    return f'/home/creator/Documents/PythonDeveloper/practice/logging'
def log_dir():
    return os.path.join(path(),'output')

def valid(p):
    return os.path.exists(p)

def isdir(f):
    return os.path.isdir(f)

def cd(p):
    if isdir(valid(p)): os.chdir(p)
    else: print("{} not a directory".format(p)) 

def create_log_dir():
    # if os.getcwd() == path():
    #     pass
    # else:
    #     cd(path())
    if valid(log_dir()):
            pass 
    else:
        
create_log_dir()