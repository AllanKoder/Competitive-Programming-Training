from collections import deque

s = input()
p = input()

class RabinKarp():
    def __init__(self, window_size: int, base: int = 53, mod: int = 10**9+7) -> None:
        # Initialize the powers
        self.chars = deque()
        self.window_size = window_size
        self.base = base
        self.mod = mod
        self.current_hash = 0
        self.length = 0

        self.powers = [0]*self.window_size
        self.powers[0] = 1
        for i in range(1, self.window_size):
            self.powers[i] = (self.powers[i-1] * base) % mod

    def add_character(self, char: str):
        if len(self.chars) == self.window_size:
            old = self.chars.popleft()
            self.current_hash = (self.current_hash - (ord(old) - ord('a') + 1) * self.powers[self.window_size-1]) % self.mod

        self.current_hash = (self.current_hash * self.base) % self.mod
        self.current_hash = (self.current_hash + (ord(char) - ord('a') + 1) % self.mod)
        self.chars.append(char)

    def get_hash(self):
        return self.current_hash
    

def search(p: str, s: str):
    pattern = RabinKarp(len(p))
    for c in p:
        pattern.add_character(c)
    hash_search = pattern.get_hash()

    search = RabinKarp(len(p))
    for i,c in enumerate(s):
        search.add_character(c)
        if i >= len(p)-1:
            if search.get_hash() == hash_search:
                return s[i-len(p)+1:i+1] == p
    return False

print(search(p, s))