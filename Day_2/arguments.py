def defaultArg(a=10, b=20):
    c = a + b
    print(c)


def varArg(*args):
    for a in args:
        print(a)


defaultArg()
varArg(10, 20, 30, 40, 50, 60)
