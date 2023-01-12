class Sequence:
   def __init__(self, el):
       self.el = el

   def __str__(self):
       return f'Последовательность {", ".join(self.el)}'

   def __add__(self, other):
       result = self.el
       for el in other.el:
           if el not in result:
               result.append(el)
       return Sequence(result)


el1 = input().split()
el2 = input().split()
print(Sequence(el1) + Sequence(el2))