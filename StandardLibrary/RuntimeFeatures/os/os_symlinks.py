import os 

link_name = os.path.join('/tmp/', os.path.basename(__file__))


print("Creating link {} -> {}".format(link_name, __file__))
os.symlink(__file__, link_name)

stat_info = os.lstat(link_name)
print("Permissions:", oct(stat_info.st_mode))

print("Points to:", os.readlink(link_name))

# Clearn up 
os.unlink(link_name)