import tarfile
import os 

filename = "tarfile_add.tar"
# par_dir = ".."
# directory = os.path.abs("..")

print("creating archive")
with tarfile.open(filename, mode='w') as out:
	print("adding tarfile_is_tarfile.py")
	out.add("tarfile_is_tarfile.py")

print()
print("Contents")
with tarfile.open(filename, mode='r') as t:
	for member_info in t.getmembers():
		print(member_info.name)