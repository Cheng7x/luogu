n, m = map(int, input().split())
minimum = min(n, m)

square = 0
for k in range(1, minimum + 1):
    square += (n - k + 1) * (m - k + 1)

rect_all = n * (n + 1) // 2 * m * (m + 1) // 2

rect_only = rect_all - square

print(square, rect_only)