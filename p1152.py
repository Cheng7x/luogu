nums = list(map(int, input().split()))
n = nums.pop(0)
diff = set()

for i in range(1, n - 1):
    diff.add(abs(nums[i] - nums[i - 1]))

if len(diff) == n - 1 and all(1 <= d <= n - 1 for d in diff):
    print("Jolly")
else:
    print("Not jolly")