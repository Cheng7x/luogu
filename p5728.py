n = int(input())
scores = [list(map(int, input().strip().split())) for _ in range(n)]

count = 0
for i in range(n):
    for j in range(n):
        if i != j:
            a, b, c = scores[i]
            x, y, z = scores[j]
            if abs(x - a) <= 5 and abs(b - y) <= 5 and abs(c - z) <= 5 and abs(sum(scores[i]) - sum(scores[j])) <= 10:
                count += 1
                
print(count // 2)