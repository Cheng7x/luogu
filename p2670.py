n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
    
def count_mines(x, y):
    directions = [
        (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in directions:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "*":
            count += 1
    return count

for i in range(n):
    for j in range(m):
        if grid[i][j] == "?":
            grid[i][j] = str(count_mines(i, j))

print("\n".join(''.join(row) for row in grid))