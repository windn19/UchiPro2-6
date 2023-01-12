from functools import total_ordering


@total_ordering
class Date:
   def __init__(self, d, m, y):
       self.d = d
       self.m = m
       self.y = y

   def __eq__(self, other):
       return self.y, self.m, self.y == other.y, other.m, other.d

   def __lt__(self, other):
       return self.y, self.m, self.y < other.y, other.m, other.d


d1 = list(map(int, input().split('.')))
d2 = list(map(int, input().split('.')))
if d1 == d2:
   print('Одного возраста')
elif d1 > d2:
   print('Первый старше')
else:
   print('Второй старше')