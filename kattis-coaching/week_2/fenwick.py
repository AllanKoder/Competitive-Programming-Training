from collections import defaultdict

L = 10**9
class Fenwick():
    def __init__(self):
        self.arr = defaultdict(int)

    def insert(self, i, val):
        while i < L:
            self.arr[i] += val
            i += (i & -i)

    def sum(self, i):
        total = 0
        while i >= 1:
            total += self.arr[i]
            i -= (i & -i)

        return total
    
    def range(self, l, r):
        return self.sum(r) - self.sum(l-1)




testing  = Fenwick()

testing.insert(1, 2)
testing.insert(2, 3)
testing.insert(3, 5)
testing.insert(L-1, 5)

print(testing.range(1, 5))
print(testing.range(1, 2))
print(testing.range(1, 1))
print(testing.range(4, 5))
print(testing.range(3, 5))
print(testing.range(1, L-1))
