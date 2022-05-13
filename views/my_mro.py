class D(object):
    def __init__(self):
        super(D, self).__init__()
        print('D')

    def fun(self):
        print('D fun()')


class C(D):
    def __init__(self):
        super(C, self).__init__()
        print('C')

    def fun(self):
        print('C fun()')


class B(D):
    def __init__(self):
        super(B, self).__init__()
        print('B')


class A(B, C):
    def __init__(self):
        super(A, self).__init__()
        print('A')


if __name__ == '__main__':
    a = A()
    print(A.__mro__)
    a.fun()