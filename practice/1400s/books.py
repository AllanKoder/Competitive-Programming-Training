n, t = map(int, input().split())
a = list(map(int, input().split()))

left = 0
current_sum = 0
max_books = 0

for right in range(n):
    current_sum += a[right]
    while current_sum > t:
        current_sum -= a[left]
        left += 1
    max_books = max(max_books, right - left + 1)

print(max_books)
