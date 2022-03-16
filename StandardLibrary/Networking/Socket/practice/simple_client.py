import os, sys
print(sys.path.append('/home/creator/Documents/PythonDeveloper/Project'))
# print(sys.path)
from UniPackage.web.server import tcp

tcp.client()