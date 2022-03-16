import os.path as op

PATHS = [
    ('one', 'two', 'three'),
    ('/', 'one', 'two', 'three'),
    ('/one', '/two', '/three'),
]

for parts in PATHS:
    print("{!r:<30} : {!r}".format(parts, op.join(*parts)))