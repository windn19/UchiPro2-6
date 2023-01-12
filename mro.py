class A:
    def __str__(self):
        return 'Экземпляр класса А'


class B:
    def __str__(self):
        return 'Экземпляр класса B'

    # def __repr__(self):
    #     return 'B()'


class C(A, B):
    pass


c = C()
lst = [c]
print(lst[0])
print(lst)
