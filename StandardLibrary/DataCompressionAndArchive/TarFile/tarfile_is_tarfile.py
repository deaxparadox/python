import tarfile


def check(file: str = None):
	assert file is not None
	return tarfile.is_tarfile(file)

for filename in ['README.txt', 'example', 'bad_example.tar', 'notthere.tar']:
	print(check(filename))
	try:
		print(check(filename))
		print("{!r:>15} : {!r}".format(filename, check(filename)))
	except IOError as err:
		print("{:>15}".format(filename, err))

