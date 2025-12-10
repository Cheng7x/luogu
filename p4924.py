n, m = map(int, input().split())

matrix = [[0] * n for _ in range(n)]

num = 1
for i in range(n):
    for j in range(n):
        matrix[i][j] = num
        num += 1

code = []
for _ in range(m):
    x, y, r, z = map(int, input().split())
    code.append((x, y, r, z))
    
def rotate(x, y, radius, z):
    r = 2 * radius + 1

    if z == 0:
        ...

    if z == 1:
        for i in range(y - r, y + r + 1):
            for j in range(x - r, x - r + 1):
                ...
                
    return matrix
    
for i in range(m):
    out = rotate(code[i][0], code[i][1], code[i][2], code[i][3])
print('\n'.join(' '.join(row) for row in out))

