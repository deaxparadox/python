import collections

def method1():
    c = collections.Counter('abcdaab')
    
    for letter in 'abcde':
        print("{} : {}".format(letter, c[letter]))    

def method2():
    c = collections.Counter('extermely')
    c['z'] = 0
    print(c)
    print(list(c.elements()))
    
def method3():
    c = collections.Counter()
    with open('/usr/share/dict/words','rt') as f:
        for line in f:
            c.update(line.strip().lower())
    print("Most common: ")
    for letter,count in c.most_common(3):
        print("{}: {:>7}".format(letter,count))

method3()
