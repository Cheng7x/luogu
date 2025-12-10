n = int(input().strip())

nums = list(map(int, input().split()))
nums.sort()

# print(" ".join(map(str, nums)))
print(*nums)