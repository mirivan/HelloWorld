import re

def split_camel(name):
    parts = re.findall(r'[A-Z]+(?=[A-Z][a-z]|$)|[A-Z][a-z]*|[a-z]+', name)
    return parts

def HelloWorld(action):
    caller_name = HelloWorld.__name__
    parts = split_camel(caller_name)
    func = getattr(__builtins__, action)
    if len(parts) > 1:
        func(' '.join(parts))
    else:
        func(caller_name)

HelloWorld('print')
