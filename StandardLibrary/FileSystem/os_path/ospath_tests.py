import os.path as op 

FILENAMES = [
    __file__,
    op.dirname(__file__),
    '/',
    './broken_link',
]
for file in FILENAMES:
    print("File                  : {!r}".format(file))
    print("Absolute             :", op.abspath(file))
    print("Is File?                 :", op.isfile(file))
    print("Is Dir?                  :", op.isdir(file))
    print("Is Link?                 :", op.islink(file))
    print("Mountpoint?          :", op.ismount(file))
    print("Exists?                      :", op.exists(file))
    print("Link Exists              :", op.lexists(file))
    print()    
    
    
    
    