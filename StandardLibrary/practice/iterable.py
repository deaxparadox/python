def cycle(iterable):
    saved = []
    for element in iterable:
        yield element 
        saved.append(element)
    while saved:
        for element in saved:
            yield element
            
            
def dropwhile(predicate, iterable):
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x 
            break 
    for x in iterable:
        yield