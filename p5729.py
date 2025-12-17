w, x, h = map(int, input().strip().split())
q = int(input().strip())

cube = [[[1 for _ in range(h + 1)] for _ in range(x + 1)] for _ in range(w + 1)]
for _ in range(q):
    x1, y1, z1, x2, y2, z2 = map(int, input().strip().split())
