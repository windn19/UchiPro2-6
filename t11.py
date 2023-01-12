class Sequence:
    def __init__(self, seq):
        self.seq = seq

    def __str__(self):
        return f'Последовательность {", ".join(self.seq)}'

    def __add__(self, other):
        result = self.seq[:]
        for it in other.seq:
            if it not in self.seq:
                result.append(it)
        return Sequence(result)


seq1 = input().split()
seq2 = input().split()
print(Sequence(seq1) + Sequence(seq2))