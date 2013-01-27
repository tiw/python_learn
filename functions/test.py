def sayHello():
    print 'hello'


def createFunction():
    return lambda x: x * x


def list_filter(l, f):
    return (i for i in l if f(i))


def isOdd(n):
    return n % 2 == 1


def sum(i):
    s = 0
    for a in i:
        s = s + a
    return s

if __name__ == '__main__':
    sayHello()
    sq = createFunction()
    print sq(5)

    l = range(10)
    print l
    print list_filter(l, isOdd)
    print sum(list_filter(l, isOdd))

