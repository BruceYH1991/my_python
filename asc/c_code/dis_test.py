import dis



def f():
    a = 1
    b = 2
    c = a + b
    return c


def g():
    f()


dis.dis(g)
print('='*30)
dis.dis(f)
