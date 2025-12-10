# 集合去重 + 列表内置排序
'''n = int(input().strip())
nums = list(map(int, input().split()))

nums = set(nums)
nums = list(nums)
nums.sort()

print(len(nums))
print(*nums)
'''

# 布尔标记数组
n = int(input().strip())
nums = list(map(int, input().split()))

vis = [False] * 1001
result = []

for num in sorted(nums):
    if not vis[num]:
        vis[num] = True
        result.append(num)

print(len(result))
for num in result:
    print(num, end=" ")