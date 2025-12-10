# 面对大数组会超内存

'''
n, k = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

print(nums[max(k - 1, 0)])
'''

# 分治法 4 3 2 1 5 -> 2 5 4 1 3
import sys
import random
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
nums = list(map(int, input().split()))

class Solution:
    def partition(self, nums, left, right):
        idx = random.randint(left, right)
        nums[idx], nums[left] = nums[left], nums[idx]

        pivot = nums[left]
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= pivot:
                j -= 1
            while i < j and nums[i] <= pivot:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[i], nums[left] = nums[left], nums[i]
        return i
    

    def findKthsmallest(self, nums, left, right, k):
        if left <= right:
            idx = self.partition(nums, left, right)
            if idx == k:
                return nums[idx]
            elif idx < k:
                return self.findKthsmallest(nums, idx + 1, right, k)
            else:
                return self.findKthsmallest(nums, left, idx - 1, k)
        return -1
    
    def k_smallest(self, nums, k):
        l, r = 0, n - 1
        while l <= r:
            pos = self.partition(nums, l, r)
            if pos == k:
                return nums[pos]
            elif pos < k:
                l = pos + 1
            else:
                r = pos - 1
        return -1
    
# print(Solution().findKthsmallest(nums, 0, n - 1, k))
print(Solution().k_smallest(nums, k)) 