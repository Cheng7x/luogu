time = [tuple(map(int, input().split())) for _ in range(7)]

out, val = 0, 0
for i, (x, y) in enumerate(time, 1):
    if x + y > 8 and x + y > val:
        val = x + y
        out = i
print(out)
