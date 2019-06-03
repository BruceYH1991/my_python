print('hello world')
print('ok')


import pandas as pd

def a():
    print('a')
    return True

def b():
    print("b")
    return False

if a() or b():
    print('or')

if b() and a():
    print('and')
