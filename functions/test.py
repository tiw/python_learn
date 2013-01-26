def sayHello():
    print 'hello'

def createFunction():
    return lambda x: x * x

def list_filter(l, f):
    return [i for i in l if f(i)]

def isOdd(n):
    return n % 2 == 1

if __name__ == '__main__':
    sayHello()
    sq = createFunction()
    print sq(5)

    l = range(10)
    print l
    print list_filter(l, isOdd)

