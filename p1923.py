# 面对大数组会超内存

'''
n, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

print(nums[max(k - 1, 0)])
'''

# 分治法
