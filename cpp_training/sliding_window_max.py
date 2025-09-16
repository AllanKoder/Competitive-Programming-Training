from collections import deque

k = int(input())
arr = list(map(int, input().split()))
class MaxSlider:
    def __init__(self, k, arr):
        self.queue = deque([])
        self.k = k
        self.arr = arr

        for i in range(k):
            self.add(i)

    def add(self, i):
        while len(self.queue) > 0 and self.arr[i] > self.arr[self.queue[-1]]:
            self.queue.pop()
        self.queue.append(i)

    def remove(self, i):
        if len(self.queue) > 0 and i >= self.queue[0]:
            self.queue.popleft()
    
    def max(self):
        return self.arr[self.queue[0]]

def solve(arr, k):
    # Initialize the first k elements
    max_slider = MaxSlider(k, arr)
    result = [max_slider.max()]

    # Go through the array and remove the top while it is smaller than the new
    for i in range(k, len(arr)):
        max_slider.remove(i-k)
        max_slider.add(i)
        result.append(max_slider.max())

    return result


print(" ".join(str(a) for a in solve(arr, k)))
