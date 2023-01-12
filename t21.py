from functools import total_ordering


@total_ordering
class Date:
    def __init__(self, d, m, y):
        self.day = d
        self.month = m
        self.year = y

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __lt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day < other.day
            else:
                return self.month < other.month
        else:
            return self.year < other.year


d1 = list(map(int, input().split('.')))
d2 = list(map(int, input().split('.')))
d1 = Date(*d1)
d2 = Date(*d2)
if d1 == d2:
   print('Одного возраста')
elif d1 < d2:
   print('Первый старше')
else:
   print('Второй старше')
