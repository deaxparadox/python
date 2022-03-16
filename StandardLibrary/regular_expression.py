import re 

def re_search():
    pattern='this'
    text='Does this text match the pattern'
    match=re.search(pattern,next)
    s=match.start()
    e=match.end()
    print('Found "{}"\nin "{}"\n from {} to {} ("{}")'.format(match.re.pattern,match.string,s,e,text[s:e]))

def re_compile():
    regexes=[
        re.compile(p)
        for p in ['this','that']
    ]
    text='Does this text match the pattern?'
    print("Text: {!r}\n".format(text))
    for regex in regexes:
        print('Seeking "{}" ->'.format(regex.pattern), end=' ')
        if regex.search(text):
            print('match!')
        else:
            print("no match!")

def re_finditer():
    text='abbaabbbbaaaaa'
    pattern='ab'
    for match in re.finditer(pattern,text):
        s=match.start()
        e=match.end()
        print("Found {!r} at {:d}:{:d}".format(text[s:e],s,e))

def re_test_patterns(text=None,patterns=None):
    if text is None and patterns is None:
        text='abbaaabbbbaaaaa'
        patterns=[('ab',"'b' followed by 'b'"),]
    """Given source text and a list of patterns, look for matches for each pattern within the text and print them to stdout."""
    # Look for each pattern in the text and print the results.
    for pattern,desc in patterns:
        print("'{}' ({})\n".format(pattern,desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern,text):
            s=match.start()
            e=match.end()
            substr=text[s:e]
            n_backslashes=text[:s].count('\\')
            prefix='.'*(s+n_backslashes)
            print("   {}' {}'".format(prefix,substr))
        print()
    return 


def re_repetition():
    text='abbaabbba'
    patterns=[
        ('ab*', 'a followed by zero or more b'),
        ('ab+', 'a followed by one or more b'),
        ('ab?', 'a followed by zero or one b'),
        ('ab{3}', 'a followed by three b'),
        ('ab{2,3}', 'a followed by two to three b')
    ]
    re_test_patterns(text,patterns)

def re_repetitions_non_greedy():
    text='abbaabbba'
    patterns=[
        ('ab*?', 'a followed by zero or more b'),
        ('ab+?', 'a followed by one or more b'),
        ('ab??', 'a followed by zero or one b'),
        ('ab{3}?', 'a followed by three b'),
        ('ab{2,3}?', 'a followed by two to three b')
    ]
    re_test_patterns(text,patterns)

def re_charset():
    text='abbaabbba'
    patterns=[
        ('[ab]', 'either a or b'),
        ('a[ab]+', 'a followed by 1 or more a or b'),
        ('a[ab]+?', 'a followed by 1 or more a or b, not greedy')
    ]
    re_test_patterns(text,patterns)

def re_charset_exclude():
    text='This is some text -- with punctuation.'
    patterns=[
        ('[^-. ]+', 'sequences without -, ., or space')
    ]
    re_test_patterns(text,patterns)

def re_charset_ranges():
    text='This is some text -- with punctuation.'
    patterns=[
        ('[a-z]+', 'sequences of lowercase letters'),
        ('[A-Z]+', 'sequences of uppercase letters'),
        ('[a-zA-Z]+', 'sequences of lower- or uppercase letters'),
        ('[A-Z][a-z]+', 'one uppercase followed by lowercase')
    ]
    re_test_patterns(text,patterns)

def re_charset_dot():
    text='abbaabbba'
    patterns=[
        ('a.', 'a followed by any one character'),
        ('b.', 'a followed by any one character'),
        ('a.*b', 'a followed by anything, ending in b'),
        ('a.*?b', 'a followed by anything, ending in b')
    ]
    re_test_patterns(text,patterns)