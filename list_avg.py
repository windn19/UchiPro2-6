class MyList(list):
    def __init__(self, name):
        super().__init__(self)
        self.name = name

    def __str__(self):
        result = super().__str__()
        return f'{self.name}: {result}'


lst = MyList('Список нечетных чисел')
for i in range(1, 11, 2):
    lst.append(i)
print(lst)
