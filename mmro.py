class A:
    pass


class B:
    pass


class C(B, A):
    pass


c = C()
print(C.__mro__)
