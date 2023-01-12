class A:
    def __init__(self):
        print('class A')


class B(A):
    def __init__(self):
        print('class B')


class C(A):
    def __init__(self):
        print('class C')


class D:
    def __init__(self):
        print('class D')


class E(C):
    def __init__(self):
        print('class E')


e = E()
print(E.__mro__)
super(E, e).__init__()