s = input()

class Manachers():
    def __init__(self, s: str):
        self.s = s
        
        self.new_string = '^#' + "#".join(s) + '#$'
        self.length = [0]* len(self.new_string)
        
        l,r = 1,1
        for i in range(1, len(self.new_string)-1):
            mirrored_index = l+r-i
            if i < r:
                self.length[i] = min(r-i, self.length[mirrored_index])
            
            while self.new_string[i - 1 - self.length[i]] == self.new_string[i + 1 + self.length[i]]:
                self.length[i] += 1
            
            if self.length[i] + i > r:
                r = i + self.length[i]
                l = i - self.length[i]

    def get_longest_palindrome(self):
        return max(self.length)

    def get_length(self, index, odd_lengthed = True):
        transformed_index = 2 + 2 * index + (0 if odd_lengthed else 1)
        return self.length[transformed_index]


m = Manachers(s)
print(m.get_longest_palindrome())
print(m.length)
print(m.new_string)
print(m.get_length(2))