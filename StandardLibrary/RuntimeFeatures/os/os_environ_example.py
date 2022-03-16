import os 
print("Initial value:", os.environ.get("TESTVAR", None))
print('Child process:')
os.system('echo $TESTVAR')

os.environ['TESTVAR']='THIS VALUE WAS CHANGED'

print()
print("Changed value:", os.environ['TESTVAR'])
print("Child process:")
os.system('echo $TESTVAR')

del os.environ['TESTVAR']

print()
print("Removed Value:", os.environ.get("TESTVAR", None))
print("Child proces:")
os.system("echo $TESTVAR")