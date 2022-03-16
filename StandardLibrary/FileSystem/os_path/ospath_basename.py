import os.path as op

PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '',
]
for path in PATHS:
    print("{!r:>17} : {}".format(path, op.basename(path)))