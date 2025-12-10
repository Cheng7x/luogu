time = [tuple(map(int, input().split())) for _ in range(7)]

out, i = 0, 0
for (x, y) in time:
    i += 1
    if max(x + y, out) > 8:
        ...