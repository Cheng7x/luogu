n, m = map(int, input().split())

toys = []
for _ in range(n):
    line = input().split()
    toys.append((int(line[0]), line[1]))
code = []
for _ in range(m):
    a, s = map(int, input().split())
    code.append((a, s))

pos = 0
for towards,step in code:
    toy_dir = toys[pos][0]
    if (towards, toy_dir) in [(0,0), (1,1)]: #顺时针
        pos = (pos - step + n) % n
    else:
        pos = (pos + step) % n
print(toys[pos][1])
        
        
