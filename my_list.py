class MyList(list):
    def get_avg(self):
        return sum(self) / len(self)


lst = MyList()
for i in range(1, 17):
    lst.append(i)
print(lst.get_avg())
