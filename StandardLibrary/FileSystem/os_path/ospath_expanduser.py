import os.path as op

for user in ['', 'dhellmann', 'nosuchuser']:
    lookup = '~' + user
    
    print("{!r:>15} : {!r}".format(
        lookup, op.expanduser(lookup)
    ))

