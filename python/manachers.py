s = input()

class Manachers():
    def __init__(self, s: str):
        self.s = s
        
        self.new_string = '^' + str("#".join(s)) + '$'
        self.length = [1]* len(self.new_string)
        
        l,r = 1,1
        for i in range(1, len(self.new_string)-1):
            mirrored_index = l+r-i
            if i < r:
                self.length[i] = min(r-i, self.length[mirrored_index])
            
            while self.new_string[i - self.length[i]] == self.new_string[i + self.length[i]]:
                self.length[i] += 1
            
            if self.length[i] + i > r:
                r = self.length[i] + i
                l = self.length[i] - i

    def get_longest_palindrome(self):
        return max(self.length)

    def get_length(self, index, odd_lengthed):
        transformed_index = 1 + 2 * index + 0 if odd_lengthed else 1
        return self.length(transformed_index)




m = Manachers(s)
print(m.get_longest_palindrome())