l, m = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(m)]

trees = [1] * (l + 1)
for i in range(m):
    trees[area[i][0]:area[i][1] + 1] = [0] * (area[i][1] + 1 - area[i][0])

print(sum(trees))