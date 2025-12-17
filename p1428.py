n = int(input().strip())
nums = list(map(int, input().strip().split()))

degree = []
for idx, val in enumerate(nums):
    count = 0
    for i in nums[:idx]:
        if val > i:
            count += 1
    degree.append(count)

print(*degree)
    