import os.path as op

PATHS = [
    'filename.txt',
    'filename',
    '/path/to/filename.txt',
    'my-archive.tar.gx',
    'no-extension',
    '/',
    '',
]
for path in PATHS:
    print("{!r:>17} : {}".format(path, op.splitext(path)))