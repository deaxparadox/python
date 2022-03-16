import tarfile

"""Using exiting tar file created in by tarfile_add.py
named "tarfile_add.tar", append tarfile_append.py file to it
"""


filename = 'tarfile_add.tar'
append_file = 'tarfile_append.py'

# Adding file 
with tarfile.open(filename, mode='a') as out:
	out.add(append_file)



print()
print("Contents")
with tarfile.open(filename, mode='r') as t:
	for member_info in t.getmembers():
		print("\t{:<}".format(member_info.name))