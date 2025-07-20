from typing import List
from operator import xor
from functools import reduce

def xor_min(numbers: List[int]) ->  int:
    if all(n == 0 for n in numbers): return 0
    result = reduce(xor, numbers)
    return bool(result) + 1

print(xor_min([1,1,1,1]))